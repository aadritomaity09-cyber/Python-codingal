import sys
print("Library Book Availability Checker")
lego_series=["LEGO Star Builders","LEGO Brick Voyagers","LEGO Robo Engineers","LEGO Space Mechanics","LEGO Jungle Makers","LEGO Arctic Crew","LEGO Turbo Constructors","LEGO Desert Mechanics","LEGO Ocean Makers","LEGO Forest Rangers","LEGO City Builders","LEGO Mountain Crew","LEGO Sky Mechanics","LEGO Time Builders","LEGO Galaxy Constructors"]
football_series=["Card Collector Legends","Pro Card Dynasty","Ultimate Card Masters","Card Vault Heroes","Card Archive Elite","Card Champion Stories","Card Universe Chronicles","Card Trophy Hunters","Card Hall Adventures","Card Stadium Files","Card Match Records","Card Rising Stars","Card Goal Masters","Card Victory Tales","Card Team Chronicles"]
books=[]
for s in lego_series:
    books.append(s+" Book 1")
    books.append(s+" Book 2")
    books.append(s+" Book 3")
for s in football_series:
    books.append(s+" Book 1")
    books.append(s+" Book 2")
    books.append(s+" Book 3")
copies=[1 if i%4!=0 else 0 for i in range(len(books))]
library=dict(zip(books,copies))
print("Books:")
for i in range(0,len(books),3):
    row=books[i:i+3]
    print("{:<50}{:<50}{:<50}".format(*row))
available=[b for b in books if library[b]>0]
print("Available books:")
for i in range(0,len(available),3):
    row=available[i:i+3]
chosen=input("Which book do you want? ")
if chosen not in library or library[chosen]==0:
    print("That book is not available.")
    sys.exit()
print("You can borrow:",chosen)
