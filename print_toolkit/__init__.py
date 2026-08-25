from . import *

from time import sleep

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

RESET = "\033[0m"

styles = {
    "minusplus": ("-", "+"),
    "zeroone": ("0", "1"),
    "blocks": ("░", "█"),
    "circles": ("○", "●"),
    "squares": ("□", "■"),
    "hash": (".", "#"),
    "lines": ("\\", "/")
}

def print_box(title = None, text = "", width = None, border = "=", color = None):
    if width is None:
        title_len = len(title) if title else 0
        text_len = len(text)
        width = max(title_len, text_len, 20) + 4

    title_part = f"{title} " if title else ""
    title_len = len(title_part)

    top = f"┌─{title_part}{border * (width - title_len - 1)}┐"
    mid = f"│ {text}{' ' * (width - len(text) - 2)} │"
    bot = f"└{'─' * (width - 1)}┘"

    if color:
        printclr(top, color)
        printclr(mid, color)
        printclr(bot, color)

    else:
        printclr(top)
        printclr(mid)
        printclr(bot)

def printclr(text, color = None, sep = " ", end = "\n"):
    if color:
        print(f"{color}{text}{RESET}", sep=sep, end=end)
    else:
        print(text, sep=sep, end=end)
def printrgb(text, r = None, g = None, b = None, sep = " ", end = "\n"):
    if not (r is None and g is None and b is None):
        print(f"\033[38;2;{r};{g};{b}m{text}{RESET}", sep=sep, end=end)
    else:
        print(text, sep=sep, end=end)

def visload(style = "default", text = "Loading: ", start = 1, end = 100, delay = 0.1, color = None):
    total = start
    if style == "default":
        while total <= end:
            percent = ((total - start) / (end - start)) * 100
            status = f"{total}/{end}"
            printclr(f"\r{text}{status} [{round(percent)}%]", color, end = "")
            total += 1
            sleep(delay)

    elif style in styles:
        empty, filled = styles[style]
        line = list(empty * (end - start + 1))
        while total <= end:
            percent = ((total - start) / (end - start)) * 100
            line[total - 1] = filled
            bar = "".join(line)

            status = f"{total}/{end}"
            printclr(f"\r{text}{bar} {status} | {round(percent)}%", color, end = "")
            sleep(delay)
            total += 1

    print()
