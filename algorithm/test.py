import dis

def f(x):
    return lambda a: a + x

dis.dis(f)