l = [1, 2, 3, -1, 4]
s = ["H", "O", "L", "A"]
l2 = [num for num in l if num > 0]
l3 = [c * num for c in s for num in l if num > 0]

print(l)
print(l2)
print(l3)