import time

time.time()

class Animation:
    def __init__(self, width, height, sprites, duration):
        self.width = width
        self.height = height
        self.sprites = sprites
        self.duration = duration
        self.n_sprites = len(sprites)
        self.static = self.n_sprites == 1
        self.time_elapsed = 0
        self.last_update = time.time()

    def update(self):
        if self.static: return

        current_time = time.time()
        self.time_elapsed += self.last_update - current_time
        self.last_update = current_time
        if self.time_elapsed > self.duration:
            self.time_elapsed -= self.duration
    
    def frame(self):
        if self.static: return self.sprites[0]

        return self.sprites[self.duration * self.n_sprites // self.time_elapsed]