class shape:
    def noshape(self):
        print("Shape has not specified")
class rectangle(shape):
    def threesides(self):
        print("This is rectangular shape")
class circle(rectangle):
    def nosides(self):
        print("This is circular shape")
c=circle()
c.noshape()
c.threesides()
c.nosides()