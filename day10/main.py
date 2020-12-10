def get_data(filename):
    with open('./' + filename, 'rt') as f:
        data = [int(line) for line in f.read().splitlines()]
        data.sort()
    return data

#part 1
def count_diffs(data):
    jolt = 0
    differences = {1:0, 2:0, 3:1}
    for n in data:
        diff = n - jolt
        jolt = n
        if diff <= 3:
            differences[diff] += 1
        else:
            print('diff too high', n)
    return differences[1] * differences[3]

#find ranges of consecutive numebrs in an list
def ranges(nums):
    gaps = [[start, end] for start, end in zip(nums, nums[1:]) if start + 1 < end]
    edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
    return list(zip(edges, edges))

#calculate the corresponding tribonacci number
def trib(n):
    t = [1, 2, 4]
    if n < 3:
        return t[n]
    else:
        return trib(n-3) + trib(n-2) + trib(n-1)

#calculate answer for part 2
def calc_possible_chains(ranges):
    output = 1
    #d = {1: 2, 2: 4, 3: 7, 4: 13}
    for start, end in ranges:
        n = end - start - 1
        if n > 0:
            output *= trib(n)
    return output

def main():
    data = get_data('data.txt')
    #print(data)
    print(count_diffs(data))

    #print(4 * 4**10 * 7**7)

    ranges_list = ranges([0, *data])
    print(ranges_list)
    print(calc_possible_chains(ranges_list))

    print(trib(5))
    print([trib(i) for i in range(10)])

main()