import os

def sprites_from_txt(path, width, height):

    #path validation
    t = type(path)
    if t != str:
        raise TypeError(f'sprites_from_txt: path must be of type \'str\', not \'{t}\'')
    if len(path) <= 4:
        raise ValueError('sprites_from_txt: invalid path')
    if path[-4:] != '.txt':
        raise ValueError('sprites_from_txt: path must lead to a .txt file')
    if not os.path.exists(path):
        raise FileNotFoundError(f'sprites_from_txt: no such file or directory: \'{path}\'')

    #width validation
    t = type(width)
    if t != int:
        raise TypeError(f'sprites_from_txt: width must be of type \'int\', not \'{t}\'')
    if width <= 0:
        raise ValueError('sprites_from_txt: width must be a positive number')
    
    #height validation
    t = type(height) 
    if t != int:
        raise TypeError(f'sprites_from_txt: height must be of type \'int\', not \'{t}\'')
    if height <= 0:
        raise ValueError('sprites_from_txt: height must be a positive number')

    with open(path, 'r') as f:
        lines = f.readlines()
        sprites = []

        sprite_row = 0
        sprite = []
        
        for i in range(len(lines)):
            if sprite_row == -1:
                sprite_row = 0
                continue

            line = lines[i]
            sprite.append([x for x in line[:width]])
            sprite_row += 1

            if sprite_row == height:
                sprite_row = -1
                sprites.append(sprite)
                sprite = []

        return sprites

def create_frame(width, height):
    
    #width validation
    t = type(width)
    if t != int:
        raise TypeError(f'create_frame: width must be of type \'int\', not \'{t}\'')
    if width <= 0:
        raise ValueError('create_frame: width must be a positive number')
    
    #height validation
    t = type(height) 
    if t != int:
        raise TypeError(f'create_frame: height must be of type \'int\', not \'{t}\'')
    if height <= 0:
        raise ValueError('create_frame: height must be a positive number')

    return [[' ' for i in range(width)] for _ in range(height)]

def output_frame(frame):
    output = '=' * (len(frame[0]) + 2)

    for row in frame:
        output += '\n|' + ''.join(row) + '|'

    output += '\n' + '=' * (len(frame[0]) + 2)

    print(output)