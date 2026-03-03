m=input("Did you have a medical cause (y/n)=")
a=float(input("Enter you attendence:"))
if m=="y":
    print("you are allowed to the test")
else:
    if a>=75:
        print("You are allowed to take the test")
    else:
       print("No,Unfortunately you ar enot allowed to the take the test")