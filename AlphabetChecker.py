try:
    ch = input("Enter a character: ")

    if len(ch) != 1:
        raise ValueError("Please enter exactly one character.")

    if ch.isalpha():
        print("It is an alphabet.")
    else:
        print("It is NOT an alphabet.")

except ValueError as e:
    print(e)
