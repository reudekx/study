from itertools import permutations

def solution(k, dungeons):
    perms =  permutations(dungeons, len(dungeons))
    max_enter = 0
    for perm in perms:
        piro = k
        enter = 0
        for dungeon in perm:
            if piro < dungeon[0]:
                break
            piro -= dungeon[1]
            enter += 1
        max_enter = max(max_enter, enter)
    return max_enter
