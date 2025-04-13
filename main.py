from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen=Screen()
screen.bgcolor("Black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)

# line in middle
tur=Turtle()
tur.hideturtle()
tur.color("white")
tur.penup()
tur.goto(0,300)
tur.setheading(-90)
while(tur.ycor()>=-300):
    tur.pendown()
    tur.forward(10)
    tur.penup()
    tur.forward(10)
screen.update()


right_paddle=Paddle(350,0)
left_paddle=Paddle(-350,0)
ball=Ball()
scoreboard=Scoreboard()

screen.listen()

screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")

screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")

game_is_on=True

# time_sleep=0.06

while(game_is_on):
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)
    # if(ball.ycor()>=300):
    #     ball.collision_top()
    # elif(ball.ycor()<=-300):
    #     ball.collision_bottom()
    # if(ball.xcor()>=400 or ball.xcor()<=-400):
    #     ball.setposition(0,0)
    #     ball.angle()

    # top and bottom collision
    if(ball.ycor()>=280 or ball.ycor()<=-280):
        ball.y_collision()

    # paddle collsion 
    if((ball.xcor()>320 and ball.xcor()<340 and ball.distance(right_paddle)<=65) or (ball.xcor()<-320 and ball.xcor()>-340 and ball.distance(left_paddle)<=65)):
        ball.x_collision()
        # time_sleep*=0.8
    
    #  score Board update
    if(ball.xcor()>=390):
        ball.reset_position()
        scoreboard.update_score(1,0)
    
    if(ball.xcor()<=-390):
        ball.reset_position()
        scoreboard.update_score(0,1)

    if(scoreboard.end_game()):
        game_is_on=False

screen.exitonclick()