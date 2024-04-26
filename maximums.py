def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x > y:
        return x 
    else:
        return y 

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if y < z < x:
        return x 
    elif x < z < y:
        return y 
    else:
        return z
