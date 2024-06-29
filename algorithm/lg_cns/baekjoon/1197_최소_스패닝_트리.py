from dataclasses import dataclass
from heapq import heappush, heappop

import sys

input = sys.stdin.readline

def kruskal():

    @dataclass
    class Edge:
        v1: int
        v2: int
        cost: int

    def find(x):
        if parent[x] != x:
            return find(parent[x])
        return x
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    v, e = map(int, input().split())
    edges = [Edge(*map(int, input().split())) for _ in range(e)]
    edges.sort(key=lambda x: x.cost)

    parent = [i for i in range(v + 1)]

    weight = 0
    cnt = 0
    for edge in edges:
        if find(edge.v1) == find(edge.v2):
            continue
        
        union(edge.v1, edge.v2)
        weight += edge.cost

        if cnt == v - 1:
            break
    
    return weight

def prim():

    @dataclass
    class Node:
        name: int
        cost: int

        def __lt__(self, other):
            return self.cost < other.cost

    v, e = map(int, input().split())
    edge = [[] for _ in range(v + 1)]
    for _ in range(e):
        v1, v2, cost = map(int, input().split())
        edge[v1].append(Node(v2, cost))
        edge[v2].append(Node(v1, cost))

    cnt = -1
    weight = 0
    selected = [False for _ in range(v + 1)]
    heap = [Node(1, 0)]
    while heap:
        cur: Node = heappop(heap)
        if selected[cur.name]:
            continue
        selected[cur.name] = True
        weight += cur.cost
        cnt += 1
        if cnt == v - 1:
            break
        for nxt in edge[cur.name]:
            if selected[nxt.name]:
                continue
            heappush(heap, nxt)

    return weight

print(prim())

'''
시작시간: 11:30
종료시간: 실패

접근:
    가중치의 합이 최소인 트리를 찾아야 한다. -> 그리고 그 가중치의 값을 구해야 함.

    DFS로 돌면 되나 싶은데.. 시간복잡도 우려가? 
    일단 트리니까 V - 1 개의 간선을 가진다.

    
후기:
    감이 안 잡혀서 답을 참고했다.
    군대 가기 전에 배웠던 MST(MST = 최소 신장 트리. 
    참고로 신장 트리란 모든 정점이 그래프 상에서 모든 노드가 사이클 없이 연결된 부분 그래프를 뜻한다.)
    알고리즘을 사용해서 풀 수 있다.

    먼저 크루스칼 알고리즘:
        간선을 가중치가 낮은 순서대로 정렬한 뒤, 하나씩 추가하면 된다.
        물론 이 과정에서 사이클이 생성되면 안 된다.
        사이클의 생성 여부는 유니온 파인드를 통해 확인하면 된다.

        알고리즘의 종료 시점은 V - 1 개의 간선을 선택했을 때.

    다음으로, 프림 알고리즘:
        
        무작위 노드를 하나 선택하여 트리에 포함시키고, 연결된 간선들 중 가중치가 제일 낮은 것을 골라서
        해당 노드를 트리에 포함시킨다. 이를 반복.

        Node 클래스를 작성했는데, 
        그냥 tuple을 이용하고 unpacking에서 데이터를 다뤄도 될 듯.
        
'''