import re
from collections import namedtuple
import itertools as it
#import networkx as nx
#from networkx import Graph

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
    print("nodePATHS " + str(nodePATHS))
    nodePATHSL = nodePATHS[0].strip()
    nodePATHSR = nodePATHS[1].strip()
    print(nodeNAME + " " + nodePATHSL + " " + nodePATHSR)

    nodes[nodeNAME] = nLR(nodePATHSL, nodePATHSR)

def print_number_of_steps(start, end):
    steps = 0
    node = start

    for direction_ in it.cycle(instruction.strip()):
        steps += 1
        if direction_ == 'L':
            node_next = nodes[node].L
        else:
            node_next = nodes[node].R

        node = node_next 
        if node == end:
            return steps 

print(print_number_of_steps(start="AAA", end="ZZZ"));
print("- - - - - - - - - - - - - - - - - - - - - - -")
