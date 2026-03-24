import turtle
turtle.Screen().bgcolor("Dark green")
turtle.Screen().setup(500,500)
p=turtle.Turtle()
n=10
l=80
angle=360.0/n
for i in range(n):
    p.forward(l)
    p.right(angle)
turtle.stamp()
turtle.done()