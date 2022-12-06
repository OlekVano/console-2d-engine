import utils

from entity import Entity

class StaticEntity(Entity):
    def from_txt(path, width, height):
        sprite = utils.sprites_from_txt(path, width, height, 1)[0]
        return StaticEntity(sprite, width, height, 0, 0)

    def draw(self, frame):
        for i in range(self.height):
            for j in range(self.width):
                frame[self.pos_y + i][self.pos_x + j] = self.sprite[i][j]