def get_data(filename):
    with open('./' + filename, 'rt') as f:
        data = [group.split() for group in f.read().split('\n\n')]
    return data

def count_questions_p1(data):
    sum = 0
    for group in data:
        unique_qs = []
        for line in group:
            for letter in line:
                if letter not in unique_qs:
                    unique_qs.append(letter)
        sum += len(unique_qs)
    return sum

def count_questions_p2(data):
    sum = 0
    for group in data:
        people = len(group)
        s = ''
        for line in group:
            s += line
        for letter in s:
            if s.count(letter) == people:
                sum += 1 / people
    return sum

def main():
    #print(get_data('test.txt'))
    data = get_data('data.txt')
    print(count_questions_p1(data))
    print(count_questions_p2(data))

main()