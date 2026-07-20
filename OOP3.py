'''
Outline:
Write a program to create a class Parrot and perform the following tasks - 
1. Create a class variable species 
2. Create a __init__ method that has instance variables - name and age 
3. Create instances of class Parrot, passing arguments as well 
4. Print Class variable by accessing it 
5. Print Instance variables as well
'''
class Parrot:
    species="Bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Parrot("Polly",10)
print("The name of the parrot is ",p1.name)
print("The age of the parrot is ",p1.age)
print("The species of the parrot is ",p1.species)

