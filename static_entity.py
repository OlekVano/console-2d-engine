import utils

from entity import Entity
from animation import Animation

class StaticEntity(Entity):
    def from_txt(path, width, height):
        sprite = utils.sprites_from_txt(path, width, height)[0]
        animation = Animation(width, height, [sprite], 0)
        return StaticEntity(animation, width, height, 0, 0)