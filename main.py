import time
from keybinds import register_keybinds

def handle_action(action):
    print(f'Action triggered: {action}')
    # TODO: Implement real window management actions here

if __name__ == '__main__':
    register_keybinds(handle_action)
    print('pyTile (Windows) running. Press Ctrl+C to exit.')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Exiting pyTile.') 