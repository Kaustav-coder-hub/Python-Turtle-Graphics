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
t.fd(200)
t.right(90)
t.fd(50)
t.right(180)
t.pendown()


t.circle(100,180)
t.fd(100)
t.circle(100,180)
t.left(90)
t.fd(50)
t.right(-90)
t.circle(-50,180)
t.fd(100)
t.circle(-50,180)
t.left(90)
t.fd(50)


t.end_fill()




t.speed(1)
t.penup()
t.fd(10000)
t.pendown()