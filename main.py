import time
from keybinds import register_keybinds
from window_manager import WindowManager

def handle_action(action, wm):
    print(f'Action triggered: {action}')
    
    if action.startswith('switch_workspace_'):
        workspace_id = int(action.split('_')[-1]) - 1  # Convert 1-based to 0-based
        wm.switch_workspace(workspace_id)
        print(f'Switched to workspace {workspace_id + 1}')
    elif action.startswith('move_window_workspace_'):
        workspace_id = int(action.split('_')[-1]) - 1  # Convert 1-based to 0-based
        wm.move_window_to_workspace(workspace_id)
        print(f'Moved window to workspace {workspace_id + 1}')
    elif action == 'toggle_floating':
        wm.toggle_floating()
        print('Toggled floating state')
    elif action in ['focus_left', 'focus_up', 'focus_prev']:
        wm.focus_window("prev")
        print('Focused previous window')
    elif action in ['focus_right', 'focus_down', 'focus_next']:
        wm.focus_window("next")
        print('Focused next window')
    elif action == 'close_window':
        if wm.focused_window:
            import win32gui
            import win32con
            win32gui.PostMessage(wm.focused_window, win32con.WM_CLOSE, 0, 0)
            print('Closed focused window')
    elif action == 'open_terminal':
        import subprocess
        subprocess.Popen(['cmd.exe'])
        print('Opened terminal')
    elif action == 'open_browser':
        import subprocess
        subprocess.Popen(['start', 'https://www.google.com'], shell=True)
        print('Opened browser')
    elif action == 'open_explorer':
        import subprocess
        subprocess.Popen(['explorer.exe'])
        print('Opened file explorer')
    elif action == 'toggle_fullscreen':
        if wm.focused_window:
            import win32gui
            import win32con
            # Toggle fullscreen state
            style = win32gui.GetWindowLong(wm.focused_window, win32con.GWL_STYLE)
            if style & win32con.WS_MAXIMIZE:
                win32gui.ShowWindow(wm.focused_window, win32con.SW_RESTORE)
            else:
                win32gui.ShowWindow(wm.focused_window, win32con.SW_MAXIMIZE)
            print('Toggled fullscreen')
    elif action == 'toggle_maximize':
        if wm.focused_window:
            import win32gui
            import win32con
            # Toggle maximize state
            style = win32gui.GetWindowLong(wm.focused_window, win32con.GWL_STYLE)
            if style & win32con.WS_MAXIMIZE:
                win32gui.ShowWindow(wm.focused_window, win32con.SW_RESTORE)
            else:
                win32gui.ShowWindow(wm.focused_window, win32con.SW_MAXIMIZE)
            print('Toggled maximize')
    elif action == 'cycle_layout':
        # Cycle through different layout modes
        layouts = ["tile", "float", "monocle"]
        current_index = layouts.index(wm.layout_mode)
        wm.layout_mode = layouts[(current_index + 1) % len(layouts)]
        wm.apply_layout()
        print(f'Switched to {wm.layout_mode} layout')
    elif action == 'reload_config':
        # Reload configuration (placeholder for future config system)
        print('Reloaded configuration')

if __name__ == '__main__':
    wm = WindowManager()
    
    # Create a callback function that includes the window manager
    def action_callback(action):
        handle_action(action, wm)
    
    register_keybinds(action_callback)
    print('pyTile (Windows) running. Press Ctrl+C to exit.')
    print('Current workspace:', wm.current_workspace + 1)
    print('Available keybinds:')
    print('  Win+1-0: Switch workspaces')
    print('  Win+Shift+1-0: Move window to workspace')
    print('  Win+Arrow keys: Focus windows')
    print('  Win+Tab: Focus next window')
    print('  Win+V: Toggle floating')
    print('  Win+Q: Close window')
    print('  Win+T: Open terminal')
    print('  Win+B: Open browser')
    print('  Win+E: Open explorer')
    print('  Win+Space: Cycle layouts')
    
    try:
        while True:
            wm.update_windows()
            wm.apply_layout()
            time.sleep(0.5)  # Reduced sleep time for more responsive updates
    except KeyboardInterrupt:
        print('Exiting pyTile.') 