import turtle


def drawBar(t, sbar):
	t.begin_fill()
	t.left(90)
	t.forward(sbar)
	t.write(str(sbar))
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(sbar)
	t.left(90)
	t.end_fill()

bars = [10, 11, 12, 13, 14, 10, 4, 2, 1]
border = 10
maxheight = max(bars)
numbars = len(bars)


screen = turtle.Screen()
screen.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
screen.bgcolor('pink')

dean = turtle.Turtle()
dean.color('green')

for a in bars:
	drawBar(dean, a)

screen.exitonclick()