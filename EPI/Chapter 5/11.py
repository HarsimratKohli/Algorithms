class Rectangle():

    def __init__(self,X,Y,width,height):
        self.x=X
        self.y=Y
        self.width=width
        self.height=height

r1 = Rectangle(0,0,1,2)
r2 = Rectangle(0,0,2,1)

def isIntersect(r1,r2):

    return r1.x<=r2.x+r2.width and r1.x + r1.width >= r2.x and r1.y<=r2.y+r2.height and r1.y + r1.height >= r2.height


def IntersectRectangle(r1,r2):
    x= max(r1.x,r2.x)
    y= max(r1.y,r2.y)
    w = min(r1.x+r1.width , r2.x+r2.width) - max(r1.x,r2.x)
    y = min(r1.y+r1.height , r2.y+r2.height) - max(r1.y,r2.y)
    if isIntersect(r1,r2):
        print("Intersect")
        x= max(r1.x,r2.x)
        y= max(r1.y,r2.y)
        w = min(r1.x+r1.width , r2.x+r2.width) - max(r1.x,r2.x)
        h = min(r1.y+r1.height , r2.y+r2.height) - max(r1.y,r2.y)
        return Rectangle(x,y,w,h)

    return Rectangle(0,0,-1,-1)

print(IntersectRectangle(r1,r2).height)
