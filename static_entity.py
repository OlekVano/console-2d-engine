import utils

class StaticEntity:
    def __init__(self, sprite, width, height, pos_x, pos_y):
        self.sprite = sprite
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def from_txt(path, width, height):
        sprite = utils.sprites_from_txt(path, width, height, 1)[0]
        return StaticEntity(sprite, width, height, 0, 0)

    def draw(self, canvas):
        for i in range(self.height):
            for j in range(self.width):
                canvas[self.pos_y + i][self.pos_x + j] = self.sprite[i][j]