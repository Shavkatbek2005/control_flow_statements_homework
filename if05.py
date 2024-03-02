def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    l=0
    if a<0:
        l-=1
    if b<0:
        l-=1
    if c<0:
        l-=1
    return l
print(main(-2,3,-4))
    
