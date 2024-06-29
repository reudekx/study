def advance():
    global cur, bingo, diag1, diag2
    x, y = coord[call[cur]]
    x_line[x] -= 1
    y_line[y] -= 1
    if x == y:
        diag1 -= 1
    if x == 4 - y:
        diag2 -= 1

    if x_line[x] == 0:
        bingo -= 1
        x_line[x] = -1
    if y_line[y] == 0:
        bingo -= 1
        y_line[y] = -1
    if diag1 == 0:
        bingo -= 1
        diag1 = -1
    if diag2 == 0:
        bingo -= 1
        diag2 = -1
    cur += 1

board = []
coord = {}
for i in range(5):
    board.append(list(map(int, input().split())))
    for j in range(5):
        coord[board[i][j]] = (i, j)

call = []
for _ in range(5):
    call.extend(list(map(int, input().split())))

x_line = [5 for _ in range(5)]
y_line = [5 for _ in range(5)]
diag1 = 5
diag2 = 5

cur = 0
bingo = 3


while bingo > 0:
    advance()

print(cur)




'''
시작 시간: 22:20
종료 시간: 22:50

접근:
    board에 숫자를 저장하고,
    숫자를 통해 board에서의 위치를 O(1)에 참조할 수 있도록

    빙고를 어떻게 확인할지?

    수를 지울 때 확인할 수 있다.
    대각선까지 포함하면 최대 4개의 선을 확인해야 한다.

    각 선에 5의 값을 부여한 뒤 1씩 제거할 수 있다.

    다 제거하고 나면 0이되고, -1로 변경

    대각선 구분
    -> x == y 이면 대각선 1

    -> x == 4 - y 이면 대각선 2

후기:
    diag1, diag2 변수를 실수로 list로 설정해버려서 시간이 좀 걸렸다.
    디버깅을 잘 해야한다.

    다른 풀이도 잘 확인해보자.

'''