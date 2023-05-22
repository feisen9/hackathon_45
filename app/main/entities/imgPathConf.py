from dataclasses import dataclass

@dataclass
class imgPathConf:
    def __init__(self) -> None:
        self.config = {}

    def config(self, key, value):
        self.config[key] = value

    def get(self, key):
        return self.config[key]