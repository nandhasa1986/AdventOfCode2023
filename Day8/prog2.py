import re
from collections import namedtuple
import itertools as it
from math import lcm

inputfp = open('input.txt', 'r')

nLR = namedtuple("Name", "L R")
nodes = {}
instruction = ""

s1 = inputfp.readline().strip()
instruction = s1
s1 = inputfp.readline().strip() # empty line

while True:
    s1 = inputfp.readline().strip()
    if not s1:
       break
    node = s1.split("=")
    nodeNAME = node[0].strip()
    nodePATHS = node[1].strip().replace("(", "").replace(")", "").split(",")
    nodePATHSL = nodePATHS[0].strip()
    nodePATHSR = nodePATHS[1].strip()
    print(nodeNAME + " " + nodePATHSL + " " + nodePATHSR)

    nodes[nodeNAME] = nLR(nodePATHSL, nodePATHSR)

def get_path_values(node, endswith):
    steps = 0
    for direction in it.cycle(instruction.strip()):
        steps += 1
        if direction == 'L':
            next_node = nodes[node].L
        else:
            next_node = nodes[node].R

        node = next_node
        if node.endswith('Z'):
            return steps

start_nodes = []
path_values = []
for node in nodes:
    if node.endswith('A'):
        start_nodes.append(node)

for node in start_nodes:
    path_values.append(get_path_values(node=node, endswith='Z'))

print(lcm(*path_values))

print("- - - - - - - - - - - - - - - - - - - - - - -")
