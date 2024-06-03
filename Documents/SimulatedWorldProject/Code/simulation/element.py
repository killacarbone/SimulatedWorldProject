class Element:
    def __init__(self, name, symbol, atomic_number, reactivity, stability):
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.reactivity = reactivity
        self.stability = stability

    def __str__(self):
        return f"{self.name} ({self.symbol}), Atomic Number: {self.atomic_number}, Reactivity: {self.reactivity}, Stability: {self.stability}"
