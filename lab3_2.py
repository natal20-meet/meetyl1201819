import turtle

"""
turtle.forward(100)
turtle.right(45)
turtle.forward(50)
"""
turtle.speed(100000000)

def make_cool_shape():
	for i in range(500):
		turtle.goto(0,0)
		turtle.forward(100)
		turtle.right(45)
		turtle.forward(100)
		turtle.right(76)
		turtle.forward(70)
		turtle.goto(0,0)
make_cool_shape()



turtle.mainloop()