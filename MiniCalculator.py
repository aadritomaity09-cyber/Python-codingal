def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def exp(a,b):
    return a**b

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exponential")

choice=int(input("Enter your choice(1-4) : "))
x=int(input("Enter num1 :"))
y=int(input("Enter num2 :"))

if choice==1:
    print("result=",add(x,y))
elif choice==2:
    print("result=",sub(x,y))
elif choice==3:
    print("result=",mul(x,y))
elif choice==4:
    print("result=",div(x,y))
elif choice==5:
    print("result=",exp(x,y))
else:
    print("Invalid choice")


