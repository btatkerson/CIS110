from graphics import*
def main():
	print("This program displays 5 dice using graphics.py")
	print("")

	win=GraphWin("Dice",400,400)
	win.setBackground('LemonChiffon2')
	win.setCoords(0,0,20,20)
	
	#Dice 
	die=Polygon(Point(2,17),Point(4,16),Point(6,17),Point(6,15),Point(4,14),
		Point(4,16),Point(4,14),Point(2,15),Point(2,17),
		Point(4,18),Point(6,17),Point(4,16),Point(2,17),)
	die.setFill('red')
	die.setOutline('white')
	die.setWidth('2')
	die.draw(win)
	dx=0
	dy=0

	#cloing and moving dice
	for i in range(1,5):
		dx=dx+3
		dy=dy-3
		dice=die.clone()
		dice.draw(win)
		dice.move(dx,dy)
	
	#white spots
	spot=Circle(Point(4,17),.15)
	spot.setFill('white')
	spot.setOutline('white')
	spot.draw(win)	

	#list of posssible die positions
	diceList=[(-1.6,-.65),(-1.1,-1.4),(-.5,-2.2),(1.4,-1),(.6,-2),(2.3,-3),(3.7,-3),(2,-4.05),(2,-4.9),(1.5,-3.8),(2.5,-5.15),(1.5,-4.65),(2.5,-4.3),(3.4,-4.4),(4.5,-4.7),(4.4,-3.9),(3.5,-5.2),(5,-6),(5,-6),(6,-6),(7,-6),(6.5,-8),(7.5,-7),(4.5,-6.75),(4.5,-7.25),(4.5,-7.75),(5.5,-7.3),(5.5,-7.8),(5.5,-8.3),(10,-9),(8,-9),(9,-9.5),(9,-8.5),(8,-10.5),(10.5,-9.9),(9.5,-11.2),(11,-12),(13,-12),(12,-12),(12,-11.5),(12,-12.5),(11.1,-13.5),(12.4,-13.3),(12.4,-14.2),(13.6,12.7),(13.6,-13.6),(13.6,-12.7)]

	#loop to dupe the dot
	for i in range(len(diceList)):
		dx,dy=diceList[i]
		spots=spot.clone()
		spots.draw(win)
		spots.move(dx,dy)
	message=Text(Point(5,1),"Click anywhere to quit.")
	message.setFill('blue')
	message.draw(win)		
	win.getMouse()


main()

