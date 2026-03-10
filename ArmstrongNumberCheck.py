num=int(input("Enetr the number that you want to check that whether it is an Armstrong Number= "))
sum=0
t=num
while t>0:
    d=t%10
    sum+=d**3
    t//=10
print("The sum of the cubes is=",sum)
if num==sum:
    print("The number is an Armstrong number!")
else:
    print("The number is not an Armstrong number!")
