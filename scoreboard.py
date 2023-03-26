from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def read_high_score(self):
        try:
            with open("data.txt", mode="r") as file:
                self.high_score = int(file.read())
        except(FileNotFoundError, ValueError):
            self.high_score = 0
        return self.high_score

    def write_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
