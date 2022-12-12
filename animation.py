import time

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

        self.time_elapsed += current_time - self.last_update
        self.last_update = current_time

        if self.time_elapsed > self.duration:
            self.time_elapsed -= self.duration
    
    def render(self):
        if self.static: return self.sprites[0]

        n_sprite = int(self.time_elapsed * self.n_sprites / self.duration)

        return self.sprites[n_sprite]