from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("blank")
        self.color("white")
        self.pensize(4)
        self.setheading(90)
        self.goto(0, -300)
        self.pencolor("white")
        for i in range(0, 50):
            self.speed("fastest")
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
            if self.ycor() == 310:
                break

