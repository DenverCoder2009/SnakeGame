from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_NUM_OF_PARTS = 3


class Snake:

    def __init__(self):
        self.number_of_body_parts = 0
        self.body_parts_list = []
        self.initialize_snake()
        self.snake_head = self.body_parts_list[0]
        self.turned = False

    def initialize_snake(self):
        for x in range(0, STARTING_NUM_OF_PARTS):
            self.create_body_part()

    def create_body_part(self):
        new_body_part = Turtle("square")
        new_body_part.penup()
        new_body_part.color("white")
        if self.body_parts_list:
            new_body_part.goto(self.body_parts_list[self.number_of_body_parts - 1].pos()[0] - 20, self.body_parts_list[self.number_of_body_parts - 1].pos()[1])
        self.body_parts_list.append(new_body_part)
        self.number_of_body_parts += 1

    def move_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
            self.move_snake()

    def move_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
            self.move_snake()

    def move_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
            self.move_snake()

    def move_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
            self.move_snake()

    def move_snake(self):
        for index in range(self.number_of_body_parts - 1, 0, -1):
            self.body_parts_list[index].goto(self.body_parts_list[index - 1].pos())
        self.snake_head.forward(MOVE_DISTANCE)





