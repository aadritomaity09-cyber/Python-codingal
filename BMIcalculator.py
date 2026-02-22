h=float(input("Height="))
w=float(input("Weight="))
bmi=w/h**2
if bmi<=18.4:
    print("Underwight")
elif bmi<=24.9:
    print("Healthy")
elif bmi<=29.9:
    print("Overweight")
elif bmi<=34.9:
    print("Severely Overwight")
elif bmi<=39.9:
    print("Obese")
else:
    print("Severely Obese")        
