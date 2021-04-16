import turtle

def drawsquare(): 
    for myMoves in range(4):
        tess.forward(100)
        tess.left(360/4)
        
        
wn = turtle.Screen()

wn.bgcolor("white") 


tess = turtle.Turtle()
tess.color("hotpink")
        
for myMoves in range(2):
    drawsquare()
    tess.forward(50)
    tess.left(45)