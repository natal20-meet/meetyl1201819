from turtle import * 
import random 
import turtle 
import math
turtle.tracer(0)
class Ball(Turtle):
	def __init__(self,radius,color,dx,dy):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.dx = random.randint(-350,350)/300
		self.dy = random.randint(-350,350)/300
		self.color(color)
		


	def move_ball(self,height,width):
		old_x = self.xcor()
		old_y = self.ycor()
		new_x = old_x + self.dx
		new_y = old_y + self.dy
		if new_x >= width or new_x <= -width:
			self.dx = -self.dx 
			new_x = old_x + self.dx 
		if new_y >= height or new_y <= -height:
			self.dy = -self.dy
			new_y = old_y + self.dy  
		self.goto(new_x,new_y)
		#check_collision(ball1,ball2)


ball1 = Ball(20,"Red",1,1)
ball2 = Ball(40,"Blue",1,1)

def check_collision(ball1,ball2):
	x2 = ball1.xcor()
	x1 = ball2.ycor()
	y2 = ball1.xcor()
	y1 = ball2.ycor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if ball1.radius + ball2.radius>=D:
		return True 
	else:
		return False
	


while True:
	ball1.penup()
	ball1.move_ball(450,450)
	ball2.penup()
	ball2.move_ball(450,450)
	
	if check_collision(ball1,ball2):
		print("we have a collision")
	turtle.update()
#turtle.mainloop()










