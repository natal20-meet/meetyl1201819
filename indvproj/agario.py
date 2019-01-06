import turtle
import time
import random
from ball import Ball 
turtle.tracer(0,0)


RUNNING = True 
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(20,0,0,5,10,"red")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5 
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5 
 

BALLS = []




for i in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_RADIUS)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	r = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.random(),random.random(),random.random())
	ball = Ball(r,x,y,dx,dy,color)
	BALLS.append(ball)

for ball in BALLS:
	ball.move_ball(500,500)

while RUNNING:
	ball.move_ball(500)

turtle.update()
turtle.mainloop()