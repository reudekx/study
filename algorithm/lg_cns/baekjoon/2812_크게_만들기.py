n, k = map(int, input().split())

s = list(map(int, input()))
stack = [s[0]]

for num in s[1:]:
    while k > 0 and stack and num > stack[-1]:
        stack.pop()
        k -= 1
    stack.append(num)

while k and stack:
    stack.pop()
    k -= 1

for num in stack:
    print(num, end='')
print()


# n, k = map(int, input().split())

# s = list(map(int, input()))
# idx = [i for i in range(n)]

# idx.sort(key=lambda x: s[x], reverse=True)

# removed = [False for _ in range(n)]
# pre = -1

# for i in range(n):
#     if (idx[i] - pre - 1) <= k and idx[i] > pre:
#         for j in range(pre + 1, idx[i]):
#             k -= 1
#             removed[j] = True
#         pre = idx[i]

# print(k, idx)

# for i in range(n):
#     if not removed[i]:
#         print(s[i], end='')
# print()



'''
1 9 2 4
0 1 2 3

9 4 2 1
1 3 2 0

'''

'''
시작 시간: 21:57
종료 시간: 22:52

접근:
    그냥 정렬을 한 뒤 숫자를 제거하면 되는 게 아닌지?
    0이 걸림돌이 되나? 그런데 문제에는 딱히 별 말이 없음.

    생각을 잘못 함. 숫자를 그냥 지우면 되는 게 아니라 위치를 고려해야 한다. 가령 맨 뒤에 있는 0보다는
    맨 앞 2개가 순서대로 8, 9 일 때 8을 지우는 게 이득이다.

    가령,
        제일 큰 숫자 중 제일 먼저 나오는 A에 대해 지워야 할 숫자가 k개일 때,
        A의 앞에 숫자가 k개 이하라면 해당 숫자들을 전부 제거해야 한다.

        즉 숫자들을 내림차순으로 정렬하고, 
        x(x <= k)개를 지울 수 있다면>
            만약 x == k였다면 종료이고,
            x < k 라면?

            여분을 가지고 다음 수 B에 대해 따져본다.

            만약 B가 A와 같다면, A보다 뒤에 있다는 것이 보장되므로
            A와의 index 사이에 있는 숫자들만 제거하면 된다.

            만약 B가 A보다 작다면?
            
                B가 A보다 앞섰다면 제거되었을 것이니 신경 쓸 필요가 없고, skip하면 된다.
                B가 A보다 뒤에 있다면, 마찬가지로 사이의 index를 제거하면 된다.



        지울 수 없다면?
            이제 A보다 작은 수 중 가장 먼저 나오는 수에 대해 따져보면 된다.

            또한 이때 해당 숫자들은 A보다 더 앞에 있게 된다.

        이를 반복하면 됨.

    파이썬의 sort는 stable 하다는 점을 이용하자.

    
    10:24)
        그냥 스택을 이용했어야 했나?

후기:
    이 문제를 풀기 직전 스택 문제를 풀었는데..
    스택을 사용하면 된다는 것을 바로 눈치채지 못했다.

    첫 단추를 잘못 끼운 상태로 시작을 해버린 게 잘못이었던 것 같다.

    또한 ''.join(map(str, stack)) 을 통해 출력했어도 됐다.

'''