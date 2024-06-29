def solution(n):
    dirs = [
        (0, 1), (1, 0), (0, -1), (-1, 0)
    ]
    
    board = [[-1 for _ in range(n)] for _ in range(n)]
    
    y = 0
    x = -1
    di = -1
    cur = 0
    
    def is_in_bound():
        return y >= 0 and y < n and x >= 0 and x < n
    
    def can_move():
        if not is_in_bound():
            return False
        return board[y][x] == -1
    
    while True:
        di = (di + 1) % 4
        dy, dx = dirs[di]
        y, x = y + dy, x + dx
        while(can_move()):
            cur += 1
            board[y][x] = cur
            y, x = y + dy, x + dx
        y -= dy
        x -= dx
        if cur == n * n:
            break
        
        
    return board




'''
시작 시간: 18:43
종료 시간: 19:01

접근:

후기:
    접근은 괜찮았으나 오류 잡는 게 쉽지많은 않았다.
    
    값을 갱신하고 can_move를 확인했으니, 다음 진행 전에 roll back을 해줬어야 했다.
    
    또한 탈출 조건 등이 잘못되었었다.
    
    앞으론 이런 실수들을 하지 않도록 주의하고 하더라도 빨리 파악할 수 있도록..
'''