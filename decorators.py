def printlog(func):
    def wrapper(*arg, **kwargs):
        print("Calling: " + func.__name__ + " with arg " + str(arg))
        return func(*arg, **kwargs)
    return wrapper

@printlog
def f(n, d):
    return n+d

print("==== f ====")
print(f(3, 4))

def add(increment):
    def decorator(func):
        def wrapper(arg):
            return increment + func(arg)
        return wrapper
    return decorator

@add(3)
def g(n):
    return n*2

print("==== g ====")
print(g(10))
