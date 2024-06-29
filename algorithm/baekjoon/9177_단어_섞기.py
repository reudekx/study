def check(c1, c2):
    if cache[c1][c2] is None:
        pos = c1 + c2
        if pos == len(w1) + len(w2):
            cache[c1][c2] = True
        elif c1 < len(w1) and w3[pos] == w1[c1] and check(c1 + 1, c2):
            cache[c1][c2] = True
        elif c2 < len(w2) and w3[pos] == w2[c2] and check(c1, c2 + 1):
            cache[c1][c2] = True
        else:
            cache[c1][c2] = False
    return cache[c1][c2]

n = int(input())
for i in range(n):
    w1, w2, w3 = input().split()
    cache =[[None for _ in range(len(w2) + 1)] for _ in range(len(w1) + 1)]

    print(f"Data set {i + 1}: {'yes' if check(0, 0) else 'no'}")


'''
접근:
    w3의 문자를 하나씩 순회하며
    w1와 w2 중 어떤 곳에서 문자를 가져온 것으로 할지 결정해야 한다.

    만약 어떤 쪽에서도 가져올 수 없게 된다면 false를 반환

    또한 w3에서의 위치는 지금까지 소모한 w1, w2의 문자 개수로부터 구해진다.

    pos = c1 + c2


'''