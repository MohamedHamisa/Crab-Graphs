

import math
import os
import random
import re
import sys

def crabGraphs(n, t, graph):
    cnn={x:[] for x in range(1,n+1)}
    for u,v in graph:
        cnn[u].append(v)
        cnn[v].append(u)
    nodes=set()
    for u in sorted(cnn, key=lambda s:len(cnn[s]),reverse=True):
        if u not in nodes and len(cnn[u])>=t:
            nodes.add(u)
    for u in sorted(cnn, key=lambda s:len(cnn[s]),reverse=True):
        feet_of_u=0
        for v in cnn[u]:
            if v not in nodes and feet_of_u<t:
                nodes.add(v)
                feet_of_u+=1
    return len(nodes)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    c = int(input().strip())

    for c_itr in range(c):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        t = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        graph = []

        for _ in range(m):
            graph.append(list(map(int, input().rstrip().split())))

        result = crabGraphs(n, t, graph)

        fptr.write(str(result) + '\n')

    fptr.close()
