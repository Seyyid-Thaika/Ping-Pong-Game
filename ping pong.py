import turtle

u = turtle.Screen()
u.title("Ping Pong by Seyyid")
u.bgcolor("green")
u.setup(width=800, height=600)
u.tracer(0)

scoreA = 0
scoreB = 0

paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("red")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)





paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("blue")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)



ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = -0.2


pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PLAYER A: 0    PLAYER B: 0", align="center", font=("Courier", 24, "bold"))


g = turtle.Turtle()
g.color("white")
g.penup()
g.hideturtle()
g.goto(0, 240)
g.write("Use 'W S' for Player A and 'UP DOWN' for Player B", align="center", font=("Courier", 12, "normal"))

def paddleAup():
    y = paddleA.ycor()
    y += 35
    paddleA.sety(y)

u.listen()
u.onkeypress(paddleAup, "w")

def paddleAdown():
    y = paddleA.ycor()
    y -= 35
    paddleA.sety(y)

u.listen()
u.onkeypress(paddleAdown, "s")

def paddleBup():
    y = paddleB.ycor()
    y += 35
    paddleB.sety(y)

u.listen()
u.onkeypress(paddleBup, "Up")

def paddleBdown():
    y = paddleB.ycor()
    y -= 35
    paddleB.sety(y)

u.listen()
u.onkeypress(paddleBdown, "Down")



while True:
    u.update()


    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)


    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreA+=1
        pen.clear()
        pen.write("PLAYER A: {}    PLAYER B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB+=1
        pen.clear()
        pen.write("PLAYER A: {}    PLAYER B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "bold"))

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()< paddleB.ycor()+40 and ball.ycor()> paddleB.ycor()-50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()< paddleA.ycor()+40 and ball.ycor()> paddleA.ycor()-50):
        ball.setx(-340)
        ball.dx *= -1










