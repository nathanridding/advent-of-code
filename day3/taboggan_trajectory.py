def get_data(filename):
    with open('./' + filename, 'rt') as f:
        data = f.read().splitlines()
    return data

def count_trees(data, right, down):
    x, y = 0, 0
    rows, cols = len(data), len(data[0])
    trees = 0
    while y < rows:
        if data[y][x] == '#':
            trees += 1
        x = (x + right) % cols
        y += down
    return trees

def multiply_slopes(data):
    return count_trees(data, 1, 1) * count_trees(data, 3, 1) * count_trees(data, 5, 1) * count_trees(data, 7, 1) * count_trees(data, 1, 2)
    
def main():
    #print(get_data('test.txt'))
    data = get_data('data.txt')
    print(count_trees(data, 3, 1))
    print(multiply_slopes(data))

main()