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
    def __init__(self, name, primary_emotion):
        self.name = name
        self.primary_emotion = primary_emotion

    def update(self):
        print(f"{self.name} is being updated with primary emotion: {self.primary_emotion}")

    def perform_action(self):
        print(f"{self.name} performs an action influenced by {self.primary_emotion}")

    def __str__(self):
        return f"Entity(name={self.name}, primary_emotion={self.primary_emotion})"
