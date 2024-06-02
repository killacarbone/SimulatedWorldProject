class World:
    def __init__(self):
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def update(self):
        for entity in self.entities:
            entity.update()

    def propose_change(self, proposal):
        votes = [entity.vote(proposal) for entity in self.entities]
        if votes.count(True) > votes.count(False):
            print(f"Proposal '{proposal}' approved by the council of gods.")
        else:
            print(f"Proposal '{proposal}' rejected by the council of gods.")

    def __str__(self):
        return f"World with {len(self.entities)} entities"


class Entity:
    def __init__(self, name, emotion):
        self.name = name
        self.emotion = emotion

    def update(self):
        print(f"{self.name} is being updated with emotion: {self.emotion}")

    def perform_action(self):
        print(f"{self.name} performs an action influenced by {self.emotion}")

    def vote(self, proposal):
        if self.emotion == "Neutrality":
            return True  # Neutrality god always votes to pass proposals
        elif self.emotion == "Love" and "love" in proposal:
            return True
        elif self.emotion == "Hate" and "hate" in proposal:
            return True
        else:
            return False

    def __str__(self):
        return f"Entity(name={self.name}, emotion={self.emotion})"
