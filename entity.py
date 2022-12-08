class Entity:
    def __init__(self, animation, width, height, pos_x, pos_y):
        self.animation = animation
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def update_function(self):
        pass

    def update(self):
        self.animation.update()
        self.update_function(self)