import turtle
from random import randint, choice
# import random

# screen settings
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.screensize(5*WIDTH, 5*HEIGHT)
# screen.bgpic('fantasy.gif')
screen.delay(0)
# turtle settings
leo = turtle.Turtle()
leo.pensize(3)
leo.speed(0)
leo.penup()
leo.setpos(WIDTH // 6, -HEIGHT // 4 - 25)
leo.pendown()
leo.color(random.choice(["red", "green", "blue", "pink", "purple"]))


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else chr for chr in axiom])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom

# turtle.pencolor('white')
# turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
# turtle.clear()
# turtle.write(f'generation: {gens}', font=("Arial", 60, "normal"))

leo.left(90)
while(True):
    # l-system settings
    gens = 13
    axiom = 'XY'
    chr_1, rule_1 = 'X', 'F[@[-X]+X]'
    step = 90
    angle = lambda: randint(0, 45)
    stack = []
    color = [0.35, 0.2, 0.0]
    thickness = 20
    
    axiom = get_result(gens, axiom)
    leo.pensize(thickness)
    for chr in axiom:
        # leo.color(color)
        if chr == 'F' or chr == 'X':
            leo.forward(step)
        elif chr == '@':
            step -= 6
            color[1] += 0.04
            thickness -= 2
            thickness = max(1, thickness)
            leo.pensize(thickness)
        elif chr == '+':
            leo.right(angle())
        elif chr == '-':
            leo.left(angle())
        elif chr == '[':
            angle_, pos_ = leo.heading(), leo.pos()
            stack.append((angle_, pos_, thickness, step, color[1]))
        elif chr == ']':
            angle_, pos_, thickness, step, color[1] = stack.pop()
            leo.pensize(thickness)
            leo.setheading(angle_)
            leo.penup()
            leo.goto(pos_)
            leo.pendown()
            
    leo.penup()
    leo.setpos(randint(0, WIDTH), -HEIGHT // 4 - 25)
    leo.pendown()
    leo.color(random.choice(["red", "green", "blue", "pink", "purple", "black"]))

screen.exitonclick()
