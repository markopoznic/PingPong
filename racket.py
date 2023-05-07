from turtle import Turtle

class Racket(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.seth(90)
        self.shape('square')
        self.color('white')
        self.penup()
        self.setx(side)
        
         
    def moveUp(self):
        self.forward(10)
        

    def moveDown(self):
        self.back(10)
        
        
    

