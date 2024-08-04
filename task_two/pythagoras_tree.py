import turtle

def tree(tr, level, width):
    tr.forward(width)
    tr.left(30)
    if level > 0:
        tree(tr, level - 1, 3 * width / 4)
    tr.right(60)
    if level > 0:
        tree(tr, level - 1, 3 * width / 4)
    tr.left(30)
    tr.backward(width)

def draw_tree_fractal():
    level = int(input('>>> Please input level of recursion: '))
    tr = turtle.Turtle()
    tr.hideturtle()
    tr.left(90)
    tr.speed(150)
    tree(tr, level, 100)
    turtle.done()

draw_tree_fractal()
