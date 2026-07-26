import random
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))
print("\nBefore swap:")
print("a =", a)
print("b =", b)
print("c =", c)
nums = [a, b, c]
random.shuffle(nums)
a, b, c = nums
print("\nAfter random swap:")
print("a =", a)
print("b =", b)
print("c =", c)
