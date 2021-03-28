import re

def get_data(filename):
    with open('./' + filename, 'rt') as f:
        #data = [format_data(line) for line in f.read().splitlines()]
        data = format_data(f.read().splitlines())
    return data

def format_data(data):
    output = []
    mask = ''
    d = {}
    for line in data:
        if re.findall('mask = [X01]{36}', line):
            if mask:
                output.append((mask, d))
            mask = re.findall('[X01]{36}', line)[0]
            mask = format_mask(mask)
            d = {}
        else:
            key, value = re.findall('\d+', line)
            d[key] = int(value)
    output.append((mask, d))
    return output

def format_mask(mask):
    mask_dict = {}
    for i in range(len(mask)):
        char = mask[i]
        if char == '1':
            mask_dict[len(mask) - i] = 1
        elif char == '0':
            mask_dict[len(mask) - i] = 0
    return mask_dict

def part1(data):
    output = {}
    for mask, d in data:
        for key, value in d.items():
            bin_value = format(value, '#038b')
            #print(bin_value)
            for i, val in mask.items():
                #print(type(bin_value[-i]))
                if val == 1 and bin_value[-i] == '0':
                    #print('one', val, bin_value[-i])
                    value += 2**(i-1)
                elif val == 0 and bin_value[-i] == '1':
                    #print('two', val, bin_value[-i])
                    value -= 2**(i-1)
            output[key] = value
    return output

def calc_p1(output):
    sum = 0
    for value in output.values():
        sum += value
    return sum

def main():
    data = get_data('data.txt')
    #print(data)
    output = part1(data)
    #print(output)
    print(calc_p1(output))

    #print(bin(11))
    #print(int(0b1011))

    #print(format_mask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'))


main()