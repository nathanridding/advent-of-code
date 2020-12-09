def get_data(filename):
    with open('./' + filename, 'rt') as f:
        data = [int(line) for line in f.read().splitlines()]
    return data

def is_sum_of_2(lst, num):
    for x in lst:
        for y in lst:
            if x + y == num and lst.index(x) != lst.index(y):
                return True
    return False

def find_invalid_p1(data, preamble):
    i = 0
    to_check = data
    while to_check != []:
        checked = data[i : preamble + i]
        to_check = data[preamble + i : ]
        if not is_sum_of_2(checked, to_check[0]):
            return to_check[0]
        else:
            i += 1
    return 'all numbers pass check'

def find_weakness_p2(data, num):
    for i in range(len(data)):
        sum = 0
        t = 0
        while sum < num:
            sum += data[i + t]
            if sum == num:
                return data[i : i + t + 1]
            t += 1

def main():
    #print(get_data('test.txt'))
    data = get_data('data.txt')
    num = find_invalid_p1(data, 25)
    arr = find_weakness_p2(data, num)
    print(num)
    #print(arr)
    print(min(arr) + max(arr))

main()