def solve():
    stack = []
    res = [-1 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        while stack and towers[stack[-1]] < towers[i]:
            res[stack.pop()] = i
        stack.append(i)
    for i in range(n):
        res[i] += 1
    return res


n = int(input())
towers = list(map(int, input().split()))
print(*solve())






"""
시작 시간: 23:04
종료 시간: 23:16

접근:
    스택 이용

    역순으로 스택에 push?

    6 9 5 7 4

    4부터 들어가고...

    stack의 top보다 큰게 등장하면 stack에서 pop 반복

    top보다 작으면 stack에 push

    즉, 자기보다 작은 것들을 모조리 pop, 그리고 자신 push

후기:
    풀이는 빠르게 떠올렸으나
    최초에 코드를 짤 때 리스트를 reverse한 뒤 연산을 하였음.
    그러나 index 자체는 순서가 보존되어 있어야 했기 때문에..

    현재의 방식으로 코드를 다시 짬

"""