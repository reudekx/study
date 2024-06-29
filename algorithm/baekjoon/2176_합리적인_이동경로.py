from dataclasses import dataclass
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

INF = 1000 * 10000

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
        for nxt in edge[node.name]:
            if node.dist + nxt.dist >= dist[nxt.name]:
                continue
            heappush(queue, Node(nxt.name, node.dist + nxt.dist))
    return dist

def solve(s, t):
    dist = dijkstra(t)
    dp = [-1 for _ in range(n)]
    def count(cur):
        if cur == t:
            return 1
        if dp[cur] == -1:
            cnt = 0
            for nxt in edge[cur]:
                if dist[cur] <= dist[nxt.name]:
                    continue
                cnt += count(nxt.name)
            dp[cur] = cnt
        return dp[cur]
    return count(s)

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edge[a - 1].append(Node(b - 1, c))
    edge[b - 1].append(Node(a - 1, c))
print(solve(0, 1))

'''
접근:
    가까워지며 이동하기 위해서는, 경로가 이미 계산되어 있어야 한다.
    
    현재 위치 cur에서 nxt로 이동하려면,
    T에서부터 cur까지의 경로보다 T에서부터 nxt까지의 경로의 길이가 더 짧아야 한다.

    따라서 T로부터 모든 정점에 대한 최단 경로를 먼저 구해야 한다.


    또한 문제에 정점의 이름에 대한 제한이 없는데.. 일단 1부터 n까지라고 가정하자.

'''