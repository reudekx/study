def find(k, s, e):
    mid = (s + e) // 2
    if a[mid] == k:
        return True
    if s == e:
        return False
    if a[mid] > k:
        return find(k, s, mid)
    else:
        return find(k, mid + 1, e)
    


n = int(input())
a = list(map(int, input().split()))

m = int(input())
tars = list(map(int, input().split()))

a.sort()

for tar in tars:
    print(1 if find(tar, 0, len(a) - 1) else 0)


'''
시작 시간: 20:30
종료 시간: 20:38

접근:
    이분 탐색 연습
    find(k, s, e) -> 닫힌 구간
    
    ex)
        recursive case:
            길이: 4
            mid = (0 + 3) // 2 = 1
            0, 1, 2, 3

            길이: 5
            mid = (0 + 4) // 2 = 2
            0, 1, 2, 3, 4

            mid, mid + 1로 나누는 게 적절

        base case:
            길이: 3
            mid = (0 + 2) // 2 = 1
            (0, 1), (2, 2)

            길이: 2
            mid = (0 + 1) // 2 = 0
            (0, 0), (1, 1)
            
            길이: 1
            mid = (0 + 0) // 2 == 0
            (0, 0), (1, 0)

            길이가 1이 될 때를 base case로 간주

후기:
    base case를 잘 따져서 탈출 조건을 찾아야 한다.

    상한이나 하한을 찾는 것도 연습해야 할 듯.

    가령 하한은 어떻게 구할 것인지?

    오름차순이라고 가정하고 생각해보자.

        -> 생각해보니 애초에 상한/하한은 해당 값의 존재를 찾는다기보다는 위치를 찾는 것이다.
        -> 따라서 a[mid] == k 조건을 없애고 비교 연산자를 잘 설정해주면 될 듯.

        
    또한 생각해보니가 mid가 중복된다.

    s, mid - 1 / mid + 1, e로 나눠야 하나?
'''

'''

개선된 이분탐색 함수이다.
'''


def find(k, s, e):
    if s > e:
        return False
    mid = (s + e) // 2
    if a[mid] == k:
        return True
    elif a[mid] > k:
        return find(k, s, mid - 1)
    else:
        return find(k, mid + 1, e)
