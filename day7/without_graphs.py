import pprint

def get_data(filename):
    with open('./' + filename, 'rt') as f:
        data_arr = [format_data(line) for line in f.read().splitlines()]
        #format this into one dictionary rather than a list of dictionaries
        data_dict = {}
        for d in data_arr:
            for key, value in d.items():
                data_dict[key] = value
    return data_dict

def format_data(line):
    outer_bag, inner_bags = line.split(' contain ')
    inner_bags = inner_bags.split(', ')
    inner_bags_dict = {}
    if inner_bags != ['no other bags.']:
        for bag in inner_bags:
            bag = bag.strip('.')
            inner_bags_dict[bag[2:-4].strip()] = int(bag[0])
    d = {outer_bag[:-4].strip(): inner_bags_dict}
    return d

bags = set() 
def find_outer_bags(data, colour):
    mapping = {colour: {}}
    for key, value in data.items():
        if colour in value.keys():
            new_key, new_value = list(find_outer_bags(data, key).items())[0]
            mapping[colour][new_key] = new_value
            bags.add(new_key)
    return mapping

def count_inner_bags(data, colour):
    pass
  
def main():
    
    pprint.pprint(get_data('test.txt'))
    print()

    data = get_data('test.txt')
    pprint.pprint(find_outer_bags(data, 'shiny gold'))
    find_outer_bags(data, 'shiny gold')
    print(len(bags))

    #print(count_inner_bags(data, 'shiny gold'))
    

main()