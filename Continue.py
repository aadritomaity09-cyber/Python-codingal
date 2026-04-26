var=int(input("Enter a number: "))
while var>0:
    var=var-1
    if var==5:
        continue
    print(var,end="|")