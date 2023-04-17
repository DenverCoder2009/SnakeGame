from turtle import Screen


class SnakeScreen:

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake")
        self.screen.tracer(0)
