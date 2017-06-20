# python2

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

graph = {ver: set() for ver in range(1, num_ver + 1)}

for i in range(num_edg):
    edge = sys.stdin.readline()
    edge = list(map(int, edge.strip('').split(' ')))
    edge = Edge(edge)
    graph[edge.start].add(edge)

print 'graph: ', graph
vertex_dict = {}


def relax(edge):
    if vertex_dict[edge.start].dist > vertex_dict[edge.end].dist + edge.weight:
        vertex_dict[edge.start].dist = vertex_dict[edge.end].dist + edge.weight


def bellmanFord(graph):
    for i in range(1, num_ver + 1):
        vertex = Vertex(i)
        vertex_dict[i] = vertex

    for i in range(1, num_ver + 1):
        vertex_dict[i].dist = 0
        for set_edge in graph.values():
            for edge in set_edge:
                print edge
                relax(edge)


bellmanFord(graph)
for ver in vertex_dict:
    print ver, " - ", vertex_dict[ver].dist
