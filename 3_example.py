from scene import *
from utils import *
from animated_entity import *

import time

entity = AnimatedEntity.from_txt('square_animated.txt', 5, 3, 3)
scene = Scene(10, 10, [entity])

def entity_update(self):
    self.pos_x += 1
    if self.pos_x > scene.width + 5:
        self.pos_x = -5

entity.update_function = entity_update

while True:
    scene.update()
    output_frame(scene.draw())
    time.sleep(0.1)