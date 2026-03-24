import math


class Logger:
    def __init__(self, name):
        self.name = name

    def info(self, message):
        self.log("INFO", message)

    def debug(self, message):
        self.log("DEBUG", message)

    def log(self, level, message):
        if level not in ["INFO", "DEBUG"]:
            raise ValueError("Level must be INFO or DEBUG")
        if not message or not message.strip():
            raise ValueError('Message must not be null or empty')
        print(f"[{level}]: {message}")


