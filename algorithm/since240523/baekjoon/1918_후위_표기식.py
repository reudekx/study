def solve():
    op = []
    res = []

    for ch in expr:
        if ch.isalpha():
            res.append(ch)
        else:
            if ch == '(':
                op.append(ch)
                continue
            while op and precedence[op[-1]] >= precedence[ch]:
                top = op.pop()
                if top == '(':
                    break
                res.append(top)
        
            if ch != ')':
                op.append(ch)
    while op:
        top = op.pop()
        if top != '(':
            res.append(top)
    return res



expr = input()

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 0,
    ')': 0,
}

print(''.join(solve()))


'''
시작 시간: 18:40
종료 시간: 19:00

접근:
    stack의 top보다 현재 연산자가 우선순위가 더 높으면 push

    같거나 낮으면 pop

    여는 괄호 항상 push

    닫는 괄호 등장 시 여는 괄호까지 pop



후기:
    풀긴 풀었는데 내 생각에는 괄호를 따로 처리하는 로직을 다 빼도 될 것 같음.


'''