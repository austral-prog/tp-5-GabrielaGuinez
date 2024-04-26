def roots(a, b, c):
    d = (b**2-4*a*c)
    if d > 0:
        r1 = (-b + (d**0.5)) / 2*a
        r2 = (-b - (d**0.5)) / 2*a
        return f"{r1,r2}"
    elif d == 0:
        r12 = (-b + (d**0.5)) / 2*a 
        return f"({r12})"
    else:
        return"( )" 

    


def value_y(a, b, c, x):
    y = a * x * x + b * x + c
    return y 



def to_string(a, b, c):
    if a == 0 and b == 0:
        return f"f(x) = {c}" 
    elif a == 0 and c == 0:
        return f"f(x) = {b} * X"
    elif b == 0 and c == 0:
        return f"f(x) = {a} * X^2"
    elif a == 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0: 
        return f"f(x) = {a} * X^2 + {c}"
    elif c == 0:
        return f"f(x) = {a} * X^2 + {b} * X"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}" 



def derivation(a, b, c): 
    A = a * 2
    if a == 0:
        return f"f'(x) = {b}"
    if b == 0:
        return f"f'(x) = {A} * X"
    else:
        return f"f'(x) = {A} * X + {b}"
