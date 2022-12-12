from entity import Entity
from animation_manager import AnimationManager

class ComplexEntity(Entity):
    def set_default_animation(self, name):
        self.renderer.set_default(name)

    def play_animation_once(self, name):
        self.renderer.play_once(name)

    def play_animation_looped(self, name):
        self.renderer.play_looped(name)