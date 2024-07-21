import numpy as np

# Turning the input into a np array
map = list()
fhand = open('input.txt')
for lines in fhand:
    line = lines.split()
    for i in line:
        row = list()
        for n in i:
            row.append(n)
        map.append(row)

np_map = np.array(map)

# '|', '-', 'L', 'J', 'F', '7', '.', 'S'

def check(old, new, direction):
    cheat_sheet = {'up':{'|':('|', 'F', '7'), 
                         '-':(),
                         'L':('|', 'F', '7'),
                         'J':('|', 'F', '7'),
                         'F':(),
                         '7':(),
                         '.':(),
                         'S':('|', 'F', '7')},
                    'down':{'|':('|', 'L', 'J'), 
                            '-':(),
                            'L':(),
                            'J':(),
                            'F':('|', 'L', 'J'),
                            '7':('|', 'L', 'J'),
                            '.':(),
                            'S':()},
                    'left':{'|':(), 
                            '-':('-', 'L', 'F'),
                            'L':(),
                            'J':('-', 'L', 'F'),
                            'F':(),
                            '7':('-', 'L', 'F'),
                            '.':(),
                            'S':('-', 'L', 'F')},
                    'right':{'|':(), 
                            '-':('-', '7', 'J'),
                            'L':('-', '7', 'J', 'S'),
                            'J':(),
                            'F':('-', '7', 'J'),
                            '7':(),
                            '.':(),
                            'S':()},
                    }
    result = new in cheat_sheet[direction][old]
    return result

symbol = 'S'
old_coord = []
current_coord = [54, 15]
count = 0
journey = list()

while symbol != 'S' or count == 0:
    # Checking for upwards
    if check(symbol, np_map[current_coord[0]-1, current_coord[1]], 'up') == True and [current_coord[0]-1, current_coord[1]] != old_coord:
        count += 1
        symbol = np_map[current_coord[0]-1, current_coord[1]]
        old_coord = [current_coord[0], current_coord[1]]
        current_coord = [current_coord[0]-1, current_coord[1]]
        journey.append(np_map[current_coord[0], current_coord[1]])
        print('up')

    # Checking for downwards
    elif check(symbol, np_map[current_coord[0]+1, current_coord[1]], 'down') == True and [current_coord[0]+1, current_coord[1]] != old_coord:
        count += 1
        symbol = np_map[current_coord[0]+1, current_coord[1]]
        old_coord = [current_coord[0], current_coord[1]]
        current_coord = [current_coord[0]+1, current_coord[1]]
        journey.append(np_map[old_coord])
        print('down')

    # Checking for leftwards
    elif check(symbol, np_map[current_coord[0], current_coord[1]-1], 'left') == True and [current_coord[0], current_coord[1]-1] != old_coord:
        count += 1
        symbol = np_map[current_coord[0], current_coord[1]-1]
        old_coord = [current_coord[0], current_coord[1]]
        current_coord = [current_coord[0], current_coord[1]-1]
        journey.append(np_map[old_coord])
        print('left')

    # Checking for rightwards
    elif check(symbol, np_map[current_coord[0], current_coord[1]+1], 'right') == True and [current_coord[0], current_coord[1]+1] != old_coord:
        count += 1
        symbol = np_map[current_coord[0], current_coord[1]+1]
        old_coord = [current_coord[0], current_coord[1]]
        current_coord = [current_coord[0], current_coord[1]+1]
        journey.append(np_map[old_coord])
        print('right')

    else:
        continue

print(count)
print(count/2)








