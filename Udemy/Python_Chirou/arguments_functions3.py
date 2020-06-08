# Print arguments of tuple
""" def argu(*tu):
    for tus in tu:
        print(tus)

argu('name', 'lastname', 10, [1, 2, 3], (4, 5, [6, 7])) """

# Print keys of diccionary
""" def dicci(**lo):
    for x in lo:
        print(x)

dicci(name='Juan', lastname='Restrepo', age=41, sex='M', note=[10, 9, 8]) """

# print keys and values
""" def dicci(**lo):
    for x in lo:
        print(x, ":", lo[x])

dicci(name='Juan', lastname='Restrepo', age=41, sex='M', note=[10, 9, 8])
 """

 # Combine go through a dictionary and tuple
def dicci(*tu, **lo):
    b = 0
    for tus in tu:
        b += tus
        print(tus)
    print("Sum of tuple values:", b)
    for x in lo:
        print(x, ":", lo[x])

dicci(1, 2, 3, 4, name='Juan', lastname='Restrepo', age=41, sex='M', note=[20, 9, 8])
