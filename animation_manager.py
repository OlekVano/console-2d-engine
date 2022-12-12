class AnimationManager:
    def __init__(self, animations={}, default=None):
        self.animations = animations
        self.default = default
        self.current = self.default
        self.loop = False

    def add(self, name, animation):
        self.animations[name] = animation
    
    def set_default(self, name):
        self.default = name
        self.current = self.default
    
    def play_once(self, name):
        self.current = name
        self.loop = False
    
    def play_looped(self, name):
        self.current = name
        self.loop = True