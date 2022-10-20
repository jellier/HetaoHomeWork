import turtle
t = turtle.Turtle()

def draw_tree(l,a):
    if l < 60-6*3:
        return
    t.left(a)
    t.fd(l)
    draw_tree(l-6,a)
    t.bk(l)
    t.right(2*a)
    t.fd(l)
    draw_tree(l-6,a)
    t.bk(l)
    t.left(a)


t.setheading(90)
draw_tree(60,30)
turtle.done()