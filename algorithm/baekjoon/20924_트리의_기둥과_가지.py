from dataclasses import dataclass
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

@dataclass
class Node:
    name: int
    dist: int

def measure(start):
    visited = [False for _ in range(n)]
    def truck(cur):
        if len(edge[cur]) > 2 - (cur == start):
            return Node(cur, 0)
        visited[cur] = True
        for nxt in edge[cur]:
            if visited[nxt.name]:
                continue
            res = truck(nxt.name)
            res.dist += nxt.dist
            return res
        return Node(cur, 0)
    def branch(cur):
        visited[cur] = True
        length = 0
        for nxt in edge[cur]:
            if visited[nxt.name]:
                continue
            length = max(length,
                branch(nxt.name) + nxt.dist
            )
        return length
    giga = truck(start)
    long = branch(giga.name)
    return giga.dist, long

n, r = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, d = map(int, input().split())
    edge[a - 1].append(Node(b - 1, d))
    edge[b - 1].append(Node(a - 1, d))

print(*measure(r - 1))