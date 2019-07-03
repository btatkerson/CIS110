from graphics import*
import math

def main():
	print("This program allows the user to draw a line segment, then displays info")
	print("of the line segment")
	print("")


	win=GraphWin("Line Segment Info",400,400)
	win.setCoords(-10,-10,10,10)
	
	msg=Text(Point(0,-9.5),"Click on two points of a line segment.").draw(win)
	p1=win.getMouse()
	p1.draw(win)
	p2=win.getMouse()
	p2.draw(win)

	line=Line(p1,p2)
	line.draw(win)
	
	mark=Circle(line.getCenter(),0.15)
	mark.setFill('cyan')
	mark.draw(win)
	
	dx=p2.getX()-p1.getX()
	dy=p2.getY()-p1.getY()
	slope=float(dy/dx)
	length=math.sqrt(dx*dx+dy*dy)

	msg.setText("Length: "+str(round(length,2))+"  Slope:"+str(round(slope,2)))
	win.getMouse()
	win.close()
main()
