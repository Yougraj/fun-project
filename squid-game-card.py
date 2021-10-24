import turtle

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
tim.right(90)
tim.forward(150)
tim.right(90)
tim.forward(300)
tim.right(180)
tim.pendown()
tim.pensize(15)


def horizontal():
    for i in range(6):
        tim.forward(100)
    tim.left(90)


def vertical():
    for i in range(3):
        tim.forward(100)
    tim.left(90)


def tringle():

    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.pendown()
    for i in range(3):
        tim.forward(120)
        tim.right(120)
    tim.penup()

def squar():
    tim.left(90)
    tim.forward(50)
    tim.left(180)
    tim.pendown()
    for i in range(4):
        tim.forward(100)
        tim.left(90)
    tim.penup()

def circle():
    tim.right(90)
    tim.forward(50)
    tim.pendown()
    tim.circle(50)
    tim.penup()

def boder():
    tim.fillcolor("#b68d60")
    tim.begin_fill()
    horizontal()
    vertical()
    horizontal()
    vertical()
    tim.end_fill()

def squid_game_card():
    boder()
    tim.penup()
    tim.goto(0, 0)
    tim.right(180)
    tim.forward(200)
    tim.right(180)
    tim.forward(300)
    squar()
    tim.forward(50)
    tim.right(90)
    tim.forward(50)

    tringle()
    tim.forward(150)
    circle()

    screen = turtle.Screen()
    screen.exitonclick()

if __name__ == "__main__":
    squid_game_card()
   
