from dataclasses import dataclass
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

INF = 100000 * 10000

@dataclass
class Node:
    name: int
    dist: int

    def __lt__(self, obj):
        return self.dist < obj.dist

def dijkstra(start):
    dist = [INF for _ in range(n)]
    queue = [Node(start, 0)]
    while queue:
        node = heappop(queue)
        if node.dist >= dist[node.name]:
            continue
        dist[node.name] = node.dist
        for next in edge[node.name]:
            if node.dist + next.dist >= dist[next.name]:
                continue
            heappush(queue, Node(next.name, node.dist + next.dist))
    return dist

def solve():
    dists = [
        dijkstra(a - 1),
        dijkstra(b - 1),
        dijkstra(c - 1)
    ]
    res = Node(-1, 0)
    for i in range(n):
        dist = min(dists[k][i] for k in range(3))
        if res.dist < dist:
            res.name = i
            res.dist = dist
    return res.name + 1

n = int(input())
a, b, c = map(int, input().split())
m = int(input())
edge = [[] for _ in range(n)]
for _ in range(m):
    d, e, l = map(int, input().split())
    edge[d - 1].append(Node(e - 1, l))
    edge[e - 1].append(Node(d - 1, l))

print(solve())