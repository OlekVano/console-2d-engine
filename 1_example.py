from scene import *
from utils import *
from static_entity import *

entity = StaticEntity.from_txt('square.txt', 5, 3)
scene = Scene(10, 10, [entity])
output_frame(scene.draw())