with open('/home/nathan/python-advent-exercises/day1/data.txt') as f:
    data = f.read().splitlines()

#print(data)
test = ['444', '1721', '979', '366', '299', '675', '1456']

def find2nums(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if int(data[i]) + int(data[j]) == 2020:
                return int(data[i]) * int(data[j])

print(find2nums(data))

def find3nums(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                if int(data[i]) + int(data[j]) + int(data[k]) == 2020:
                    return int(data[i]) * int(data[j]) * int(data[k])

print(find3nums(data))
        
        