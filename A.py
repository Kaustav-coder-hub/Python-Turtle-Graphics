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
t.goto(-50,0)
t.pendown()
t.left(75)
t.fd(300)
t.right(75)
t.fd(50)
t.right(75)
t.fd(300)
t.right(105)
t.fd(50)
t.right(75)
t.fd(100)
t.left(75)
t.fd(53)
t.left(75)
t.fd(100)
t.right(75)
t.fd(50)

t.penup()
t.right(180)
t.fd(50)
t.left(75)
t.fd(150)
t.pendown()

t.fd(50)
t.right(180)
t.left(30)
t.fd(50)
t.right(105)
t.fd(25)


t.end_fill()





t.speed(1)
t.penup()
t.fd(10000)
t.pendown()