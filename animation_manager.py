class AnimationManager:
    def __init__(self):
        self.animations = {}
        self.default = None
        self.current = None
        self.loop = True

    def add(self, name, animation):
        self.animations[name] = animation
    
    def set_default(self, name):
        self.default = name
    
    def playOnce(self, name):
        self.current = name
        self.loop = False
    
    def play(self, name):
        self.current = name
        self.loop = True