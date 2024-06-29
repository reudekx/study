def can_apply(food_cnt):
    for cnt in food_cnt.values():
        if cnt > 0:
            return False
    return True

def solution(want, number, discount):
    
    food_cnt = {}
    
    for food, cnt in zip(want, number):
        food_cnt[food] = cnt
    
    day = 0
    
    sum_number = sum(number)
    
    for i in range(sum_number):
        dis = discount[i]
        if dis in food_cnt:
            food_cnt[dis] -= 1
            
    day += can_apply(food_cnt)
            
    for i in range(sum_number, len(discount)):
        first = discount[i - sum_number]
        
        if first in food_cnt:
            food_cnt[first] += 1
        
        dis = discount[i]
        if dis not in food_cnt:
            continue
        
        food_cnt[dis] -= 1
        day += can_apply(food_cnt)
    
    return day












'''
시작 시간: 20:25
종료 시간: 20:57

접근:
    처음에는 흐름이 끊긴 날에 할인 정보를 초기화했는데..
    흐름이 끊겼더라도 시작 날짜가 달랐으면 흐름이 끊기지 않을 수도 있었던 가능성을 고려하지 못한 것이었다.

    그래서 음수가 되더라도 food_cnt를 감소시켜줬다. 어차피 first를 pop(?) 하면서 다시 복구가 되므로..

후기:

    슬라이딩 윈도우 -> 이것을 사용할 수도 있다는 점을 인지하자.

'''