num1=[1,2,3,4,5]
num2=[10,20,30,40,50]
result=map(lambda x,y:x+y,num1,num2)
print("addition of 2 lists")
print(list(result))


nums=[6,7,8,9,10]
def sq(n):
    return n*n
m=list(map(sq,nums))
print("the squares of numbers in a list",m)
