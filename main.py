import time
from keybinds import register_keybinds
from window_manager import WindowManager

def handle_action(action):
    print(f'Action triggered: {action}')
    # TODO: Implement real window management actions here

if __name__ == '__main__':
    register_keybinds(handle_action)
    wm = WindowManager()
    print('pyTile (Windows) running. Press Ctrl+C to exit.')
    try:
        while True:
            wm.update_windows()
            wm.apply_layout()
            time.sleep(1)
    except KeyboardInterrupt:
        print('Exiting pyTile.') 