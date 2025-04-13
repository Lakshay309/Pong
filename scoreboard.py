from turtle import Turtle

FONT=("Courier",80,"normal")
ALIGNMENT="center"
LEFT_CORRDINATE=(-100,200)
RIGHT_CORRDINATE=(100,200)
GAME_WIN=5

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score=0
        self.r_score=0
        self.display()

    def display(self):
        self.goto(LEFT_CORRDINATE)
        self.write(self.l_score,align=ALIGNMENT,font=FONT)
        self.goto(RIGHT_CORRDINATE)
        self.write(self.r_score,align=ALIGNMENT,font=FONT)

    def update_score(self,left:int,right:int):
        self.clear()
        self.l_score+=left
        self.r_score+=right
        self.display()
        
    def end_game(self):
        if(self.l_score>=5 or self.r_score>=5):
            self.goto(0,0)
            self.write("GAME OVER",font=FONT,align=ALIGNMENT)
            return True
        return False