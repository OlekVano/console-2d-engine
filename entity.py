class Entity:
    def __init__(self, animation, width, height, pos_x, pos_y):
        self.animation = animation
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def update_function(*args):
        pass

    def update(self):
        self.animation.update()
        self.update_function(self)

    def draw(self, frame):
        sprite = self.animation.frame()
        for y in range(self.height):
            for x in range(self.width):
                frame_pos_y = self.pos_y + y
                frame_pos_x = self.pos_x + x

                if frame_pos_y >= 0 and frame_pos_y < len(frame) and frame_pos_x >= 0 and frame_pos_x < len(frame[0]):
                    frame[frame_pos_y][frame_pos_x] = sprite[y][x]