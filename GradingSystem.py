print("Enetr your marks:")
m=int(input("Marks in math:"))
e=int(input("Marks in english:"))
s=int(input("Marks in science:"))
cs=int(input("Marks in computer science:"))
bio=int(input("Marks in biology:"))

total=m+e+s+cs+bio
print("You have obtained",total,"marks out of 500")
avg=total/5
print("average=",avg)
if avg>=91 and avg<=100:
    print("your grade is A1")
elif avg>=81 and avg<=90:
    print("your grade is A2")
elif avg>=71 and avg<=80:
    print("your grade is B1")
elif avg>=61 and avg<=70:
    print("your grade is B2")
elif avg>=51 and avg<=60:
    print("your grade is C1")
elif avg>=41 and avg<=50:
    print("your grade is C2")
elif avg>=33 and avg<=40:
    print("your grade is D")
else:
    print("Failed")

