import turtle
colors=["red","purple","yellow","orange"]
t=turtle.Pen()
turtle.bgcolor("WHITE")
t.speed(0)
for x in range(360):
    t.pencolor(colors[x%4])
    t.width(x//1000+1)
    t.forward(x)
    t.left(59)
    t.getscreen()
