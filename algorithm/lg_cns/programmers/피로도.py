def travel(piro, visited, dungeons, dp):
    if dp[piro][visited] == -1:
        max_travel = 0
        for i in range(len(dungeons)):
            if visited & (2 ** i):
                continue
            if piro < dungeons[i][0]:
                continue
            max_travel = max(max_travel, travel(piro - dungeons[i][1], visited | (2 ** i), dungeons, dp) + 1)
        dp[piro][visited] = max_travel
    return dp[piro][visited]

def solution(k, dungeons):
    dp = [[-1 for _ in range(256)] for _ in range(5001)]
    
    
    answer = travel(k, 0, dungeons, dp)
    return answer







'''
시작 시간: 10:58
종료 시간: 11:10

접근:

    그리디하게 접근?
    DP:
        현재 state에서 최대 던전 수를 구하면 된다. (현재 피로도, 방문 여부)
        
        O(5000 * 2^8) = O(5000 * 256) 대충.. 1250,0000

    piro: 피로도
    visited: 방문 여부

    
후기:
    순열을 이용해서 푸는 방법도 있음.

    O(8! * 8)

    이게 더 빠른 듯.. 

    백각이 불여일행이라고, 순열을 이용해 직접 풀어보자

    덤으로 필요한 라이브러리를 빠르게 익혀놓는 게 좋아보인다.
'''