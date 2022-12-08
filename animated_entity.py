import utils

from entity import Entity
from animation import Animation

class AnimatedEntity(Entity):
    def from_txt(path, width, height, duration):
        sprites = utils.sprites_from_txt(path, width, height, 0)
        animation = Animation(width, height, sprites, duration)
        return AnimatedEntity(animation, width, height, 0, 0)

    def draw(self, frame):
        sprite = self.animation.frame()
        for i in range(self.height):
            for j in range(self.width):
                try:
                    frame[self.pos_y + i][self.pos_x + j] = sprite[i][j]
                except:
                    pass