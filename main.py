from static_entity import StaticObject

x = StaticObject.from_txt('square.txt', 5, 3)
canvas = [
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
]
x.pos_x = 1
x.pos_y = 1
x.draw(canvas)
print(canvas)