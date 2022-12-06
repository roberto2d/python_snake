import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(1080, 720)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True

# if __name__ == '__main__':
score = Score()
timer = 0.2

while game and score.score < 50 and snake.dead == False:
    screen.update()
    time.sleep(timer)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.respawn()
        timer *= 0.95
        x = snake.segments[-1].xcor()
        y = snake.segments[-1].ycor()
        snake.create_segment((x, y))
        score.increase_score()

    if snake.dead:
        game = False
        score.right(90)
        score.forward(30)
        score.clear()
        score.write(f"\nGAME OVER\nthe highest score is {score.high_score}", align="left", font=("Ariel", 20, "normal"))

if game and score.score >= 50:
    snake.move()
    food.erase()
    time.sleep(0.1)
    score.goto(0, 10)
    score.write("\nCONGRATULATIONS!\nYou win!", align="center", font=("Ariel", 20, "normal"))

screen.exitonclick()
