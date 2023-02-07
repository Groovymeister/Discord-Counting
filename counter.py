from pynput import keyboard
import time as t
from pywinauto import Application
from pywinauto.keyboard import SendKeys

NUM = 0
app = Application().connect(process=10520)

def on_press_start(key):
    if key == keyboard.Key.f10:
        count()

def on_press_loop(key):
    if key == keyboard.Key.f9:
        global NUM
        NUM = int(input("Enter new number: "))
        return False

def count():
    global NUM
    with keyboard.Listener(on_press=on_press_loop) as listener:
        while True:
            NUM += 1
            app.window(title = "#couting | RIT Frens - Discord").send_keystrokes(str(NUM) + '{ENTER}')
            t.sleep(2)
            if not listener.running:
                break

def main():
    global NUM
    NUM = int(input("Enter last number: "))
    with keyboard.Listener(on_press=on_press_start) as listener:
        listener.join()


if __name__ == "__main__":
    main()