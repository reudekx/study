dirs = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]

def is_in_bound(r, c):
    return r >= 0 and r < n and c >= 0 and c < m

def can_move(r, c):
    if not is_in_bound(r, c):
        return False
    return room[r][c] != 1

def count(r, c, d):
    cnt = 0
    while True:
        if room[r][c] == 0:
            room[r][c] = 2
            cnt += 1
        
        nd = -1

        for i in range(1, 5):
            dr, dc = dirs[(d - i + 4) % 4]
            nr, nc = r + dr, c + dc
            if is_in_bound(nr, nc) and room[nr][nc] == 0:
                nd = (d - i + 4) % 4
                break


        if nd == -1:
            dr, dc = dirs[d]
            if can_move(r - dr, c - dc):
                r, c = r - dr, c - dc
            else:
                break
        else:
            d = nd
            dr, dc = dirs[d]
            r, c = r + dr, c + dc

    return cnt


n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

print(count(r, c, d))

'''
시작 시간: 19:14
종료 시간: 19:49

접근:

후기:
    '반시계로 회전한다' -> 만약 현재 방향의 앞 칸이 청소 가능하더라도 먼저 반시계로 회전했어야 했는데.. 이를 놓쳤다.

    조건을 꼼꼼하게 따져볼 필요가 있어 보인다.

    그리고 r, c도 알파벳을 틀린다든가 하는 오류가 존재했음.

    시뮬레이션 문제는, 직접 시뮬레이션을 진행하며 (내가 짠) 코드와 다른 부분이 있나 관찰해봐도 좋을 것 같다.

    또한 청소 구역을 세는 로직을 따로 빼낼 수도 있다.

'''