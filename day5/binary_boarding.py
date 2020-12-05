def get_data(filename):
    with open('./' + filename, 'rt') as f:
        data = f.read().splitlines()
    return data

def calculate_id(str):
    #find row
    lst = list(range(128))
    for l in str[:7]:
        if l == 'F':
            lst = lst[:len(lst)//2]
        elif l == 'B':
            lst = lst[len(lst)//2:]
    row = lst[0]
    #find column
    lst = list(range(8))
    for l in str[7:]:
        if l == 'L':
            lst = lst[:len(lst)//2]
        elif l == 'R':
            lst = lst[len(lst)//2:]
    col = lst[0]
    #return seat id
    return row * 8 + col

def find_max_id(data):
    return max([calculate_id(str) for str in data])

def find_my_seat(data):
    ids = [calculate_id(str) for str in data]
    for id in ids:
        if id + 1 not in ids and id != find_max_id(data):
            return id + 1

def main():
    data = get_data('data.txt')
    print(find_max_id(data))
    print(find_my_seat(data))

main()