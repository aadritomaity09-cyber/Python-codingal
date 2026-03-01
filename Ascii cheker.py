print(ord('5'))

print(ord('9'))

print(chr(53))

print(chr(9))


char = input("Enter a single character: ")

if type(char) is str and len(char) == 1:

    print("Valid input!")

else:

    print("Please enter exactly ONE character!")

ascii_val = ord(char)

# Display the result

print(f"Character: {char}")

print(f"ASCII Value: {ascii_val}")