class World:
    def __init__(self):
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def update(self):
        for entity in self.entities:
            entity.update()

    def __str__(self):
        return f"World with {len(self.entities)} entities"


class Entity:
    def __init__(self, name, emotions=None):
        self.name = name
        self.emotions = emotions if emotions else {}

    def update(self):
        print(f"{self.name} is being updated")

    def perform_action(self):
        print(f"{self.name} performs an action")

    def __str__(self):
        return f"Entity(name={self.name}, emotions={self.emotions})"
