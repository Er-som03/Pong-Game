from turtle import  Terminator,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

sc = Screen()
sc.bgcolor("black")
sc.setup(width=800, height=600)
sc.title("Pong")
sc.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()



sc.listen()
sc.onkeypress(r_paddle.go_up,"Up")
sc.onkeypress(r_paddle.go_down,"Down")
sc.onkeypress(l_paddle.go_up,"w")
sc.onkeypress(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    try:
        time.sleep(ball.move_speed)
        sc.update()
        ball.move()

        if ball.ycor()>280 or ball.ycor()<-280:
            ball.bounce_y()

        if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()< -320:
            ball.bounce_x()
           

        if ball.xcor() > 380:
            ball.reset_position()
            score.l_point()

        if ball.xcor() < -380:
            ball.reset_position()
            score.r_point()
        
        
        
        
        # Include your game logic here

    except Terminator:
        print("The Turtle graphics window was closed.")
        game_is_on = False
# sc.exitonclick()


