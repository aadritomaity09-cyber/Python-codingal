try:
    m,a=eval(input("Enter 2 numbers (m,a) "))
    res=m/a
    print("Result=",res)
except ZeroDivisionError:
    print("Divided by 0")
except SyntaxError:
    print("Comma is missing")
except:
    print("Wrong input")
else:
    print("No exception")
finally:
    print("The progarm will run no matter what")