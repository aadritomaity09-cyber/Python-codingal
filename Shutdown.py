import sys
m = int(input("Shutdown program?(1=yes and 2=no)"))
if m==1:
    print("Shutting program down...")
elif m==2:
    print("Aborting shutdown")
    sys.exit()
a=int(input("Shut down all apps?(1=yes and 2=no)"))
if a==1:
    print("Shutting all apps down...")
elif a==2:
    print("Aborting shutdown")
    sys.exit()
g=int(input("Shut down all systems?(1=yes and 2=no)"))
if g==1:
    print("Shutting all systems down...")
elif g==2:
    print("Aborting shutdown")
    sys.exit()
i=int(input("Shut down all code?(1=yes and 2=no)"))
if i==1:
    print("Shutting all code down...")
elif i==2:
    print("Aborting shutdown")
    sys.exit()
c=int(input("Shut down everything else?(1=yes and 2=no)"))
if c==1:
    print("Shutting everything else down...")
elif c==2:
    print("Aborting shutdown")
    sys.exit()
else:
    print("Only 1 or 2")

