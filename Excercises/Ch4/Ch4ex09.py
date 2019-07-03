from graphics import*
import math

def main():
	print("This program allows the user to draw a Rectangle using two inputs(mouse clicks)")
	print("of the line segment")
	print("")


	win=GraphWin("Rectangle Info",500,500)
	win.setCoords(0,0,10,10)
	
	msg=Text(Point(5,1),"Click on opposite corners of a rectangle.").draw(win)
	p1=win.getMouse()
	p1.draw(win)
	p2=win.getMouse()
	p2.draw(win)

	rect=Rectangle(p1,p2)
	rect.setWidth(2)
	rect.draw(win)
	

	length=abs(p2.getX()-p1.getX())
	height=abs(p2.getY()-p1.getY())

	area=length*height
	perimeter=2*(length+height)

	msg.setText("The perimeter is "+str(perimeter))
	Text(Point(5,.5),"The area is "+str(area)).draw(win)
	win.getMouse()
	win.close()
main()
