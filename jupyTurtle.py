from IPython.display import Markdown
from IPython import display
from math import cos, sin, pi

class Turtle:
    
    def __init__(self, height = 100, width = 100, size=0, debug = False):
        self.debug = debug
        
        # Display
        if (size != 0):
            self.height = size
            self.width = size
        else:
            self.height = height
            self.width = width
            
        self.elts = ""
        self.eltCount = 0
        self.frameId = 0
        self.preventRefresh = False
        
        # Turtle 
        self.turtlePos = [self.width / 2, self.height / 2]
        self.direction = 0
        self.drawColor = "#C4C4C4"
        self.penDown = True
        
    def __repr__(self):
        return self.toString()
    
    def __str__(self):
        return self.toString()
    
    def toString(self):
        eCount = str(self.eltCount) + " element(s)"
        if (self.eltCount > 100): eCount += " 🛑"
        elif (self.eltCount > 50): eCount += " ⚠"
        
        direction = {
            0: "East",
            1: "South",
            2: "West",
            3: "North",
            4: "East"
        }
        
        return """---------------------------------------------------------------------------
JupyTurtle Stats                                                     v0.0.1
        
Height: {height}px
Width: {width}px
EltCount: {eltCount}
FrameId: {frameId}
PreventRefresh: {preventRefresh}

TurtlePos: {turtlePos}
Direction: {orientation} ({direction})
PenDown: {penDown}
---------------------------------------------------------------------------""".format(
            height=self.height,
            width=self.width,
            turtlePos=self.turtlePos,
            eltCount=eCount,
            frameId=self.frameId,
            preventRefresh=self.preventRefresh,
            orientation=direction[round(self.direction / 90)],
            direction=round(self.direction, 2),
            penDown=self.penDown
        )
    
    def drawLine(self, startPos, endPos, color=None):
        if (color == None): color = self.drawColor
        self.elts += f"<line x1='{startPos[0]}' y1='{startPos[1]}' x2='{endPos[0]}' y2='{endPos[1]}' stroke='{color}' />"
        self.eltCount += 1
        if not self.preventRefresh: self.display()
            
    def setPreventRefresh(self, state):
        self.preventRefresh = state
    def setDebug(self, state):
        self.debug = state
    
    def forward(self, lenght):
        newPos = [
            self.turtlePos[0] + cos(self.direction * pi/180) * lenght,
            self.turtlePos[1] + sin(self.direction * pi/180) * lenght
        ]
        if (self.penDown): self.drawLine(self.turtlePos, newPos)
        self.turtlePos = newPos
        
    def backward(self, lenght):
        newPos = [
            self.turtlePos[0] - cos(self.direction * pi/180) * lenght,
            self.turtlePos[1] - sin(self.direction * pi/180) * lenght
        ]
        if (self.penDown): self.drawLine(self.turtlePos, newPos)
        self.turtlePos = newPos
        
    def pendown(self):
        self.penDown = True
        
    def penup(self):
        self.penDown = False
        
    def goto(self, pos):
        if (self.penDown): self.drawLine(self.turtlePos, pos)
        self.turtlePos = pos
    
    def rotate(self, rotation):
        self.direction = rotation % 360
    
    def left(self, amount):
        self.rotate(self.direction - amount)
        
    def right(self, amount):
        self.rotate(self.direction + amount)
        
    def color(self, color):
        self.drawColor = color
    
    def display(self):
        display.clear_output(wait=True)
        display.display(Markdown(
            "<style>svg {border: 1px solid #C4C4C4C4; width: "+str(self.width)+"px!important; height:"+str(self.height)+"px!important}</style>"+
            "<svg viewBox='0 0 "+str(self.width)+" "+str(self.height)+"' xmlns='http://www.w3.org/2000/svg'>"+
                self.elts+
            "</svg>"+
            ("<pre>"+self.toString()+"</pre>" if (self.debug) else "")
        ))
        self.frameId += 1
        
