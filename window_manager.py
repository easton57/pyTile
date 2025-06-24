import win32gui
import win32con
import win32api
import win32process
import win32com.client
import math

class WindowManager:
    def __init__(self):
        self.windows = []
        self.workspaces = [[] for _ in range(10)]  # 10 workspaces
        self.current_workspace = 0
        self.floating_windows = set()
        self.focused_window = None
        self.layout_mode = "tile"  # "tile", "float", "monocle"
        
    def is_window_valid(self, hwnd):
        if not win32gui.IsWindowVisible(hwnd):
            return False
        if win32gui.IsIconic(hwnd):
            return False
        # Filter out tool windows, etc.
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        if style & win32con.WS_EX_TOOLWINDOW:
            return False
        # Filter out invisible/empty titles
        title = win32gui.GetWindowText(hwnd)
        if not title.strip():
            return False
        return True

    def get_top_level_windows(self):
        windows = []
        def callback(hwnd, extra):
            if self.is_window_valid(hwnd):
                windows.append(hwnd)
        win32gui.EnumWindows(callback, None)
        return windows

    def update_windows(self):
        all_windows = self.get_top_level_windows()
        
        # Update workspace assignments for new windows
        for hwnd in all_windows:
            if hwnd not in [w for ws in self.workspaces for w in ws]:
                # New window - assign to current workspace
                self.workspaces[self.current_workspace].append(hwnd)
        
        # Remove windows that no longer exist
        for i, workspace in enumerate(self.workspaces):
            self.workspaces[i] = [w for w in workspace if w in all_windows]
        
        # Update current workspace windows
        self.windows = self.workspaces[self.current_workspace]
        
        # Auto-focus the most recently active window if no focus
        if not self.focused_window and self.windows:
            self.focused_window = self.get_most_recent_window()
        
        return self.windows

    def get_screen_info(self):
        """Get primary monitor information"""
        screen = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0,0)))['Monitor']
        x0, y0, x1, y1 = screen
        return x0, y0, x1, y1

    def apply_layout(self):
        """Apply the current layout to windows in the current workspace"""
        tiled_windows = [w for w in self.windows if w not in self.floating_windows]
        n = len(tiled_windows)
        
        if n == 0:
            return
            
        x0, y0, x1, y1 = self.get_screen_info()
        width = x1 - x0
        height = y1 - y0
        
        if self.layout_mode == "float":
            # In float mode, don't tile windows - let them keep their positions
            return
        elif self.layout_mode == "monocle":
            # Monocle mode - only show the focused window, maximize it
            if self.focused_window and self.focused_window in tiled_windows:
                # Maximize focused window
                win32gui.ShowWindow(self.focused_window, win32con.SW_MAXIMIZE)
                # Minimize all other windows
                for hwnd in tiled_windows:
                    if hwnd != self.focused_window:
                        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            elif tiled_windows:
                # If no focused window, focus the first one
                self.focused_window = tiled_windows[0]
                win32gui.ShowWindow(self.focused_window, win32con.SW_MAXIMIZE)
                for hwnd in tiled_windows[1:]:
                    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
        else:  # tile mode
            if n == 1:
                # Maximize the only window
                hwnd = tiled_windows[0]
                win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
            elif n == 2:
                # Split screen - left and right
                tile_width = width // 2
                for i, hwnd in enumerate(tiled_windows):
                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                    win32gui.MoveWindow(
                        hwnd,
                        x0 + i * tile_width,
                        y0,
                        tile_width,
                        height,
                        True
                    )
            elif n <= 4:
                # 2x2 grid for 3-4 windows
                cols = 2
                rows = math.ceil(n / cols)
                tile_width = width // cols
                tile_height = height // rows
                
                for i, hwnd in enumerate(tiled_windows):
                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                    col = i % cols
                    row = i // cols
                    win32gui.MoveWindow(
                        hwnd,
                        x0 + col * tile_width,
                        y0 + row * tile_height,
                        tile_width,
                        tile_height,
                        True
                    )
            else:
                # For more than 4 windows, use a more complex layout
                # Calculate optimal grid based on aspect ratio
                aspect_ratio = width / height
                if aspect_ratio > 1.5:  # Wide screen
                    cols = math.ceil(math.sqrt(n * aspect_ratio))
                else:  # Tall screen
                    cols = math.ceil(math.sqrt(n / aspect_ratio))
                
                rows = math.ceil(n / cols)
                tile_width = width // cols
                tile_height = height // rows
                
                for i, hwnd in enumerate(tiled_windows):
                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                    col = i % cols
                    row = i // cols
                    
                    # Handle the last row if it's not full
                    if row == rows - 1 and n % cols != 0:
                        # Distribute remaining windows evenly in the last row
                        remaining = n % cols
                        if remaining == 0:
                            remaining = cols
                        adjusted_width = width // remaining
                        win32gui.MoveWindow(
                            hwnd,
                            x0 + col * adjusted_width,
                            y0 + row * tile_height,
                            adjusted_width,
                            tile_height,
                            True
                        )
                    else:
                        win32gui.MoveWindow(
                            hwnd,
                            x0 + col * tile_width,
                            y0 + row * tile_height,
                            tile_width,
                            tile_height,
                            True
                        )

    def switch_workspace(self, workspace_id):
        """Switch to a different workspace"""
        if 0 <= workspace_id < len(self.workspaces):
            self.current_workspace = workspace_id
            self.update_windows()
            self.apply_layout()

    def move_window_to_workspace(self, workspace_id):
        """Move the focused window to a different workspace"""
        if (0 <= workspace_id < len(self.workspaces) and 
            self.focused_window and 
            self.focused_window in self.windows):
            
            # Remove from current workspace
            if self.focused_window in self.workspaces[self.current_workspace]:
                self.workspaces[self.current_workspace].remove(self.focused_window)
            
            # Add to target workspace
            self.workspaces[workspace_id].append(self.focused_window)
            
            # Update current workspace windows
            self.update_windows()
            self.apply_layout()

    def toggle_floating(self):
        """Toggle floating state of focused window"""
        if self.focused_window and self.focused_window in self.windows:
            if self.focused_window in self.floating_windows:
                self.floating_windows.remove(self.focused_window)
            else:
                self.floating_windows.add(self.focused_window)
            self.apply_layout()

    def focus_window(self, direction):
        """Focus next/previous window"""
        if not self.windows:
            return
            
        if not self.focused_window:
            self.focused_window = self.windows[0]
        else:
            try:
                current_index = self.windows.index(self.focused_window)
                if direction == "next":
                    new_index = (current_index + 1) % len(self.windows)
                else:  # "prev"
                    new_index = (current_index - 1) % len(self.windows)
                self.focused_window = self.windows[new_index]
            except ValueError:
                self.focused_window = self.windows[0]
        
        # Bring focused window to front
        if self.focused_window:
            win32gui.SetForegroundWindow(self.focused_window)
            win32gui.BringWindowToTop(self.focused_window)

    def get_most_recent_window(self):
        """Get the most recently active window from the current workspace"""
        if not self.windows:
            return None
            
        # Try to get the foreground window first
        try:
            foreground = win32gui.GetForegroundWindow()
            if foreground in self.windows:
                return foreground
        except:
            pass
            
        # Fall back to the first window
        return self.windows[0] if self.windows else None 