import turtle
import random
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(800,600)
turtle.tracer(False)
t.hideturtle()
# l 为长度，a为角度, c代表层数
def draw_tree(l,a,c):
    if l < first_l-6*(c-1):
        return
    t.left(a)
    t.fd(l)
    draw_tree(l-6,a,c)
    t.bk(l)
    t.right(2*a)
    t.fd(l)
    draw_tree(l-6,a,c)
    t.bk(l)
    t.left(a)

for i in range(50):
    x = random.randint(-400,400)
    y = random.randint(-300,300)
    t.penup()
    t.goto(x,y)
    t.pendown()
    if x >= 0:
        t.setheading(45)
        angle = 10
    else:
        t.setheading(135)
        angle = -10
    shu_ceng = random.randint(4,6)
    first_l = random.randint(30,60)
    draw_tree(first_l,angle,shu_ceng)


turtle.done()
