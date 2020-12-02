def get_data(filename):
    with open('/home/nathan/adventofcode20/day2/' + filename, 'rt') as f:
        data = [line.split() for line in f.read().splitlines()]
    #format the data as a dictionary so that is easier to use
    newData = []
    for j in range(len(data)):
        d = {}
        d['nums'] = [int(n) for n in [i[0].split('-') for i in data][j]]
        d['char'] = [i[1][0] for i in data][j]
        d['password'] = [i[2] for i in data][j]
        newData.append(d)
    return newData

def check_passwords1(data):
    valid_passwords = 0
    for d in data:
        #count how many times the required charcter appears in the password
        count = d['password'].count(d['char'])
        #check if it is in the required range
        if count >= d['nums'][0] and count <= d['nums'][1]:
            valid_passwords += 1
    return valid_passwords

def check_passwords2(data):
    valid_passwords = 0
    for d in data:
        #array with just the characters in the relevent positions
        relevent_letters = [d['password'][d['nums'][0] - 1], d['password'][d['nums'][1] - 1]]
        #check the required character appears exactly once in this array
        if relevent_letters.count(d['char']) == 1:
            valid_passwords += 1
    return valid_passwords

def main():
    print(get_data('test_data.txt'))
    data = get_data('data.txt')
    print(check_passwords1(data))
    print(check_passwords2(data))

main()