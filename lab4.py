'''
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
	def make_sound(self):
		print(self.sound*3)
a = Animal("whoof ", "Cookie" , 2, "red")
a.eat("bone")
a.description()
a.make_sound()
'''

class Person(object):
	def __init__(self,name,age,city,gender,fav_food,sport):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
		self.fav_food = fav_food
		self.sport = sport
	def eat_lunch(self):
		print("Abed, can we have " + self.fav_food + " ,pleaseeeeeeeeeeeeee")
	def play_sport(self):
		print("I am playing" + self.sport)
b = Person("stormi",15,"Jerusalem","Female","sushi"," soccer")
b.eat_lunch()
b.play_sport()

class song(object):
	def __init__(self,lyrics,sing_a_song):
		self.sing_a_song = song
		self.lyrics = lyrics
	def song(self):
		print('this is song' + str(self.sing_a_song) + ',is my favorite')
song_1 = ["I have these Lucid dreams", "where I can't hear a thing", "i know that you want me dead."]
song = song(song_1,"lucid dreams")

song.song()