import turtle
from turtle import Turtle
import random

turtle.colormode(255)
class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")
	def pick_color(self):	
		R = random.randint(0,255)
		B = random.randint(0,255)
		G = random.randint(0,255)
		self.color(R,B,G)
#square1 = Square(25)
#square1.pick_color()
"""
class Rectangle(object):
	def __init__(self,width,height)
		self.width = width
		self.height = height
	def make_shape(self):
"""

		

		

turtle.mainloop()