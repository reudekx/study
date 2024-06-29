# 순서쌍
pair = lambda a: lambda b: lambda f: f(a)(b)
first = lambda a: lambda b: a
second = lambda a: lambda b: b

# 수
zero = lambda f: lambda x: x



succ = lambda n: lambda f: lambda x: f(n(f)(x))

add = lambda m: lambda n: m(succ)(n) # lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))

mul = lambda m: lambda n: m(add(n))(zero)


# 출력
three = lambda f: lambda x: f(f(f(x)))

prt = lambda n: print(n(lambda x: x + 1)(0))

# prt(add(three)(three))


# 논리 연산


# 피보나치

# 단순한 버전
simple_fib = (lambda x: x(x))(lambda f: lambda n: 1 if n <= 1 else f(f)(n - 2) + f(f)(n - 1))

# Y Combinator
Y = lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))

fib = lambda f: lambda n: 1 if n <= 1 else f(n - 2) + f(n - 1)

for i in range(10):
    print(Y(fib)(i))