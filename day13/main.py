from functools import reduce

def get_data(filename):
    with open('./' + filename, 'rt') as f:
        start, ids = f.read().splitlines()
        start = int(start)
        ids = [int(id) if id != 'x' else id for id in ids.split(',')]
    return start, ids

def part1(data):
    start, ids = data
    ids = list(filter(lambda id : id != 'x', ids))
    time = start
    while True:
        for id in ids:
            if time % id == 0:
                print(start, time, id)
                return (time - start) * id
        time += 1

def part2(data):
    start, ids = data
    time = 0
    s = set()
    condition = False
    time = 0
    while True:
        for index in range(len(ids)):
            if ids[index] != 'x':
                if (time + index) % ids[index] == 0:
                    condition = True
                    s.add(ids[index])
                else:
                    condition = False
                    break
        if condition:
            return time
        interval = reduce(lambda a,b : a*b, s)
        time += interval

def main():
    data = get_data('data.txt')
    #print(data)
    print('Part 1:'. part1(data))
    print('Part 2:', part2(data))

main()