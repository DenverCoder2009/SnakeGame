from snake import Snake
from snake_screen import SnakeScreen
from food import Food
from scoreboard import Scoreboard
import time

snake_screen = SnakeScreen()
my_snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    scoreboard.write_score()
    snake_screen.screen.listen()
    snake_screen.screen.onkey(key="Up", fun=my_snake.move_up)
    snake_screen.screen.onkey(key="Down", fun=my_snake.move_down)
    snake_screen.screen.onkey(key="Left", fun=my_snake.move_left)
    snake_screen.screen.onkey(key="Right", fun=my_snake.move_right)
    my_snake.move_snake()
    time.sleep(.05)
    snake_screen.screen.update()

    # Identifies collision with a food piece
    if my_snake.snake_head.distance(food) < 15:
        scoreboard.increment_score()
        my_snake.create_body_part()
        food.refresh()
        print("nomomomomomomom")

    # Identifies collision with the walls
    if my_snake.snake_head.xcor() > 280 or my_snake.snake_head.xcor() < -290 or my_snake.snake_head.ycor() > 280 or \
            my_snake.snake_head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # identifies collision with the snakes own body parts.
    for item in my_snake.body_parts_list[1:]:
        if my_snake.snake_head.distance(item) < 10:
            game_is_on = False
            scoreboard.game_over()

snake_screen.screen.exitonclick()
