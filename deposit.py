import time as t
from pywinauto import Application
from pywinauto.keyboard import SendKeys
#Use Discord Canary for this Process

def main():
    app = Application().connect(process=3952)
    while True:
        app.window(title = "#gambling | RIT Frens - Discord").send_keystrokes('!dep all' + '{ENTER}')
        t.sleep(600)


if __name__ == "__main__":
    main()