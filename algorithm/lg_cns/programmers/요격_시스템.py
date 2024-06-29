def solution(targets):
    targets.sort(key=lambda x: x[1])
    
    cnt = 0
    cur = -0.5
    for s, e in targets:
        if cur > s and cur < e:
            continue
        cur = e - 0.5
        cnt += 1
        
    return cnt
            



'''
문제:
    https://school.programmers.co.kr/learn/courses/30/lessons/181188

시작 시간: 20:23
종료 시간: 20:33

접근:
    무조건 0.5 단위로 쏴도 된다.
    
    정렬을 이용해야 할 듯.
    
    가령, 미사일들을 순서대로 나열하고,
    
    시간에 따라 요격을 한다고 했을 때
    
    지나간 미사일들에 대해선 요격을 할 수 없다고 치자. 
    -> 즉 어떤 미사일이 '지나가 버리기' 전에 '무조건' 요격을 해야 한다.
    
    그렇다면 e에 대해 오름차순으로 정렬하고, 
    첫번째 미사일의 e - 0.5에 대해 요격을 진행하고, 피격된 미사일들을 제거한다.
    
    이후 이걸 반복

후기:
    직관적으로 해답이 보여서 풀 수 있었다.
    
    정렬을 하는 것과, 강제로 순서를 부여하는 것이 핵심
'''