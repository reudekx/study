def find(s, e):
    mid = (s + e) // 2
    cnt = 0
    for lan in lans:
        cnt += lan // mid
    if s == e:
        return (mid, cnt >= n)
    if cnt < n:
        return find(s, mid)
    else:
        max_len, can_make = find(mid + 1, e)
        if not can_make:
            return (mid, True)
        else:
            return (max_len, True)





k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

print(find(1, max(lans))[0])





'''
시작 시간: 20:58
종료 시간:

접근:
    최소한 n개를 만드는 최대 길이 x를 출력해야 한다.

    k <= n 이고, x는 1 이상 max(lan) 이하이다.

    max(lan)부터 1씩 감소시키며 n개 이상을 만드는 것이 가능한지 따져보면 될 듯.
    
        -> 이분 탐색 이용해서 구하기? 
        즉 1씩 감소시키는 게 아니라 이분탐색으로 상한을 찾음

        또한 개수를 구하는 것은 모든 수에 대해 나누기 연산을 하긴 해야 할 듯.
        -> 이것 또한 최적화 방법이 있을 수도? 일단 고려하지 않고 풀어보자

후기:

    max(lans) 값을 넣으려다 그냥 1, 10000으로 함수를 호출했다가 틀렸다.

    다시 생각해보니 k의 범위가 1 ~ 10000이고 랜선의 길이는 2 ^ 31 - 1 까지였다.

    수의 범위를 잘 따지자.

    또한 왼쪽 범위를 탐색할 때 mid가 닫힌 구간으로 포함되면 mid에 대한 계산이 중복되는 것 같은데..

    base case를 다시 생각해야 할 듯

'''