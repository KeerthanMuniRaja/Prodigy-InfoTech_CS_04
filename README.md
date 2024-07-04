# Simple Keylogger

## Purpose
The purpose of this project is to create a basic keylogger in Python using the `pynput` library. This keylogger captures and logs keystrokes from the user's keyboard input, providing a way to record and monitor typed text.

## Description
This script listens for keyboard events using `pynput`'s `Listener` class. It records each keystroke and logs it into a text file (`keylog.txt`). Special keys like space and enter are handled separately, while other keys are logged directly. Pressing the escape key (`Key.esc`) terminates the keylogging process.

## How It Works
1. **Keylogging:**
   - The script uses `pynput.keyboard.Listener` to listen for key press events.
   - On each key press, it determines the type of key and logs the corresponding character or special key (space, enter) into `keylog.txt`.
   - Pressing the escape key (`Key.esc`) stops the keylogging process and exits the program.

2. **Output:**
   - All logged keystrokes are stored in the `keylog.txt` file in real-time as they are typed.
   - The file accumulates a record of all keys pressed until the logger is stopped.

## Example Usage
1. **Start Keylogger:**
   - Run the script to initiate the keylogging process.
   - The program starts listening for keyboard inputs silently in the background.

2. **Logging Keystrokes:**
   - As the user types, each keystroke is recorded and appended to the `keylog.txt` file.
   - Special keys like space and enter are converted to their respective representations in the log.

3. **Stopping the Keylogger:**
   - Press the escape key (`Key.esc`) to stop the keylogging process.
   - The program terminates, and the log file (`keylog.txt`) contains all captured keystrokes.

## Notes
- Ensure Python and the `pynput` library are installed to run the script.
- Use this keylogger responsibly and in accordance with legal and ethical guidelines.
