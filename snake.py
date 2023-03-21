from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.initial_size = 3
        self.initial_position = (0, 0)
        self.move_distance = 20
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(self.initial_size):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(self.initial_position[0] - i * 20, self.initial_position[1])  # x=0,-20,-40 and y=0
            self.snake_body.append(segment)

    def extend_snake(self):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        last_segment = self.snake_body[-1]  # [-1] refers to last object on the snake_body list
        segment.goto(last_segment.xcor(), last_segment.ycor())  # new segment goes to the position of tail segment
        self.snake_body.append(segment)
        # new segment and tail segment will overlap initially before new movement update

    def move_snake(self):
        # Iterate through the snake body segments in reverse order, starting from the tail
        # and stopping just before the head (body_segment = 1).
        for body_segment in range(len(self.snake_body) - 1, 0, -1):
            # Get the x and y coordinates of the previous segment (body_segment - 1)
            x = self.snake_body[body_segment - 1].xcor()
            y = self.snake_body[body_segment - 1].ycor()

            # Move the current segment (body_segment) to the position of the previous segment
            self.snake_body[body_segment].goto(x, y)

        # Move the head of the snake forward by 20 units in its current direction
        self.head.forward(self.move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
