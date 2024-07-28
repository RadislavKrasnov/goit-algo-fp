import turtle

WIDTH = 15
BRANCH_LENGTH = 120
ROTATION_LENGTH = 27

def draw_tree_fractal():
    level = int(input('>>> Please input level of recursion: '))
    turt = turtle.Turtle()
    turt.hideturtle()
    turt.speed('fastest')
    turt.left(90)
    turt.width(WIDTH)
    turt.penup()
    turt.back(BRANCH_LENGTH * 1.5)
    turt.pendown()
    turt.forward(BRANCH_LENGTH)
    draw_tree(turt, BRANCH_LENGTH, level)
    turtle.done()

def draw_tree(turt, branch_length, level):
    width = turt.width()
    turt.width(width * 3. / 4.)
    branch_length *= 3. / 4.
    turt.left(ROTATION_LENGTH)
    turt.forward(branch_length)

    if level > 0:
        draw_tree(turt, branch_length, level - 1)
    turt.back(branch_length)
    turt.right(2 * ROTATION_LENGTH)
    turt.forward(branch_length)

    if level > 0:
        draw_tree(turt, branch_length, level - 1)
    turt.back(branch_length)
    turt.left(ROTATION_LENGTH)

    turt.width(width)

draw_tree_fractal()
