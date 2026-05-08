try:
    m = int(input("Enter your age: "))

    if m % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

except ValueError:
    print("Invalid input! Please enter a number.")

finally:
    print("This program will run no matter what")

print("Have a good day")

