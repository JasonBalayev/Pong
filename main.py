#import statements
import turtle as t
import winsound
   
                                                                                               
pong = t.Screen()
pong.tracer(0)
pong.title('AP CSP Pong')
pong.bgcolor('black')
pong.setup(width=1200, height=615)

#list
first_name = t.textinput("What is Player 1's name", "Name")
second_name = t.textinput("What is Player 2's name", "Name")

list_names = [first_name,second_name]

#score display
score = t.Turtle()
score.color('white')
score.penup()
score.goto(0, 260)
score.color("red")
score.write(list_names[0] + ": 0"  +"                                    "+ list_names[1]+": 0", align='center', font=('Arial', 24, 'bold'))
score.hideturtle()

#score variables
score_1 = 0
score_2 = 0

#characters
left_paddle = t.Turtle()
left_paddle.speed(0)
left_paddle.shape('square')
left_paddle.color('white')
left_paddle.shapesize(stretch_wid=8, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-355,0)
left_paddle_score = 0

right_paddle = t.Turtle()
right_paddle.speed(0)
right_paddle.shape('square')
right_paddle.color('white')
right_paddle.shapesize(stretch_wid=8, stretch_len=1)
right_paddle.penup()
right_paddle.goto(355,0)
 
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball_dx = 1.5 
ball_dy = 1.5

# visible barrier drawings
barriers1 = t.Turtle()
barriers1.shape('square')
barriers1.color('red')
barriers1.shapesize(stretch_wid=1, stretch_len=40)
barriers1.penup()
barriers1.goto(0,220)

barriers2 = t.Turtle()
barriers2.shape('square')
barriers2.color('red')
barriers2.shapesize(stretch_wid=22, stretch_len=1)
barriers2.penup()
barriers2.goto(-390,0)

barriers3 = t.Turtle()
barriers3.shape('square')
barriers3.color('red')
barriers3.shapesize(stretch_wid=22, stretch_len=1)
barriers3.penup()
barriers3.goto(390,0)

barriers4 = t.Turtle()
barriers4.shape('square')
barriers4.color('red')
barriers4.shapesize(stretch_wid=1, stretch_len=40)
barriers4.penup()
barriers4.goto(0,-220)

#the right paddle functions
def b():
    y = right_paddle.ycor()
    y -= 30
    right_paddle.sety(y)

def f():
    y = right_paddle.ycor()
    y += 30
    right_paddle.sety(y)

#the left paddle functions
def b_1():
    y = left_paddle.ycor()
    y -= 30
    left_paddle.sety(y)

def f_1():
    y = left_paddle.ycor()
    y += 30
    left_paddle.sety(y)

def endgame():
    t.hideturtle()
    t.bgcolor("black")
    left_paddle.hideturtle()
    right_paddle.hideturtle()
    score.hideturtle()
    score.clear()
    ball.hideturtle()
    barriers1.hideturtle()
    barriers2.hideturtle()  
    barriers3.hideturtle()
    barriers4.hideturtle()            

#onclick events
def new_func(b, f, b_1, f_1):
    t.listen()
    t.onkeypress(f,'Up')
    t.onkeypress(b,'Down')
    t.onkeypress(f_1,'w')
    t.onkeypress(b_1,'s')

new_func(b, f, b_1, f_1)

#get hit (iteration)
while True:
    pong.update()

    # Moving Ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # Border checking
    if ball.ycor() > 200 or ball.ycor() < -200:
        ball_dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx *= -1
        score_1 += 1
        score.clear()
        score.write(list_names[0]  + ": " + str(score_1) +"                                    "+ list_names[1] +": "+ str(score_2), align='center', font=('Arial', 24, 'bold'))
       
    if (ball.xcor() < -390):
        ball.goto(0, 0)
        ball_dx *= -1
        score_2 = score_2 + 1
        score.clear()
        score.write(list_names[0]  + ": " + str(score_1) +"                                    "+ list_names[1] +": "+ str(score_2), align='center', font=('Arial', 24, 'bold'))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 82 and ball.ycor() > right_paddle.ycor() -60):
        ball.setx(340)
        ball_dx *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 82 and ball.ycor() > left_paddle.ycor() -60):
        ball.setx(-340)
        ball_dx *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)
    
    # end screen 
    if(score_1 > 4):
        t.color("white")
        t.write("Congrats " + list_names[0] +", you win with a score of " + str(score_1),align='center', font=('Arial', 24, 'bold'))
        endgame()
    elif(score_2 > 4):
        t.color("white")
        t.write("Congrats " + list_names[1] + ", you won with a score of " + str(score_2),align='center', font=('Arial', 24, 'bold'))
        endgame() 