import turtle
import time
import random
import math
from ball import Ball 
#from Turtle import Turtle Screen
turtle.tracer(10000,0)
turtle.setup(1500,1000)

turtle.title("Welcome to Agario!")
#ALL INSERTED PICTURES
turtle.register_shape("galaxy2.gif")
turtle.register_shape("uranus.gif")
turtle.register_shape("earth2.gif")
turtle.register_shape("planet.gif")
turtle.register_shape("saturn.gif")
turtle.register_shape("saturn2.gif")
turtle.register_shape("mars.gif")
turtle.register_shape("3D_Neptune.gif")
turtle.register_shape("18_mercury_new.gif")
turtle.register_shape("planet2.gif")
turtle.register_shape("jupiter.gif")
turtle.register_shape("Star.gif")
turtle.bgpic("galaxy2.gif")
#ALL VARIABLES USED
RUNNING = True 
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(50,0,0,5,10,"red")
NUMBER_OF_BALLS = 10
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5 
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5 

 
#LISTS
FOOD = []
BALLS = []
#PICS OF BALLS
MY_BALL.shape("earth2.gif")
pic3 = turtle.shape("earth2.gif")
#turning PICS into turtles
"""
pic1 = turtle.shape("uranus.gif")
pic2 = turtle.shape("jupiter.gif")
pic3 = turtle.shape("earth2.gif")
pic4 = turtle.shape("3D_Neptune.gif")
pic5 = turtle.shape("18_mercury_new.gif")
pic6 = turtle.shape("mars.gif")
pic7 = turtle.shape("saturn.gif")
pic8 = turtle.shape("saturn.gif")
pic9 = turtle.shape("planet.gif")
pic10 = turtle.shape("planet2.gif")

"""
def pick_planet():
	turtle = Turtle(visible=False)
	pic1.goto(20,20)


def onclick_handler(x, y):
    if -100 < x < 100:
        if FONTSIZE < y < FONTSIZE*3:
            turtle.undo()
            turtle.write("Option 1", font=FONT)
        elif -FONTSIZE < y < FONTSIZE:
            turtle.undo()
            turtle.write("Option 2", font=FONT)
        elif -FONTSIZE*3 < y < -FONTSIZE:
            turtle.undo()
            turtle.write("Option 3", font=FONT) 

	#screen = Screen()
	#screen.onscreenclick(onclick_handler)
	#screen.mainloop()

#HOW MANY play balls AND RANDOM CHARACTERISTICS FOR EACH
for i in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_RADIUS)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	r = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	#picture = random.randint()
	color = (random.random(),random.random(),random.random())
	ball = Ball(r,x,y,dx,dy,color)
	BALLS.append(ball)

# FOOD BALLS ARE CREATED 
def make_food():
	for n in range (100):
		x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
		y = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
		dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_RADIUS)
		dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
		r = 8
	#picture = random.randint()
		food = Ball(r,x,y,dx,dy,color) 
		FOOD.append(food)
		food.shape("Star.gif")
def eat_food():
	for food in FOOD:
		if check_collision(MY_BALL,food):
			MY_BALL_r = MY_BALL.r
			food_r = food.r
			
			new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			new_y = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			x_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			y_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			
			while x_speed == 0:
				x_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			while y_speed == 0:
				y_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			if MY_BALL.r < food.r:
				return False 	
			if MY_BALL.r > food.r:
				MY_BALL.r += 1  
				MY_BALL.shapesize((MY_BALL_r+1)/10)
				food.goto(new_x,new_y)
				food.dx=x_speed
				food.dy=y_speed
		if check_collision(ball,food):
			ball_r = ball.r
			food_r = food.r
			
			new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			new_y = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			x_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			y_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			
			while x_speed == 0:
				x_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			while y_speed == 0:
				y_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			if ball.r < food.r:
				return False 	
			if ball.r > food.r:
				ball.r += 1  
				ball.shapesize((ball_r+1)/10)
				food.goto(new_x,new_y)
				food.dx=x_speed
				food.dy=y_speed

	


#THE FUNCTION THAT CHECKS COLLISIONS
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

#THE FUNCTION THAT CHECKS THE COLLISION OF THE BALLS TOGETHER
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if check_collision(ball_a,ball_b):
				r1 = ball_a.r
				r2 = ball_b.r
				if ball_a.r > ball_b.r:
					#UPDATING THE CHARACTERISTICS AFTER COLLISION
					ball_a.r += 1 
					ball_a.shapesize((r1+1)/10)

					new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
					new_y = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
					x_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					y_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
					new_radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
					new_color = (random.random(),random.random(),random.random())
					while x_speed == 0:
						x_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_RADIUS)
					while y_speed == 0:
						y_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
					ball_b.goto(new_x,new_y)
					ball_b.dx=x_speed
					ball_b.dy=y_speed
					ball_b.r=new_radius
					ball_b.color(new_color)
					ball_b.shapesize(new_radius/10)


#THE FUNCTION THAT CHECKS THE COLLISIONS WITH MY BALL

def check_myball_collision():
	for ball in BALLS:
		if check_collision(MY_BALL,ball):
			MY_BALL_r = MY_BALL.r
			ball_r = ball.r
			
			new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			new_y = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			x_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			y_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			new_radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
			new_color = (random.random(),random.random(),random.random())
			while x_speed == 0:
				x_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			while y_speed == 0:
				y_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			if MY_BALL.r < ball.r:
				turtle.hideturtle()
				turtle.goto(0,0)
				turtle.write("GAME OVER! NICE TRY!",move=False, align='center' ,font=("Arial", 23, "bold"))
				return False 	
				
			if MY_BALL.r > ball.r:
				MY_BALL.r += 1  
				MY_BALL.shapesize((MY_BALL_r+1)/10)
				pic1.shapesize((MY_BALL_r+1)/10)
				pic1.resizemode("earth2.gif")
				ball.goto(new_x,new_y)
				ball.dx=x_speed
				ball.dy=y_speed
				ball.r=new_radius
				ball.color(new_color)
				ball.shapesize(new_radius/10)

	return True


def move_around(event):
	x = event.x - SCREEN_WIDTH
	y = -event.y + SCREEN_HEIGHT 
	MY_BALL.goto(x,y)

turtle.getcanvas().bind("<Motion>", move_around) 
turtle.listen()


make_food() 


while RUNNING:
	turtle.update()
	ball.move_ball(SCREEN_WIDTH,SCREEN_HEIGHT)
	for ball in BALLS:
		ball.move_ball(SCREEN_WIDTH,SCREEN_HEIGHT)
		time.sleep(SLEEP)
	RUNNING = check_myball_collision()
	eat_food()
	check_all_balls_collision() 
for ball in BALLS:
	ball.shapesize(0.000000001)   

turtle.update()


turtle.mainloop()