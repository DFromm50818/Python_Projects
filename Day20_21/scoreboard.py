from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score {self.high_score}", align= ALIGMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.read_highscore()
        self.update_scoreboard()

    def read_highscore(self):
        with open("data.txt", mode= "r") as file:
            self.high_score = int(file.read())

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", align= ALIGMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
