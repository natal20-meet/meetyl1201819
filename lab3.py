import turtle 
#turtle.right(45)
#turtle.forward(60)
#turtle.left(150)
#turtle.forward(60)
angle = 144
length = 100
def draw_star(angle,length):
	for i in range(5):
		turtle.left(angle)
		turtle.forward(length)
turtle.hideturtle()
#draw_star(angle,length)
angle_2 = 90
length_2 = 50
angle_3 = 55
length_3 = 50
angle_4 = 120
def draw_shape(angle,length):
	for i in range(4):
		turtle.forward(length_2)
		turtle.left(angle_2)
	for i in range(1):
		turtle.right(angle_3)
		turtle.forward(length_3)
		turtle.left(angle_4)
		turtle.forward(length_3)
draw_shape(angle,length)

turtle.mainloop()



