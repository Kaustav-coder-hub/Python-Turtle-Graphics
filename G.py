import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Drawing - Letter G")

# Create a turtle named 't'
t = turtle.Turtle()
t.hideturtle()
t.pensize(5)

t.fillcolor('blue')

t.begin_fill()

t.left(90)
t.fd(100)
t.circle(-100,90)
t.fd(100)
t.right(90)
t.fd(50)
t.right(90)
t.fd(100)
t.circle(50,90)
t.fd(100)
t.circle(50,90)
t.fd(50)
t.left(90)
t.fd(50)
t.left(90)
t.fd(50)
t.right(90)
t.fd(50)
t.right(90)
t.fd(100)
t.right(90)
t.fd(150)
t.right(90)
t.fd(100)
t.circle(-100,90)

t.end_fill()

t.speed(1)
t.penup()
t.fd(10000)
t.pendown()