import re

def get_data(filename):
    with open('./' + filename, 'rt') as f:
        data = [make_dictionary(line) for line in format_data(f.read().splitlines())]
    return data

def format_data(data):
    new_data, new_line = [], ''
    for line in data:
        if line != '':
            new_line += ' ' + line
        else:
            new_data.append(new_line)
            new_line = ''
    new_data.append(new_line)
    return new_data

def make_dictionary(line):
    d = {}
    line = line.split()
    for item in line:
        (key, val) = item.split(':')
        d[key] = val
    return d

def validate_passport_p1(d):
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in required_keys:
        if key not in d.keys():
            return False
    return True

def validate_passport_p2(d):
    if not (len(d['byr']) == 4 and int(d['byr']) >= 1920 and int(d['byr']) <= 2002):
        return False
    elif not (len(d['iyr']) == 4 and int(d['iyr']) >= 2010 and int(d['iyr']) <= 2020):
        return False
    elif not (len(d['eyr']) == 4 and int(d['eyr']) >= 2020 and int(d['eyr']) <= 2030):
        return False
    elif not ((d['hgt'][-2:] == 'cm' and int(d['hgt'][:-2]) >= 150 and int(d['hgt'][:-2]) <= 193) or (d['hgt'][-2:] == 'in' and int(d['hgt'][:-2]) >= 59 and int(d['hgt'][:-2]) <= 76)):
        return False
    elif not re.search('^#[0-9a-f]{6}$', d['hcl']):
        return False
    elif d['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    elif not re.search('^[0-9]{9}$', d['pid']):
        return False
    else:
        return True
    

def main():
    #print(get_data('test.txt'))
    data = get_data('data.txt')

    arr1 = list(filter(validate_passport_p1, data))
    arr2 = list(filter(validate_passport_p2, arr1))
    
    print(len(arr1))
    print(len(arr2))

    
main()