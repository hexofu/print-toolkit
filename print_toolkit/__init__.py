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




printrgb("Hello ")
visload(text = "Загрузка: ", start = 1, end = 50, delay = 0.1, color = GREEN)
visload(text = "Загрузка: ", style = "minusplus", start = 1, end = 50, delay = 0.1, color = GREEN)
visload(text = "Загрузка: ", style = "circles", start = 1, end = 50, delay = 0.1, color = BLUE)
visload(text = "Загрузка: ", style = "squares", start = 1, end = 50, delay = 0.1, color = BLUE)
visload(text = "Загрузка: ", style = "lines", start = 1, end = 50, delay = 0.1, color = RED)
