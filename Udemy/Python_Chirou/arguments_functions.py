def functions(a, b):
    """ topic: arguments definied into functions """
    return (a * b)

f = functions(4, 5)
print(f) #Result: 20

def lessthan(a, b):
    """ topic: defined variables values """
    return (a - b)

f = lessthan(b=4, a=5)
print(f) #Result: 1

# condition for enter arguments
def nule(x=None, i=None):
    if x == None or i == None:
        print("enter the two value")
        return
    return x / i

print(nule(1, 4)) # Result: 0.25
