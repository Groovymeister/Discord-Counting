import keyboard

def count(num):
    return None

def main():
    num = int(input("Please enter your starting number: "))
    keyboard.add_hotkey('F9', exit)
    keyboard.add_hotkey('F10', count, args = (num))
    


if __name__ == "__main__":
    main()