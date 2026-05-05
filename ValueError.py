try:
    m=int(input("Enter a number "))
    print("Number written is",m)
except ValueError as a:
    print("Exception=",a)