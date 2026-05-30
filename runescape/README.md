# Runescape Python Automation Scripts

This folder contains two standalone Python automation scripts that use screen/mouse automation and image matching.

## Files

- `highalch.py`: Repeats a fixed mouse-click sequence a set number of times.
- `rsmagic.py`: Moves across preset coordinates and looks for the `attack_hobgoblin.png` template on screen, then clicks it.
- `attack_hobgoblin.png`: Template image used by `rsmagic.py` for OpenCV matching.
- `hobgoblin1.png` to `hobgoblin4.png`: Currently not used by active code (leftover/experimental assets from commented logic).

## Requirements

- Python 3.9+
- Windows (current coordinates are hardcoded for one screen/client layout)
- Python packages:
  - `pyautogui`
  - `opencv-python`
  - `numpy`

Install dependencies:

```powershell
pip install pyautogui opencv-python numpy
```

## Important Behavior and Safety

These scripts control your mouse. Keep this in mind before running:

- Move your mouse to the top-left corner of the screen to trigger PyAutoGUI failsafe (`pyautogui.FailSafeException`) and stop execution.
- Use `Ctrl+C` in the terminal to stop a running script.
- Do not interact with other windows while scripts are running.
- Coordinates are absolute pixel positions and may not match your resolution/UI scale.

## Script Details

### `highalch.py`

What it does:

- Sets `count = 374`.
- Repeats until count reaches 0:
  - Moves mouse to `(1548, 336)`.
  - Left-clicks once.
  - Waits 0.1-0.3 seconds.
  - Left-clicks again.
  - Waits 2.3 seconds.
  - Decrements and prints remaining `count`.

How to run:

```powershell
python highalch.py
```

Common customization:

- Change repetitions by editing `count`.
- Change click target by editing `pyautogui.moveTo(1548, 336)`.
- Tune delays for your timing needs.

### `rsmagic.py`

What it does:

- Iterates through a hardcoded `coordinates` list.
- For each point:
  - Adds small random offset to mouse movement.
  - Moves mouse to that adjusted location.
  - Takes screenshot and performs OpenCV template match with `attack_hobgoblin.png`.
  - If match score is `>= 0.8`, clicks near the center with a small random offset.
  - Waits 1-3 seconds before next coordinate.

How to run:

```powershell
python rsmagic.py
```

Common customization:

- Update `coordinates` for your layout.
- Adjust match sensitivity by changing `threshold = 0.8` in `find_attack_option()`.
- Replace `attack_hobgoblin.png` with a cleaner screenshot if detection is unreliable.

## Getting Screen Coordinates

Both scripts include commented helper code that prints live mouse position. To use it:

1. Uncomment the mouse-position loop at the bottom of the script.
2. Run the script.
3. Move mouse to target spots and note `(x, y)` values.
4. Re-comment helper loop and apply coordinates in code.

## Troubleshooting

- Script does nothing useful:
  - Verify game window position/size is exactly what coordinates expect.
  - Confirm DPI scaling is consistent (100% scaling is easiest).
- Template not found:
  - Re-capture `attack_hobgoblin.png` at current resolution/UI theme.
  - Lower threshold slightly (for example `0.75`) if false negatives are high.
- Immediate stop with failsafe exception:
  - Mouse likely touched top-left corner; rerun and keep cursor away from `(0, 0)`.

## Notes

- These are standalone scripts; there is no shared module structure or CLI flags.
- To add safer controls, consider adding a hotkey listener or explicit countdown before automation starts.
