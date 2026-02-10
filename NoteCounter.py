amount=int(input("Enter your amount:"))
note1=amount//1000
note2=(amount%1000)//500
note3=((amount%1000)%500)//100

print(note1)
print(note2)
print(note3)
