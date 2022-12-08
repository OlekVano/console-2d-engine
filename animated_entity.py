import utils

from entity import Entity
from animation import Animation

class AnimatedEntity(Entity):
    def from_txt(path, width, height, duration):
        sprites = utils.sprites_from_txt(path, width, height)
        animation = Animation(width, height, sprites, duration)
        return AnimatedEntity(animation, width, height, 0, 0)