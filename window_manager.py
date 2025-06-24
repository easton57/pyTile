import win32gui
import win32con
import win32api
import win32process
import win32com.client

class WindowManager:
    def __init__(self):
        self.windows = []
        self.prev_window_handles = set()

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
        self.windows = self.get_top_level_windows()
        return self.windows

    def apply_layout(self):
        n = len(self.windows)
        if n == 0:
            return
        screen = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0,0)))['Monitor']
        x0, y0, x1, y1 = screen
        width = x1 - x0
        height = y1 - y0
        if n == 1:
            # Maximize the only window
            hwnd = self.windows[0]
            win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        else:
            # Tile horizontally
            tile_width = width // n
            for i, hwnd in enumerate(self.windows):
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                win32gui.MoveWindow(
                    hwnd,
                    x0 + i * tile_width,
                    y0,
                    tile_width,
                    height,
                    True
                ) 