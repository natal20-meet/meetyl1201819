class Animal(object):
	def __init__(self,sound,name,age,fav_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.fav_color = fav_color
	def eat(self,food):
		print("Yummy!! " + self.name + " is eating a " + food)
	def description(self):
		print(self.name + " is " + str(self.age) + " years old and loves the color " + self.fav_color)
a = Animal("whoof", "Cookie" , 2, "red")
a.eat("bone")
a.description()
