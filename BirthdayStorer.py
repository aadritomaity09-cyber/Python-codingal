valueslist = ("4/4/1985", "25/1/1987", "10/11/1989", "24/1/2010", "7/12/2015")
choice = int(input("Which item number do you want to see (1-5)? "))
try:
    print("The value is:", valueslist[choice - 1])
except IndexError:
    print("INVALID VALUE")