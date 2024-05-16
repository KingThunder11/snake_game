import turtle
from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake(Turtle):
    def __init__(self):
        """
        Creates a snake of 3 length.
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def reset(self):
        """
        Moves the snake off the screen and initializes a new snake
        at the starting positions.
        """
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Creates a new snake at the starting positions.
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Adds a segment of the snake body.
        """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        # add a new segment to the snake
        """
        Adds another segment to the end of the snake.
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Moves the snake by the move distance.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """
        Changes the move direction of the snake to up.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        """
        Changes the move direction of the snake to down.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Changes the move direction of the snake to left.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Changes the move direction of the snake to right.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)