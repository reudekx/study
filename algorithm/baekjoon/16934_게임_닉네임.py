import sys

input = sys.stdin.readline

def make_alias(nick):
    if nick in cnt:
        cnt[nick] += 1
    else:
        cnt[nick] = 1
    tree = root
    idx = None
    for i, ch in enumerate(nick):
        if ch not in tree:
            tree[ch] = {}
            if idx is None:
                idx = i
        tree = tree[ch]

    if idx is not None:
        return nick[0 : idx + 1]
    else:
        return nick + (str(cnt[nick]) if cnt[nick] > 1 else '')
    
def solve():
    for nick in nicks:
        print(make_alias(nick))

n = int(input())
nicks = [input() for _ in range(n)]
root = {}
cnt = {}

solve()