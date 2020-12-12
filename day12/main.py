def get_data(filename):
    with open('./' + filename, 'rt') as f:
        data = [format_data(line) for line in f.read().splitlines()]
    return data

def format_data(line):
    letter = line[0]
    number = int(line[1:])
    return letter, number

def apply_move_p1(line, pos, dir):
    letter, number = line
    x, y = pos
    if letter == 'N':
        y += number
    elif letter == 'S':
        y -= number
    elif letter == 'E':
        x += number
    elif letter == 'W':
        x -= number
    elif letter == 'L':
        dir = (dir + number) % 360
    elif letter == 'R':
        dir = (dir - number) % 360
    elif letter == 'F':
        if dir == 90:
            y += number
        elif dir == 270:
            y -= number
        elif dir == 0:
            x += number
        elif dir == 180:
            x -= number
    pos = (x, y)
    return pos, dir

def part1(data):
    pos = (0, 0)
    dir = 0
    for line in data:
        pos, dir = apply_move_p1(line, pos, dir)
        #print(pos, dir)
    return pos, dir

def apply_move_p2(line, ship_pos, wp_pos):
    letter, number = line
    x1, y1 = ship_pos
    x2, y2 = wp_pos
    if letter == 'N':
        y2 += number
    elif letter == 'S':
        y2 -= number
    elif letter == 'E':
        x2 += number
    elif letter == 'W':
        x2 -= number
    elif letter == 'L':
        #waypoint's relative position to ship
        x, y = (x2 - x1, y2 - y1)
        if number == 90:
            x2 = x1 - y
            y2 = y1 + x
        elif number == 180:
            x2 = x1 - x
            y2 = y1 - y
        elif number == 270:
            x2 = x1 + y
            y2 = y1 - x
    elif letter == 'R':
        #waypoint's relative position to ship
        x, y = (x2 - x1, y2 - y1)
        if number == 90:
            x2 = x1 + y
            y2 = y1 - x
        elif number == 180:
            x2 = x1 - x
            y2 = y1 - y
        elif number == 270:
            x2 = x1 - y
            y2 = y1 + x
    elif letter == 'F':
        #waypoint's relative position to ship
        x, y = (x2 - x1, y2 - y1)
        x1 += x * number
        x2 += x * number
        y1 += y * number
        y2 += y * number
    ship_pos = (x1, y1)
    wp_pos = (x2, y2)
    return ship_pos, wp_pos
    
def part2(data):
    ship_pos = (0, 0)
    wp_pos = (10, 1)
    for line in data:
        ship_pos, wp_pos = apply_move_p2(line, ship_pos, wp_pos)
        #print(ship_pos, wp_pos)
    return ship_pos, wp_pos  

def main():
    data = get_data('data.txt')
    #print(data)
    print(part1(data)[0])
    print(part2(data)[0])

main()