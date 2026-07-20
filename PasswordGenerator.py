import random
length = input("How many characters should your password be? ")
length = int(length)
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#£$¤%&|"
password = ""
for i in range(length):
    random_letter = random.choice(characters)
    password = password + random_letter
print("Your new password is:")
print(password)
