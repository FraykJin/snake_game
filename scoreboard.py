from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())

        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 12, "bold"))

    def add_score(self):
        self.score += 1
        self.refresh()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 12, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.refresh()



