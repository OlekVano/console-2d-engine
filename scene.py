import utils

class Scene:
    def __init__(self, width, height, entities=[]):
        self.width = width
        self.height = height
        self.entities = entities

    def draw(self):
        frame = utils.create_frame(self.width, self.height)

        for entity in self.entities:
            entity.draw(frame)

        return frame

    def update(self):
        for entity in self.entities:
            entity.update()