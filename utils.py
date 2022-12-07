def sprites_from_txt(path, width, height, n_frames):
    with open(path, 'r') as f:
        lines = f.readlines()
        sprites = []

        sprite_row = 0
        sprite = []
        
        for i in range(len(lines)):
            if sprite_row == height:
                sprite_row = 0
                sprites.append(sprite)
                sprite = []
            else:
                line = lines[i]
                sprite.append([x for x in line[:width]])
                sprite_row += 1

        return sprites

def create_frame(width, height):
    return [[' ' for i in range(width)] for _ in range(height)]

def output_frame(frame):
    output = '=' * (len(frame[0]) + 2)

    for row in frame:
        output += '\n|' + ''.join(row) + '|'

    output += '\n' + '=' * (len(frame[0]) + 2)

    print(output)