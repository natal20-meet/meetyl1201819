import turtle
import time
import random
import math
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
	y = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_RADIUS)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	r = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.random(),random.random(),random.random())
	ball = Ball(r,x,y,dx,dy,color)
	BALLS.append(ball)



def check_collision(ball_a,ball_b):
	if ball_a == ball_b:
		return False 
	x1 = ball_a.xcor()
	y1 = ball_a.ycor()
	x2 = ball_b.xcor()
	y2 = ball_b.ycor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if ball_a.r + ball_b.r>=(D+ 10):
		return True 
		

	else:
		return False
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if check_collision(ball_a,ball_b) == True:
				r1 = ball_a.r
				r2 = ball_b.r
				if ball_a.r > ball_b.r:
					ball_a.r += 1 
					ball_a.shapesize((r1+1)/10)

					new_x_cor = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
					new_y_cor = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
					x_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_RADIUS)
					y_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
					new_radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
					new_color = (random.random(),random.random(),random.random())
					while x_speed == 0:
						x_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_RADIUS)
					while y_speed == 0:
						y_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
					ball_b.goto(new_x_cor,new_y_cor)
					ball_b.dx=x_speed
					ball_b.dy=y_speed
					ball_b.r=new_radius
					ball_b.color(new_color)
					ball_b.shapesize(new_radius/10)

while RUNNING:
	turtle.update()
	ball.move_ball(SCREEN_WIDTH,SCREEN_HEIGHT)
	for ball in BALLS:
		ball.move_ball(SCREEN_WIDTH,SCREEN_HEIGHT)
		time.sleep(SLEEP)
	check_all_balls_collision()

#def check_myball_collision():
	#for ball in BALLS:







check_all_balls_collision(BALLS)
turtle.update()
turtle.mainloop()