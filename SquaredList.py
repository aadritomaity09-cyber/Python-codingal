start = int(input("enter a lower range: "))
end = int(input("enter a upper range: "))
squares = [x**2 for x in range(start, end + 1)]
print(f"Squares from {start} to {end}: {squares}")
