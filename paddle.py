from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def paddle_up(self):
        ycor = self.ycor()
        xcor = self.xcor()
        ycor += 20
        self.goto(y=ycor, x=xcor)

    def paddle_down(self):
        ycor = self.ycor()
        xcor = self.xcor()
        ycor -= 20
        self.goto(y=ycor, x=xcor)
