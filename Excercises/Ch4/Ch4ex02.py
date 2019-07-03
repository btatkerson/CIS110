from graphics import*
def main():
	print("This program displays an Archery Target usig graphics.py")
	print("")

	win=GraphWin("Archery Target",400,400)
	win.setCoords(-6,-6,6,6)
	center=Point(0,0)
	win.setBackground('grey')
	#White Circle	
	whiteCircle=Circle(center,5)
	whiteCircle.setFill('white')
	#Black Circle
	blackCircle=Circle(center,4)
	blackCircle.setFill('black')
	#Blue Circle
	blueCircle=Circle(center,3)
	blueCircle.setFill('blue')
	#Red Circle
	redCircle=Circle(center,2)
	redCircle.setFill('red')
	#Yellow Circle
	yellowCircle=Circle(center,1)
	yellowCircle.setFill('yellow')
	#Draw
	whiteCircle.draw(win)
	blackCircle.draw(win)
	blueCircle.draw(win)
	redCircle.draw(win)
	yellowCircle.draw(win)
	win.getMouse()
main()
