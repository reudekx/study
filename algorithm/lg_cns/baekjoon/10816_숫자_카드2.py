def find_lower(k, s, e):
    if s >= e:
        return s
    mid = (s + e) // 2
    if cards[mid] >= k:
        return find_lower(k, s, mid)
    else:
        return find_lower(k, mid + 1, e)
    
def find_upper(k, s, e):
    if s >= e:
        return s
    mid = (s + e + 1) // 2
    if cards[mid] > k:
        return find_upper(k, s, mid - 1)
    else:
        return find_upper(k, mid, e)




n = int(input())
cards = list(map(int, input().split()))
m = int(input())
tars = list(map(int, input().split()))

cards.sort()

for tar in tars:
    lower = find_lower(tar, 0, n - 1)
    upper = find_upper(tar, 0, n - 1)
    print(lower, upper)
    cnt = 0 if cards[lower] != tar else upper - lower + 1
    print(cnt, end = ' ')
    print()





'''
시작 시간: 00:19
종료 시간: 00:%1

접근:
    이분 탐색으로 하한, 상한 찾기

후기:
    생각보다 base case 처리하는 게 빡셌다.
    또한 하한과 상한을 찾고 나서도
    검증을 해야하는 경우가 있었다.
    가령 cards의 최솟값 미만의 수나 최댓값 초과의 수의 경우
    lower와 upper이 각각 0과 n - 1을 가리킬 것이기 때문에 
    해당하는 원소가 1개 있는 경우와의 구분이 필요했다.

    다만 다른 존재하지 않은 수는 어째서 0이 잘 나온 건지?
    -> 확인해 볼 필요가 있어보인다.
    출력해보니 존재하지 않는 수는 그보다 더 큰 수 중 최솟값을
    lower로 가리키고 있었고,
    더 작은 수 중 최대값을 upper로 가리키고 있었다.

'''