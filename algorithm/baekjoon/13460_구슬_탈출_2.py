# global WALL, EMPTY, HOLE, BLUE, RED

WALL = '#'
EMPTY = '.'
HOLE = 'O'
BLUE = 'B'
RED = 'R'

DIRS = (
    (0, 1), (1, 0), (0, -1), (-1, 0)
)

FAIL = 0
SUCCESS = 1
CONTINUE = 2

def is_in_bound(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def move(x, y, bx, by, rx, ry, dx, dy):
    while is_in_bound(x + dx, y + dy):
        nx, ny = x + dx, y + dy
        if (nx, ny) in ((bx, by), (rx, ry)):
            return x, y
        if board[nx][ny] == WALL:
            return x, y
        if board[nx][ny] == HOLE:
            return -1, -1
        x, y = nx, ny
    return x, y

def tilt(bx, by, rx, ry, dx, dy):
    if dx > 0:
        if bx > rx:
            nbx, nby = move(bx, by, bx, by, rx, ry, dx, dy)
            nrx, nry = move(rx, ry, nbx, nby, rx, ry, dx, dy)
        else:
            nrx, nry = move(rx, ry, bx, by, rx, ry, dx, dy)
            nbx, nby = move(bx, by, bx, by, nrx, nry, dx, dy)
    if dx < 0:
        if bx < rx:
            nbx, nby = move(bx, by, bx, by, rx, ry, dx, dy)
            nrx, nry = move(rx, ry, nbx, nby, rx, ry, dx, dy)
        else:
            nrx, nry = move(rx, ry, bx, by, rx, ry, dx, dy)
            nbx, nby = move(bx, by, bx, by, nrx, nry, dx, dy)
    if dy > 0:
        if by > ry:
            nbx, nby = move(bx, by, bx, by, rx, ry, dx, dy)
            nrx, nry = move(rx, ry, nbx, nby, rx, ry, dx, dy)
        else:
            nrx, nry = move(rx, ry, bx, by, rx, ry, dx, dy)
            nbx, nby = move(bx, by, bx, by, nrx, nry, dx, dy)
    if dy < 0:
        if by < ry:
            nbx, nby = move(bx, by, bx, by, rx, ry, dx, dy)
            nrx, nry = move(rx, ry, nbx, nby, rx, ry, dx, dy)
        else:
            nrx, nry = move(rx, ry, bx, by, rx, ry, dx, dy)
            nbx, nby = move(bx, by, bx, by, nrx, nry, dx, dy)
    
    crds = (nbx, nby, nrx, nry)

    if nbx == -1:
        return FAIL, crds
    if nrx == -1:
        return SUCCESS, crds
    
    return CONTINUE, crds
    
# depth는 1부터 시작
def dfs(bx, by, rx, ry, depth):
    if depth == 11:
        return 11
    
    min_move = 11
    
    for dx, dy in DIRS:
        res, crds = tilt(bx, by, rx, ry, dx, dy)
        if res == SUCCESS:
            min_move = 1
            break
        elif res == CONTINUE:
            min_move = min(min_move, dfs(*crds, depth + 1) + 1)

    return min_move


n, m = map(int, input().split())
bx, by, rx, ry = 0, 0, 0, 0

board = []

for i in range(n):
    board.append(list(input()))
    for j in range(m):
        if board[i][j] == BLUE:
            bx, by = i, j
            board[i][j] = EMPTY
        elif board[i][j] == RED:
            rx, ry = i, j
            board[i][j] = EMPTY

ans = dfs(bx, by, rx, ry, 1)

ans = ans if ans < 11 else -1
print(ans)


'''
시작 시간: 12:24
종료 시간: 13:08

접근:
    1년 전에 시도했다가 통과하지 못했던 문제이다.

    
    단순하게 DFS로 구현

    구슬을 BOARD에 입력할 건지?
    -> 복원을 해야하므로, 그냥 좌표만 유지해도 될 듯

    시간복잡도:

        최악의 경우

        4 ^ 10 번 이동시켜야 함

        4 ^ 10 = 2 ^ 20 = 1024 * 1024 = 대략 100만

        1초 = 1억번이라고 가정할 때

        100만번 연산 내에서 200의 상수시간 가능 (제한이 2초임)
후기:
    경우의 수가 그리 많지 않은 경우
    일반화를 시키기보다는 어느 정도의 코드 중복은 감수하는 것이 시간을 아끼는 방법인 것 같다.

    
    또한 ry를 rx로 잘못 적어 굉장히 디버깅을 하였다.
    답이 틀린 경우 모든 코드에 대해서 오타 점검을 할 필요가 있음

'''