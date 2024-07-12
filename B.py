import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Drawing - Letter F")

# Create a turtle named 't'
t = turtle.Turtle()
t.hideturtle()
t.pensize(5)

t.fillcolor('blue')

t.begin_fill()

t.penup()
t.goto(0,300)
t.pendown()

t.right(90)
t.fd(300)
t.left(90)
t.fd(150)
t.circle(25,90)
t.fd(100)
t.circle(25,90)

t.penup()
t.fd(100)
t.right(180)
t.fd(100)
t.pendown()

t.circle(25,90)
t.fd(100)
t.circle(25,90)
t.fd(150)

t.penup()
t.goto(25,37.5)
t.right(180)
t.pendown()

t.fd(100)
t.circle(12.5,90)
t.fd(50)
t.circle(12.5,90)
t.fd(100)
t.left(90)
t.fd(75)

t.penup()
t.goto(25,187.5)
t.right(-90)
t.pendown()


t.fd(100)
t.circle(12.5,90)
t.fd(50)
t.circle(12.5,90)
t.fd(100)
t.left(90)
t.fd(75)

t.end_fill()






t.speed(1)
t.penup()
t.fd(10000)
t.pendown()