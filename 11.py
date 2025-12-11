import fileinput
import networkx as nx
import re

G = nx.DiGraph()
for line in fileinput.input():
    tokens = re.findall(r'\w+', line)
    src = tokens[0]
    for dst in tokens[1:]:
        G.add_edge(src, dst)

print(len(list(nx.all_simple_paths(G, 'you', 'out'))))

memo = {}
def count(src, dst):
    if src == dst:
        return 1
    key = (src, dst)
    if key not in memo:
        memo[key] = sum(count(x, dst) for x in G[src])
    return memo[key]

a = count('svr', 'fft') * count('fft', 'dac') * count('dac', 'out')
b = count('svr', 'dac') * count('dac', 'fft') * count('fft', 'out')
print(a + b)
