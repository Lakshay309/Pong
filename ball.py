from turtle import Turtle
import random

INIT_SPEED=0.06
ANGLES=[-10,10]
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.setposition(0,0)
        self.move_speed=INIT_SPEED
        # self.angle()
        self.x_move=random.choice(ANGLES)
        self.y_move=random.choice(ANGLES)

    # def angle(self):
    #     ball_angle=random.choice(ANGLES)
    #     self.setheading(ball_angle)

    def move(self):
        # self.forward(10)
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    # def collision_top(self):
    #     if 0 < self.heading() < 180:
    #         self.setheading(-self.heading())

    # def collision_bottom(self):
    #     if 180 < self.heading() < 360:
    #         self.setheading(-self.heading())
    def y_collision(self):
        self.y_move=-self.y_move
    
    def x_collision(self):
        self.x_move=-self.x_move
        self.move_speed*=0.8

    def reset_position(self):
        self.setposition(0,0)
        self.x_move=-self.x_move
        self.move_speed=INIT_SPEED
    