x=int(input("Enter speed 1="))
y=int(input("Enter speed 2="))
z=int(input("Enter speed 3="))

avg=(x+y+z)/3
print(avg)
if avg>x and avg>y and avg>z:
    print(avg,"is higher")
elif x>avg and x>y and x>z:
    print(x,"is higher")
elif y>avg and y>x and y>z:
    print(y,"is higher")
else:
    print(z,"is higher")