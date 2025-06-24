#!/usr/bin/env python3
"""
Simple test script to verify tiling functionality
"""

import time
import subprocess
import win32gui
from window_manager import WindowManager

def test_tiling():
    print("Testing pyTile window manager...")
    
    # Create window manager
    wm = WindowManager()
    
    # Open some test applications
    print("Opening test applications...")
    apps = [
        ['notepad.exe'],
        ['calc.exe'],
        ['mspaint.exe']
    ]
    
    processes = []
    for app in apps:
        try:
            proc = subprocess.Popen(app)
            processes.append(proc)
            print(f"Opened {app[0]}")
        except Exception as e:
            print(f"Failed to open {app[0]}: {e}")
    
    # Wait for windows to appear
    print("Waiting for windows to appear...")
    time.sleep(3)
    
    # Test tiling
    print("Testing tiling...")
    wm.update_windows()
    print(f"Found {len(wm.windows)} windows in workspace {wm.current_workspace + 1}")
    
    for i, hwnd in enumerate(wm.windows):
        try:
            title = win32gui.GetWindowText(hwnd)
            print(f"  Window {i+1}: {title}")
        except:
            print(f"  Window {i+1}: <unknown>")
    
    # Apply layout
    wm.apply_layout()
    print("Applied tiling layout")
    
    # Test workspace switching
    print("Testing workspace switching...")
    wm.switch_workspace(1)
    print(f"Switched to workspace {wm.current_workspace + 1}")
    
    # Test focus
    if wm.windows:
        wm.focus_window("next")
        print("Focused next window")
    
    # Clean up
    print("Cleaning up...")
    for proc in processes:
        try:
            proc.terminate()
        except:
            pass
    
    print("Test completed!")

if __name__ == "__main__":
    test_tiling() 