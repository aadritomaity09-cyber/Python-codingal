def cube(n):
    return n**n**n
    
def div3(n):
    if a %3==0:
        return (cube(n))
    else:
        return False
a=int(input("Enter the number to be cubed =="))
print(div3(a))
