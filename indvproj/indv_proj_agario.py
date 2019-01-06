from turtle import *
import turtle

class Ball(Turtle):
	def __init__(self,r,x,y,dx,dy,color):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(r/10)
		self.r = r
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.color(color)
		self.penup()
	

	def move_ball(self,screen_width,screen_height):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		top_side_ball = new_y + self.r 
		bottom_side_ball = new_y - self.r 
		if new_x >= screen_width or new_x <= -screen_width:
			self.dx = -self.dx
			new_x = current_x + self.dx
		if new_y >= screen_height or new_y <= -screen_height:
			self.dy = -self.dy
			new_y = current_y + self.dy  
		self.goto(new_x,new_y) 







	

