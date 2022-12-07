import utils

from entity import Entity
from animation import Animation

class StaticEntity(Entity):
    def from_txt(path, width, height):
        sprite = utils.sprites_from_txt(path, width, height, 1)[0]
        animation = Animation(width, height, [sprite], 0)
        return StaticEntity(animation, width, height, 0, 0)

    def draw(self, frame):
        for i in range(self.height):
            for j in range(self.width):
                sprite = self.animation.frame()
                frame[self.pos_y + i][self.pos_x + j] = sprite[i][j]