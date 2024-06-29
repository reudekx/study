def scope():
    f = lambda: print(x)
    x = 10
    f()


scope()
print(x)