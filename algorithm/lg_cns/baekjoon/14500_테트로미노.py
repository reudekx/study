from dataclasses import dataclass

@dataclass
class Shape:
    blocks: list
    h: int
    w: int

@dataclass
class Board:
    board: list
    h: int
    w: int

def get_sum(shape, board, y, x):
    res = 0
    for by, bx in shape.blocks:
        res += board.board[y + by][x + bx]
    return res

def get_max(shape, board):
    res = 0
    for y in range(board.h - shape.h + 1):
        for x in range(board.w - shape.w + 1):
            res = max(res, get_sum(shape, board, y, x))
    return res

def rotate(board):
    rotated = [[0 for _ in range(board.h)] for _ in range(board.w)]

    for y in range(board.h):
        for x in range(board.w):
            rotated[x][board.h - 1 - y] = board.board[y][x]

    return Board(rotated, board.w, board.h)

def flip(board):
    flipped = [[0 for _ in range(board.w)] for _ in range(board.h)]

    for y in range(board.h):
        for x in range(board.w):
            flipped[y][board.w - 1 - x] = board.board[y][x]

    return Board(flipped, board.h, board.w)

def solve():
    ans = 0
    board = origin
    for _ in range(4):
        for shape in shapes:
            ans = max(ans, get_max(shape, board))
        board = rotate(board)
    board = flip(board)
    for _ in range(4):
        for shape in shapes:
            ans = max(ans, get_max(shape, board))
        board = rotate(board)
    return ans

n, m = map(int, input().split())
origin = Board(
    [list(map(int, input().split())) for _ in range(n)], n, m
)

shapes = [
    Shape([
        (0, 0), (0, 1), (0, 2), (0, 3)
    ], 1, 4),
    Shape([
        (0, 0), (0, 1), (1, 0), (1, 1)
    ], 2, 2),
    Shape([
        (0, 0), (1, 0), (2, 0), (2, 1)
    ], 3, 2),
    Shape([
        (0, 0), (1, 0), (1, 1), (2, 1)
    ], 3, 2),
    Shape([
        (0, 0), (0, 1), (1, 1), (0, 2)
    ], 2, 3)
]

print(solve())


'''
깜빡하고 시간을 안 쟀다.. 30분 정도 걸린 듯

후기:
    회전 변환을 떠올려서 풀려니까 좀 헤맸음.
    아예 공식을 외우는 것도 괜찮아보인다.

    가령,
        시계방향 90도 회전 -> Transpose를 한 뒤 Horizontal Flip
        180도 회전 -> Vertical Flip
        270도 회전 -> Transpose를 한 뒤 Vertical Flip

    또한 다른 사람의 풀이를 보니
    
    도형들의 모든 경우의 수를 나열한 뒤,
    범위 검사를 통해 도형을 놓을 수 있는지 검사하는 풀이도 있었다.
    (또한, 범위 검사를 따로 진행하지 않고 sum을 구하는 과정에서, 도형의 cell이 범위를 넘어가면 sum을 0으로 하고 break)

'''