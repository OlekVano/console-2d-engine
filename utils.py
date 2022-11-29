def sprites_from_txt(path, width, height, n_frames):
    with open(path, 'r') as f:
        lines = f.readlines()

        frames = []

        for n_frame in range(n_frames):
            frame = []

            for i in range(height):
                line = lines[i + n_frame * height]

                #frames.append(line[:width].split())
                frame.append([x for x in line[:width]])
            
            frames.append(frame)

        return frames

def create_frame(width, height):
    return [[' ' for i in range(width)] for _ in range(height)]

def output_frame(frame):
    output = '=' * (len(frame[0]) + 2)

    for row in frame:
        output += '\n|' + ''.join(row) + '|'

    output += '\n' + '=' * (len(frame[0]) + 2)

    print(output)