from graphics import*
import math

def main():
	print("This program computes the intersection")
	print("of a circle and a borizontal line")
	print("")

	r=float(input("Enter the radius of the circle: "))
	yi=float(input("Enter the y-inctercept of the line: "))

	win=GraphWin("Circle Intersection")
	win.setCoords(-10,-10,10,10)
	
	Circle(Point(0,0),r).draw(win)
	Line(Point(-10,yi),Point(10,yi)).draw(win)

	x=math.sqrt(r*r-yi*yi)
	print("x values of intersection are", -x,x)
	
	p1=Circle(Point(x,yi),0.25)
	p1.setOutline('red')
	p1.setFill('red')
	p1.draw(win)

	p2=p1.clone()
	p2.move(-2*x,0)
	p2.draw(win)
	
	win.getMouse()
main()
