""" # recursive function
def back_count(seconds):
    seconds -= 1
    if seconds > 0:
        print(seconds)
        back_count(seconds)
    else:
        print("end_count")

back_count(10) """


""" # convert functions
e = int("-15")
print(type(e), e)


print("binary: ", bin(e), type(e), e)

print("hexagecimal: ", hex(e), type(e), e)

print("absolute value: ", abs(e), type(e), e)
 """
