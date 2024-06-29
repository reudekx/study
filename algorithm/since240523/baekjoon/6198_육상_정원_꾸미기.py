def solve():
    stack = []
    cnt = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        while stack and h[stack[-1]] < h[i]:
            cnt[i] += cnt[stack.pop()] + 1
        stack.append(i)
    return sum(cnt)

n = int(input())
h = [int(input()) for _ in range(n)]
print(solve())



"""
시작 시간: 23:18
종료 시간: 23:28

접근:
    스택 이용

    볼 수 있는 각각의 개수를 구하는 것이 아닌 합을 구하는 것이 핵심?
        -> 합을 구하는 건 쉽지만 각각의 개수를 구하는 건 어려울 수 있음

    10 3 7 4 12 2

    최초 push 10

    3 -> 10이 볼 수 있음. 일단 push 3

    7 -> 3이 볼 수 없음. pop 3

    뭔가 이상.. 차라리 자신을 '본' 놈을 구한다면?

    역순으로 접근하면 될 듯.

    또한 스택에 남아있는 놈이 본 개수는 자신도 볼 수 있다.

후기:
    결과적으로 자신'이' 본 개수를 구하긴 했는데,

    자신'을' 본 개수를 구하려면 정방향으로 진행했어야 했다.

    가령, [10, 7]이 들어있는 상태에서 4를 확인하면, 4는 스택에 푸시되고, 4를 본 개수는 stack의 기존 길이일 것이다.

"""