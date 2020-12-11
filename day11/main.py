from pprint import pprint
from copy import deepcopy

def get_data(filename):
    with open('./' + filename, 'rt') as f:
        data = [[seat for seat in line] for line in f.read().splitlines()]
    return data
    
def find_adjacent_p1(data, i, j):
    adjacent = []
    #add top row
    if i-1 >= 0:
        adjacent.append(data[i-1][j])
        if j-1 >= 0:
            adjacent.append(data[i-1][j-1])
        if j+1 < len(data[i]):
            adjacent.append(data[i-1][j+1])
    #add middle row
    if j-1 >= 0:
        adjacent.append(data[i][j-1])
    if j+1 < len(data[i]):
        adjacent.append(data[i][j+1])
    #add bottom row
    if i+1 < len(data):
        adjacent.append(data[i+1][j])
        if j-1 >= 0:
            adjacent.append(data[i+1][j-1])
        if j+1 < len(data[i]):
            adjacent.append(data[i+1][j+1])
    return adjacent

def apply_change_p1(data):
    new_data = deepcopy(data)
    changes_made = False
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '.':
                adjacent = find_adjacent_p1(data, i, j)
            if data[i][j] == 'L' and adjacent.count('#') == 0:
                new_data[i][j] = '#'
                changes_made = True
            if data[i][j] == '#' and adjacent.count('#') >= 4:
                new_data[i][j] = 'L'
                changes_made = True
    return new_data, changes_made

def part1(data):
    changes_made = True
    while changes_made:
        data, changes_made = apply_change_p1(data)
    occupied = sum([line.count('#') for line in data])
    return occupied

def find_visible_p2(data, i, j):
    visible = []
    #north
    d = 1
    while i-d >= 0:
        if data[i-d][j] == 'L':
            visible.append('L')
            break
        elif data[i-d][j] == '#':
            visible.append('#')
            break
        d += 1
    #south
    d = 1
    while i+d < len(data):
        if data[i+d][j] == 'L':
            visible.append('L')
            break
        elif data[i+d][j] == '#':
            visible.append('#')
            break
        d += 1
    #west
    d = 1
    while j-d >= 0:
        if data[i][j-d] == 'L':
            visible.append('L')
            break
        elif data[i][j-d] == '#':
            visible.append('#')
            break
        d += 1
    #east
    d = 1
    while j+d < len(data[i]):
        if data[i][j+d] == 'L':
            visible.append('L')
            break
        elif data[i][j+d] == '#':
            visible.append('#')
            break
        d += 1
    #south-east
    d = 1
    while i+d < len(data) and j+d < len(data[i]):
        if data[i+d][j+d] == 'L':
            visible.append('L')
            break
        elif data[i+d][j+d] == '#':
            visible.append('#')
            break
        d += 1
    #south-west
    d = 1
    while i+d < len(data) and j-d >= 0:
        if data[i+d][j-d] == 'L':
            visible.append('L')
            break
        elif data[i+d][j-d] == '#':
            visible.append('#')
            break
        d += 1
    #south-east
    d = 1
    while i-d >= 0 and j+d < len(data[i]):
        if data[i-d][j+d] == 'L':
            visible.append('L')
            break
        elif data[i-d][j+d] == '#':
            visible.append('#')
            break
        d += 1
    #north-west
    d = 1
    while i-d >= 0 and j-d >= 0:
        if data[i-d][j-d] == 'L':
            visible.append('L')
            break
        elif data[i-d][j-d] == '#':
            visible.append('#')
            break
        d += 1
    return visible

def apply_change_p2(data):
    new_data = deepcopy(data)
    changes_made = False
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '.':
                visible = find_visible_p2(data, i, j)
            if data[i][j] == 'L' and visible.count('#') == 0:
                new_data[i][j] = '#'
                changes_made = True
            if data[i][j] == '#' and visible.count('#') >= 5:
                new_data[i][j] = 'L'
                changes_made = True
    return new_data, changes_made
    
def part2(data):
    changes_made = True
    while changes_made:
        data, changes_made = apply_change_p2(data)
    occupied = sum([line.count('#') for line in data])
    return occupied

def main():
    data = get_data('data.txt')
    #pprint(data)
    #pprint(apply_change_p1(data)[0])
    print(part1(data))
    print(part2(data))
    #print(find_visible(data, 2, 7))

main()