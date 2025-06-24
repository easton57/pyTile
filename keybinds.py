import keyboard

# Define your main modifier
MAIN_MOD = 'windows'

# Example keybinds mapping Hyprland to Windows
KEYBINDS = [
    # (hotkey, action)
    (f'{MAIN_MOD}+t', 'open_terminal'),
    (f'{MAIN_MOD}+b', 'open_browser'),
    (f'{MAIN_MOD}+q', 'close_window'),
    (f'{MAIN_MOD}+v', 'toggle_floating'),
    (f'{MAIN_MOD}+left', 'focus_left'),
    (f'{MAIN_MOD}+right', 'focus_right'),
    (f'{MAIN_MOD}+up', 'focus_up'),
    (f'{MAIN_MOD}+down', 'focus_down'),
    (f'{MAIN_MOD}+1', 'switch_workspace_1'),
    (f'{MAIN_MOD}+2', 'switch_workspace_2'),
    (f'{MAIN_MOD}+3', 'switch_workspace_3'),
    (f'{MAIN_MOD}+shift+1', 'move_window_workspace_1'),
    (f'{MAIN_MOD}+shift+2', 'move_window_workspace_2'),
    (f'{MAIN_MOD}+shift+3', 'move_window_workspace_3'),
]

# Example: registering keybinds (to be used in main.py)
def register_keybinds(callback):
    for hotkey, action in KEYBINDS:
        keyboard.add_hotkey(hotkey, callback, args=(action,)) 