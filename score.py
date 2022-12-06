from turtle import Turtle


class Score(Turtle):
    high_score: int

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.high_score = 0
        with open("data.txt", mode= "r") as data:
            self.high_score += int(data.read())
        self.score = -1
        self.color("white")
        self.goto(-500, 300)
        self.increase_score()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score} The highest score is {self.high_score}", align="left", font=("Arial", 20, "normal"))
        if self.score >= self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
