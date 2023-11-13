class rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        self.area=self.l*self.b
    def __lt__(self, r):
        if self.area<r2.area:
            print("Area of 2nd rectangle is greater!")
        else:
            print("Area of 1st rectangle is greater!")
    def display(self):
        print("Area of rectangle=",self.area)
l=int(input("Enter the length of the 1st rectangle:"))
b=int(input("Enter the breadth of the 1st rectangle:"))
r1=rect(l,b)
l=int(input("Enter the length of 2nd rectangle:"))
b=int(input("Enter the breadth of 2nd rectangle:"))
r2=rect(l,b)
r1.area()
r1.display()
r2.area()
r2.display()
r1<r2