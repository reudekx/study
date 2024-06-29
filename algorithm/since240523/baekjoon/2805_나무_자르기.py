import sys
input = sys.stdin.readline

def find(k, s, e):
    if s >= e:
        return s
    mid = (s + e + 1) // 2
    taken = 0
    for tree in trees:
        taken += max(0, tree - mid)
    if taken < m:
        return find(k, s, mid - 1)
    else:
        return find(k, mid, e)

n, m = map(int, input().split())

trees = list(map(int, input().split()))

print(find(m, 0, max(trees)))

'''
시작 시간: 19:19
종료 시간: 19:31

접근:
    max(tree)부터 0까지 감소시키며 m미터 이상의 나무를 가져갈 수 있는
    최대 높이를 구하면 된다.
    
    이분 탐색 이용

    가령, mid = max(tree) 의 높이에서 잘랐을 때

    m미터 이상이 확보되면, 높이를 더 높여도 된다.

    만약 확보되지 않으면 높이를 낮춰야 한다.

후기:
    제출했을 때 시간초과가 뜨길래 base case를 따져봤는데
    잘못된 부분이 없는 것 같아 입력 함수를 교체하고 pypy로 제출했더니 통과함.


'''