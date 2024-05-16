from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        file = open("data.txt")
        self.high_score = int(file.read())
        file.close()
        self.penup()
        self.goto(0, 265)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        """
        Clears the previous text of the scoreboard and writes it again.
        """
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increases the score of the player by one and rewrites it to the screen.
        """
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """
        Changes the high score if the player score is higher. Resets the
        player score to 0.
        """
        if self.score > self.high_score:
            file = open("data.txt", mode="w")
            file.write(f"{self.score}")
            file.close()
        self.score = 0
        self.update_high_score()
        self.update_scoreboard()

    def update_high_score(self):
        """
        Updates the high score attribute.
        """
        file = open("data.txt")
        self.high_score = int(file.read())
        file.close()
