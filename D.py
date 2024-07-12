import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Drawing - Letter F")

# Create a turtle named 't'
t = turtle.Turtle()
t.hideturtle()
t.pensize(5)

t.goto(0,300)
#t.right(90)
t.fd(200)
t.circle(-100,90)
t.fd(100)
t.circle(-100,90)
t.fd(200)

t.penup()
t.goto(75,50)
t.pendown()

t.right(180)
t.fd(100)
t.circle(50,90)
t.fd(100)
t.circle(50,90)
# t.fd(50)
# t.circle(50,90)
t.fd(100)
t.left(90)
t.fd(200)



t.speed(1)
t.penup()
t.fd(10000)
t.pendown()