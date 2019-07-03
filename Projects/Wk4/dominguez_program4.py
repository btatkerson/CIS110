'''
Program Name:dominguez_program4.py
Program Description:This program creates an American Flag using graphics.py
Author:Daniel Dominguez
Date Created:6/11/19
Notes of Interest:none
'''
import time
from graphics import*

def main():
	#introduction
	print("This program creates an American Flag using graphics.py")
	print("")
	#Create the window and set dimensions to 500,300 with a black background
	win=GraphWin("American Flag",500,300)
	win.setCoords(0,0,475,250)
	win.setBackground('black')
	center=Point(237,125)

	#Creates the flag "canvas" (white background)
	canvas=Rectangle(Point(0,0),Point(475,250))
	canvas.setFill('white')
	canvas.draw(win)
	
	#Creates a red stripe
	redSt=Rectangle(Point(0,0),Point(475,18))
	redSt.setFill('red')
	redSt.draw(win)
	
	#Forloop that creates 7 red strips every 39 pixels
	dx=0
	dy=0
	for i in range(1,7):
		dy=dy+39
		newRedSt=redSt.clone()
		newRedSt.draw(win)
		newRedSt.move(dx,dy)

	#Creates the inner blue rectangle. (.75 was creating a distorted
	blueSq=Rectangle(Point(0,250),Point(205,118))
	blueSq.setFill('blue')
	blueSq.setOutline('black')
	blueSq.draw(win)
	center=(Point(102.5,184))


	#Creates a star without displaying it to the screen.
	poly1=Polygon(Point(0,15),Point(6,15),Point(7.5,20),Point(9,15),Point(15,15),
		Point(10,10),Point(13,5),Point(7.5,7),Point(2,5),Point(5,10))
	poly1.setFill('white')
	poly1.setOutline('black')

	#Here is a series of foor loops to create the star pattern using a 
	#list of x values with a static	y value.
	
	## (5)Six star rows:
	sixStarRow=[12,46,80,114,148,182]
	fiveStarRow=[30,64,98,132,166]

	for i in range(len(sixStarRow)):
		dx2=sixStarRow[i]
		dy2=122
		stars=poly1.clone()
		stars.draw(win)
		stars.move(dx2,dy2)
	for i in range(len(sixStarRow)):
		dx2=sixStarRow[i]
		dy2=147
		stars=poly1.clone()
		stars.draw(win)
		stars.move(dx2,dy2)
	for i in range(len(sixStarRow)):
		dx2=sixStarRow[i]
		dy2=172
		stars=poly1.clone()
		stars.draw(win)
		stars.move(dx2,dy2)
	for i in range(len(sixStarRow)):
		dx2=sixStarRow[i]
		dy2=197
		stars=poly1.clone()
		stars.draw(win)
		stars.move(dx2,dy2)
	for i in range(len(sixStarRow)):
		dx2=sixStarRow[i]
		dy2=222
		stars=poly1.clone()
		stars.draw(win)
		stars.move(dx2,dy2)

	## (4)5 Star rows
	for i in range(len(fiveStarRow)):
		dx3=fiveStarRow[i]
		dy3=135
		stars2=poly1.clone()
		stars2.draw(win)
		stars2.move(dx3,dy3)
	for i in range(len(fiveStarRow)):
		dx3=fiveStarRow[i]
		dy3=160
		stars2=poly1.clone()
		stars2.draw(win)
		stars2.move(dx3,dy3)
	for i in range(len(fiveStarRow)):
		dx3=fiveStarRow[i]
		dy3=185
		stars2=poly1.clone()
		stars2.draw(win)
		stars2.move(dx3,dy3)
	for i in range(len(fiveStarRow)):
		dx3=fiveStarRow[i]
		dy3=210
		stars2=poly1.clone()
		stars2.draw(win)
		stars2.move(dx3,dy3)



	#Wait for a mouse click and then close the program
	win.getMouse()
	win.close()

	#prints authors name, class and date.
	print("Daniel Dominguez")
	print("CIS110 Program 1")
	#Prints the current date and time using asctime()
	print(time.asctime(time.localtime(time.time())))
main()
