n = int(input())
a = list(map(int, input().split()))

stack = []
oken = [0 for _ in range(n)]

for i in range(n):
    while stack and a[i] > a[stack[-1]]:
        oken[stack[-1]] = a[i]
        stack.pop()
    stack.append(i)

while stack:
    oken[stack[-1]] = -1
    stack.pop()

print(*oken)

'''
시작 시간: 21:35
종료 시간: 21:49

접근:
    NGE(i) = Aj일 때,

    i < k
    Ai < Ak

    를 만족하는 k중 min 값이 j이다.

    모든 수에 대해 NGE를 구해야 함.

    [3, 5, 2, 7] 
    [0, 1, 2, 3]

    [2, 3, 5, 7]
    [2, 0, 1, 3]

    O(N) 또는 O(N log N) 풀이를 찾아야 함.

    이분 탐색을 해야 하나 싶은데, 조건이 2개이다.

    값도 커야하고 인덱스도 커야 한다.

    스택을 이용해야 하나?

    Top보다 작으면 스택에 넣고, Top보다 크면 pop

후기:
    문제를 모아놓은 사이트에 분류가 스택으로 되어 있었는데, 못 봐서 다행이었다.

    선형적으로 풀 방법을 생각하다가 운 좋게 떠올렸다.

    정확히는 이전에 구한 값을 이용해서 연쇄적 혹은 재귀적으로 계산할 방법을 생각해보고 있다가 떠올림.

    '스택'을 이용해서 풀 수도 있다는 것을 염두에 두어야 할 듯.

'''