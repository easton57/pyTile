# pyTile (Windows)

A tiling window manager for Windows, inspired by Hyprland and built in Python.

## Features
- **Smart Tiling Layouts**: Automatic grid-based tiling that adapts to screen aspect ratio
- **Workspace Management**: 10 virtual workspaces with easy switching
- **Multiple Layout Modes**: Tile, Float, and Monocle layouts
- **Window Focus Management**: Navigate between windows with keyboard shortcuts
- **Floating Windows**: Toggle windows between tiled and floating states
- **Customizable Keybindings**: Hyprland-inspired keybindings (fully customizable)
- **Application Launcher**: Quick application launching via hotkeys

## Requirements
- Python 3.8+
- Windows 10/11
- See `requirements.txt` for Python dependencies

## Setup
```sh
pip install -r requirements.txt
```

## Usage
```sh
python main.py
```

## Keybindings

### Workspace Management
- `Win+1-0`: Switch to workspace 1-10
- `Win+Shift+1-0`: Move focused window to workspace 1-10

### Window Focus
- `Win+Arrow Keys`: Focus windows in different directions
- `Win+Tab`: Focus next window
- `Win+Shift+Tab`: Focus previous window

### Window Management
- `Win+V`: Toggle floating state
- `Win+Q`: Close focused window
- `Win+F`: Toggle fullscreen
- `Win+M`: Toggle maximize

### Application Launcher
- `Win+T`: Open terminal (cmd.exe)
- `Win+B`: Open browser
- `Win+E`: Open file explorer

### Layout Controls
- `Win+Space`: Cycle through layout modes (Tile → Float → Monocle)

## Layout Modes

### Tile Mode
- **1 Window**: Maximized
- **2 Windows**: Split screen (left/right)
- **3-4 Windows**: 2x2 grid
- **5+ Windows**: Smart grid based on screen aspect ratio

### Float Mode
Windows maintain their original positions and sizes. No automatic tiling.

### Monocle Mode
Only the focused window is visible (maximized). Other windows are minimized.

## Configuration
Keybindings are defined in `keybinds.py` and can be customized by editing the `KEYBINDS` list.

## Testing
Run the test script to verify functionality:
```sh
python test_tiling.py
```

## Troubleshooting

### Windows Not Tiling Properly
- Make sure you're in Tile mode (not Float or Monocle)
- Check that windows are not floating (use `Win+V` to toggle)
- Ensure windows are on the current workspace

### Keybindings Not Working
- Run as administrator if needed
- Check that no other applications are using the same keybindings
- Verify Python dependencies are installed correctly

---
**Note:** This project is in active development. Expect bugs and missing features! 