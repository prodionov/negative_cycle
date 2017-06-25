#python2

import heapq
import sys
import itertools


class Vertex():

    def __init__(self, id, dist=float('inf')):
        self.id = id
        self.dist = dist
        self.parent = None
        #self.status = 'Not Removed'
        #self.vertex = (self.dist, [self.id, self.parent])

    @property
    def vertex(self):
        return [self.dist, self.id, self.parent]

    @property
    def dist(self):
        return dist

    @dist.setter
    def dist(self, value):
        self.dist = value

    def __str__(self):
        return str(self.id) + "  " + str(self.dist)


class Edge():

    def __init__(self, info):
        self.start = info[0]
        self.end = info[1]
        self.weight = info[2]

    def __str__(self):
        return str(self.start) + " " + str(self.end) + " " + str(self.weight)


var = sys.stdin.readline()
var = map(int, var.strip('').split(' '))

num_ver = var[0]
num_edg = var[1]
#vertex_list = set(range(1, num_ver + 1))

graph = {ver: set() for ver in range(1, num_ver + 1)}

for i in range(num_edg):
    edge = sys.stdin.readline()
    edge = list(map(int, edge.strip('').split(' ')))
    edge = Edge(edge)
    graph[edge.start].add(edge)


answer = 0

print 'graph: ', graph
vertex_set = set(range(1, num_ver + 1))
vertex_dict = {}
counter = itertools.count()



def relax(edge, iteration):
    global answer, relaxation
    if vertex_dict[edge.end].dist > vertex_dict[edge.start].dist + edge.weight:
        relaxation = True
        print "relaxing edge: ", edge
        if iteration == num_ver:
            print 'iteration equals to number of vertices'
            answer = 1
            #break
        vertex_dict[edge.end].dist = vertex_dict[edge.start].dist + edge.weight
        if edge.end in vertex_set:
            vertex_set.remove(edge.end)
        print "vertex_id: ", edge.end , " new dist: ", vertex_dict[edge.end].dist, '\n'

def bellmanFord(graph, s):
    for i in range(1, num_ver + 1):
        vertex = Vertex(i)
        vertex_dict[i] = vertex

    vertex_dict[s].dist = 0
    for i in range(1, num_ver + 1):
        print 'iteration: ', i
        relaxation = False
        print '\n nodes and distances at the start'
        for ver in vertex_dict:
            print ver, " - ", vertex_dict[ver].dist  
        print '\n'
        iteration = i
        for set_edge in graph.values():
            for edge in set_edge:
                print edge
                relax(edge, iteration)
        print "relaxation", relaxation
        if not relaxation:
            break
while vertex_set:
    s = vertex_set.pop()
    print 's - ', s
    bellmanFord(graph, s)
#for ver in vertex_dict:
#    print ver, " - ", vertex_dict[ver].dist
print 'answer: ', answer
