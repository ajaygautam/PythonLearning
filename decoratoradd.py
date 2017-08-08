def add(increment):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return increment + func(*args, **kwargs)
        return wrapper
    return decorator

@add(3)
def f(n):
    return n+2

print("==== f ====")
print(f(4))


def multiply(factor):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return factor * func(*args, **kwargs)
        return wrapper
    return decorator

@multiply(3)
def g(n):
    return n+2

print("==== g ====")
print(g(4))
