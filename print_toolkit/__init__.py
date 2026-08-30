from . import *

from time import sleep
from datetime import datetime

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

RESET = "\033[0m"

BOLD = "\033[1m"
STRIKE = "\033[9m"
UNDERLINE = "\033[4m"
ITALIC = "\033[3m"

styles = {
    "minusplus": ("-", "+"),
    "zeroone": ("0", "1"),
    "blocks": ("░", "█"),
    "circles": ("○", "●"),
    "squares": ("□", "■"),
    "hash": (".", "#"),
    "lines": ("\\", "/")
}


def print_box(title=None, text="", width=None, border="=", color=None, style=""):
    if width is None:
        title_len = len(title) if title else 0
        text_len = len(text)
        width = max(title_len, text_len, 20) + 4

    title_part = f"{title} " if title else ""
    title_len = len(title_part)

    top = f"┌─{title_part}{border * (width - title_len - 1)}┐"
    mid = f"│ {text}{' ' * (width - len(text) - 2)} │"
    bot = f"└{'─' * width}┘"

    if color:
        print(f"{style}{color}{top}{RESET}")
        print(f"{style}{color}{mid}{RESET}")
        print(f"{style}{color}{bot}{RESET}")

    else:
        print(f"{style}{top}{RESET}")
        print(f"{style}{mid}{RESET}")
        print(f"{style}{bot}{RESET}")


def printclr(*args, color=None, style="", sep=" ", end="\n"):
    if color:
        colored = [f"{style}{color}{arg}{RESET}" for arg in args]
        print(*colored, sep=sep, end=end)
    else:
        print(*args, sep=sep, end=end)


def printrgb(*args, r=None, g=None, b=None, style="", sep=" ", end="\n"):
    if not (r is None and g is None and b is None):
        colored = [f"{style}\033[38;2;{r};{g};{b}m{arg}{RESET}" for arg in args]
        print(*colored, sep=sep, end=end)
    else:
        print(*args, sep=sep, end=end)


def typewriter(text, delay=0.5, color=None, style=""):
    for char in text:
        if color:
            print(f"{style}{color}{char}{RESET}", end="", flush=True)
        else:
            print(f"{style}{char}", end="", flush=True)
        sleep(delay)
    print(RESET)


def pulse(text, delay=0.5, times=5, color=None, style=""):
    for _ in range(times - 1):
        if color:
            print(f"\r{style}{color}{text}{RESET}", end="", flush=True)
        else:
            print(f"\r{style}{text}", end="", flush=True)
        sleep(delay)
        print(f"\r{' ' * len(text)}", end="", flush=True)
        sleep(delay)
    if color:
        print(f"\r{style}{color}{text}{RESET}")
    else:
        print(f"\r{style}{text}{RESET}")


def visload(style="default", text="Loading: ", start=1, end=100, delay=0.1, color=None):
    total = start
    if style == "default":
        while total <= end:
            percent = ((total - start) / (end - start)) * 100
            status = f"{total}/{end}"
            printclr(f"\r{text}{status} [{round(percent)}%]", color, end="")
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
            printclr(f"\r{text}{bar} {status} | {round(percent)}%", color, end="")
            sleep(delay)
            total += 1

    print()


class Logger:
    LEVELS = {
        "debug": {"color": "\033[90m", "icon": "🐞", "label": "DEBUG"},
        "info": {"color": "\033[94m", "icon": "ℹ️", "label": "INFO"},
        "success": {"color": "\033[92m", "icon": "✅", "label": "SUCCESS"},
        "warning": {"color": "\033[93m", "icon": "📢", "label": "WARNING"},
        "error": {"color": "\033[91m", "icon": "❌", "label": "ERROR"},
        "critical": {"color": "\033[41m", "icon": "❗", "label": "CRITICAL"},
    }

    def __init__(self, name="App", level="info", show_time=True, show_icon=True):
        self.name = name
        level_lower = level.lower()

        self.show_time = show_time
        self.show_icon = show_icon

        self.level_order = ["debug", "info", "success", "warning", "error", "critical"]

        if level_lower in self.level_order:
            self.level = level_lower
            self.min_level = self.level_order.index(level_lower)

        else:
            self.level = "info"
            self.min_level = 1


    def _log(self, level, message, *args, **kwargs):
        end = kwargs.get("end", "\n")
        sep = kwargs.get("sep", " ")

        if self.level not in self.level_order:
            return

        curr_index = self.level_order.index(self.level)
        if curr_index < self.min_level:
            return

        parts = []

        if self.show_time:
            time_str = datetime.now().strftime("%H:%M:%S")
            parts.append(time_str)

        level_data = self.LEVELS[level]
        color = level_data["color"]

        if self.show_icon:
            icon = level_data["icon"]
            label = f"{icon} {level_data['label']}"
        else:
            label = level_data["label"]

        parts.append(f"{color}{label}{RESET}")

        parts.append(f"\033[36m{self.name}{RESET}")

        if args:
            message = message.format(*args)
        parts.append(f"{color}{message}{RESET}")

        print(" ".join(parts), sep=sep, end=end)

    def debug(self, message, *args, **kwargs):
        self._log("debug", message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        self._log("info", message, *args, **kwargs)

    def success(self, message, *args, **kwargs):
        self._log("success", message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        self._log("warning", message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        self._log("error", message, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        self._log("critical", message, *args, **kwargs)

    def set_level(self, level):
        level_lower = level.lower()
        if level_lower in self.level_order:
            self.min_level = self.level_order.index(level_lower)
            self.level = level_lower


# simplified functions
_logger = None


def get_logger(name="App", level="info"):
    global _logger
    if _logger is None or _logger.name != name:
        _logger = Logger(name, level)

    return _logger


def log_debug(msg): get_logger().debug(msg)
def log_info(msg): get_logger().info(msg)
def log_success(msg): get_logger().success(msg)
def log_warning(msg): get_logger().warning(msg)
def log_error(msg): get_logger().error(msg)
def log_critical(msg): get_logger().critical(msg)

__all__ = [
    "BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE", "RESET",

    "BOLD", "STRIKE", "UNDERLINE", "ITALIC",

    "print_box", "printclr", "printrgb",

    "typewriter", "pulse", "visload",

    "Logger", "get_logger", "log_debug", "log_info",
    "log_success", "log_warning", "log_error", "log_critical",

    "styles"
]