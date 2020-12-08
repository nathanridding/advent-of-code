import re
import networkx as nx
import matplotlib.pyplot as plt
import pprint

def get_data(filename):
    with open('./' + filename, 'rt') as f:
        data = [format_data(line) for line in f.read().splitlines()]
    return data

def format_data(line):
    bag = re.findall('^[a-z]+ [a-z]+', line)
    contains = re.findall('(\d+) ([a-z]+ [a-z]+) bag', line)
    return [bag[0], contains]

def make_graph(data):
    G = nx.DiGraph()
    #add all nodes to the graph
    nodes = [line[0] for line in data]
    G.add_nodes_from(nodes)
    #add all edges to the graph
    for line in data:
        for pair in line[1]:
            G.add_edge(pair[1], line[0], weight=int(pair[0]))
    #print(G.nodes())
    #print(G.edges())
    return G

def part1(G, node):
    H = nx.dfs_tree(G, node)
    #print(H.nodes())
    #print(H.edges())
    return len(H)

def part2(G, node):
    output = 1
    for key, value in G.pred[node].items():
        output = output + value['weight'] * part2(G, key)
    return output

def main():
    #pprint.pprint(get_data('test.txt'))
    #print('---------------------------------')
    
    data = get_data('data.txt')
    G = make_graph(data)

    print(part1(G, 'shiny gold') - 1)
    print(part2(G, 'shiny gold') - 1)

main()