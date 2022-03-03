
import turtle

class figure:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c
        
    def triangle(self):
        """
        à partir du point de coordonnées (x;y) et de côté c (points)"""
        turtle.down() #descend le stylo
        for i in range(4):
            turtle.forward(self.c)
            turtle.left(90)

    def ligne(self,x1,y1,x2,y2,n):
        dx = (x2-x1) / n
        dy = (y2-y1) / n
        y = y1
        x= x1 
        for i in range(n):
            turtle.up()
            turtle.goto(x,y)
            self.triangle()
            print(x,y)
            x += dx
            y += dy
    
    def symetrie_ligne(self,x1,y1,x2,y2,n):
        self.ligne(x1,y1,x2,y2,n)
        self.ligne(-x1,y1,-x2,y2,n)
        
    


triangle = figure(20,20,30)
triangle.symetrie_ligne(10,20,50,60,5)


