class Vulnerability:
    def __init__(self, name, lvl):
        self.name = name
        self.lv = lvl

    def __str__(self):
        return f"Vulnerability: {self.name}, LVl: {self.lvl}"

    def __eq__(self, other):
        if isinstance(other, Vulnerability):
            return self.name == other.name and self.lvl == other.lvl
        return False

    def __lt__(self, other):
        if isinstance(other, Vulnerability):
            return self.lvl < other.lvl
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Vulnerability):
            return self.lvl > other.lvl
        return NotImplemented

    def increase_rank(self, amount=1):
        self.lvl += amount

    def decrease_rank(self, amount=1):
        self.lvl -= amount
        if self.lvl < 0:
            self.lvl = 0