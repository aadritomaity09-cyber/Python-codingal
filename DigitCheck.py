s=int(input("Enter a number:"))
sum=0
temp=abs(s)
count=0
if temp==0:
    count=1
else:
    while temp>0:
        temp=temp//10
        count+=1
    print(f"There are",count,"numbers")