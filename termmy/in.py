import sys

if sys.platform == "win32":
    import msvcrt

    def getch():
        return msvcrt.getch().decode("utf-8")  # Read single byte, decode to UTF-8

else:
    import tty
    import termios

    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)  # Set to raw mode
            ch = sys.stdin.read(1)  # Read one character
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # Restore settings
        return ch

if __name__ == "__main__":
    while True: print(repr(getch()))