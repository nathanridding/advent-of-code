def get_data(filename):
    with open('./' + filename, 'rt') as f:
        data = [line.split() for line in f.read().splitlines()]
    return data

def find_acc(data):
    acc, i, visited = 0, 0, []
    while i not in visited:
        if i == len(data):
            return 'end', acc
        visited.append(i)
        if data[i][0] == 'nop':
            i += 1
        elif data[i][0] == 'acc':
            acc += int(data[i][1])
            i += 1
        elif data[i][0] == 'jmp':
            i += int(data[i][1])
    return 'loop', acc

def find_value_to_change(data):
    for i in range(len(data)):
        if data[i][0] == 'nop':
            data[i][0] = 'jmp'
            word, acc = find_acc(data)
            if word == 'end':
                return i, acc
            else:
                data[i][0] = 'nop'
        elif data[i][0] == 'jmp':
            data[i][0] = 'nop'
            word, acc = find_acc(data)
            if word == 'end':
                return i, acc
            else:
                data[i][0] = 'jmp'
    return 'no match found'
            
def main():
    #print(get_data('test.txt'))
    data = get_data('data.txt')
    print(find_acc(data))
    print(find_value_to_change(data))

main()