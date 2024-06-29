import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    code = list(input().split())
    if code[0] == "push":
        stack.append(code[1])
    elif code[0] == "pop":
        print(stack.pop(-1) if stack else -1)
    elif code[0] == "size":
        print(len(stack))
    elif code[0] == "empty":
        print(0 if stack else 1)
    elif code[0] == "top":
        print(stack[-1] if stack else -1)
    



"""
시작 시간: 22:58
종료 시간: 23:02

접근:

후기:
    연습용 문제

"""