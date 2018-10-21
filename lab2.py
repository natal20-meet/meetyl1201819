import tkinter as tk 
from tkinter import simpledialog
a = [1,2,3,4,5]
def make_list ():
	x = [a[0], a[4]]
	print (x)

#make_list()

b = [-2,-1,0,1,2,3,4,5,6,7,8,9]
def values_less_5(x): 
	for number in b:
		if number <=5:
			print(number)
num_list2 = []

#values_less_5(b) 
c = [2,4,6,8,10,12,14,16,18]
d = [2,6,10,14,18]
for y in c:
	for x in d:
		if y == x:
			num_list2.append(y)
#print(num_list2)

print("write a number")

answer = simpledialog.askstring("Input", "write a number",parent=tk.Tk())
answer = int(answer)
if answer%2 == 0:
	print (str(answer) + "is a prime number")



		

