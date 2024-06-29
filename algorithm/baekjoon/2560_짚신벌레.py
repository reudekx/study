MOD = 1000

def sum(k):
    if k <= 0:
        return k == 0
    if dp[k] == -1:
        dp[k] = (sum(k - 1) % MOD + sum(k - a) % MOD - sum(k - b) % MOD + MOD) % MOD
    return dp[k]

def count(k):
    return (sum(k) % MOD - sum(k - d) % MOD + MOD) % MOD

def solve(k):
    for i in range(k + 1):
        sum(i)
    return count(k)

a, b, d, n = map(int, input().split())

dp = [-1 for _ in range(n + 1)]

print(solve(n))


'''
접근:
    1. 상상
        트리 형태로 계속 증식하고 있음.

    2. state 정의
        현재 날짜는 cur이다.
        수많은 짚신벌레들이 있다..
        태어난 지 a ~ b - 1일째인 짚신벌레들이 일제히 새 개체를 낳음.
        그리고 태어난 지 d일째인 짚신벌레들이 전부 사망함.

        이 상황에서 현재 짚신벌레 수를 어떻게 구할까?

        이전 일자들의 개수 변화량을 통해 유추할 수 있어야 한다. (아니면 애초에 문제를 해결할 수 없음..)

        현재 짚신벌레들이 

        
풀이:
    Count(n)
    = Born(n) + Born(n-1) + ... + Born(n-d+1)
    = Sum(n) - Sum(n-d)

    Born(n)
    = Born(n-a) + Born(n-a-1) + ... Born(n-b+1)
    = Sum(n-a) - Sum(n-b)

    Sum(n) = Sum(n-1) + Born(n)
    = Sum(n-1) + Sum(n-a) - Sum(n-b)

'''