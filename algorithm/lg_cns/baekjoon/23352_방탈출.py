from collections import deque

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]


def bfs(x, y):
    visited = [[False for _ in range(m)] for _ in range(n)]
    max_length = 0
    max_sum = 0
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True
    while queue:
        cx, cy, cd = queue.popleft()
        if cd >= max_length:
            csum = board[cx][cy] + board[x][y]
            if cd > max_length:
                max_sum = csum
            elif cd == max_length:
                max_sum = max(max_sum, csum)
            max_length = cd
        for dx, dy in dirs:
            nx = cx + dx
            ny = cy + dy
            if not (nx >= 0 and nx < n and ny >= 0 and ny < m):
                continue
            if visited[nx][ny] or board[nx][ny] == 0:
                continue
            visited[nx][ny] = True
            nd = cd + 1
            queue.append((nx, ny, nd))
    return max_length, max_sum


def solve():
    max_length = 0
    max_sum = 0
    for x in range(n):
        for y in range(m):
            if board[x][y] == 0:
                continue
            length, sum = bfs(x, y)
            # print(f"b[{x}][{y}] = {board[x][y]}, length = {length}, sum = {sum}, max_length = {max_length}, max_sum = {max_sum}")
            if length >= max_length:
                if length > max_length:
                    max_sum = sum
                elif length == max_length:
                    max_sum = max(max_sum, sum)
                max_length = length
    return max_sum





n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(solve())

'''
시작 시간: 22:13
종료 시간: 22:51

접근:
    문제 해석)
        임의의 시작/종료 지점을 골랐을 때 해당 지점 간의 최단 경로를 구하는데,
        이때 경로가 가장 길어지도록 지점을 선택해야 함. 또한 시작 = 종료 지점일 수 있다.

        시작 지점을 하나 고르고, 거기서 최단 경로를 구하자. BFS로 구하면 될 듯.

        2500 * 2500의 시간복잡도

후기:
    BFS로 최단 경로를 구하면 되는데, 다익스트라, A* 알고리즘 등이 먼저 떠올라서 시간을 지체해버렸다.

    또한 디버깅을 하는데 오래 걸렸다.

    먼저 max 길이와 현재 길이가 같을 때는 max(max_sum, sum)을 구해야 하고, 
    현재 길이가 더 길 때는 그냥 max_sum을 sum으로 덮어씌워 줘야 했다.

    또한 보드의 값이 0인 지점은 BFS 도중 건너가도 안 되지만, solve 지점에서 시작도 하면 안 되었었다.

    실수를 줄여야 할 듯

'''