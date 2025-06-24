import keyboard

# Define your main modifier
MAIN_MOD = 'windows'

# Enhanced keybinds mapping Hyprland to Windows
KEYBINDS = [
    # Application launching
    (f'{MAIN_MOD}+t', 'open_terminal'),
    (f'{MAIN_MOD}+b', 'open_browser'),
    (f'{MAIN_MOD}+e', 'open_explorer'),
    
    # Window management
    (f'{MAIN_MOD}+q', 'close_window'),
    (f'{MAIN_MOD}+v', 'toggle_floating'),
    (f'{MAIN_MOD}+f', 'toggle_fullscreen'),
    (f'{MAIN_MOD}+m', 'toggle_maximize'),
    
    # Window focus
    (f'{MAIN_MOD}+left', 'focus_left'),
    (f'{MAIN_MOD}+right', 'focus_right'),
    (f'{MAIN_MOD}+up', 'focus_up'),
    (f'{MAIN_MOD}+down', 'focus_down'),
    (f'{MAIN_MOD}+tab', 'focus_next'),
    (f'{MAIN_MOD}+shift+tab', 'focus_prev'),
    
    # Workspace switching
    (f'{MAIN_MOD}+1', 'switch_workspace_1'),
    (f'{MAIN_MOD}+2', 'switch_workspace_2'),
    (f'{MAIN_MOD}+3', 'switch_workspace_3'),
    (f'{MAIN_MOD}+4', 'switch_workspace_4'),
    (f'{MAIN_MOD}+5', 'switch_workspace_5'),
    (f'{MAIN_MOD}+6', 'switch_workspace_6'),
    (f'{MAIN_MOD}+7', 'switch_workspace_7'),
    (f'{MAIN_MOD}+8', 'switch_workspace_8'),
    (f'{MAIN_MOD}+9', 'switch_workspace_9'),
    (f'{MAIN_MOD}+0', 'switch_workspace_10'),
    
    # Move windows between workspaces
    (f'{MAIN_MOD}+shift+1', 'move_window_workspace_1'),
    (f'{MAIN_MOD}+shift+2', 'move_window_workspace_2'),
    (f'{MAIN_MOD}+shift+3', 'move_window_workspace_3'),
    (f'{MAIN_MOD}+shift+4', 'move_window_workspace_4'),
    (f'{MAIN_MOD}+shift+5', 'move_window_workspace_5'),
    (f'{MAIN_MOD}+shift+6', 'move_window_workspace_6'),
    (f'{MAIN_MOD}+shift+7', 'move_window_workspace_7'),
    (f'{MAIN_MOD}+shift+8', 'move_window_workspace_8'),
    (f'{MAIN_MOD}+shift+9', 'move_window_workspace_9'),
    (f'{MAIN_MOD}+shift+0', 'move_window_workspace_10'),
    
    # Layout controls
    (f'{MAIN_MOD}+space', 'cycle_layout'),
    (f'{MAIN_MOD}+r', 'reload_config'),
]

def register_keybinds(callback):
    """Register all keybinds with the callback function"""
    for hotkey, action in KEYBINDS:
        try:
            keyboard.add_hotkey(hotkey, callback, args=(action,))
            print(f"Registered hotkey: {hotkey} -> {action}")
        except Exception as e:
            print(f"Failed to register hotkey {hotkey}: {e}")

def unregister_all_keybinds():
    """Unregister all keybinds"""
    keyboard.unhook_all() 