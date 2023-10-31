class rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        self.arear=self.l*self.b
    def perimeter(self):
        self.peri=(2*(self.l+self.b))
    def compare(self,r2):
        if self.arear==r2.arear:
            print("Area are equal!")
        elif self.arear>r2.arear:
            print("Area of 1st rectangle is greater!")
        else:
            print("Area of 2nd rectangle is greater!")
    def display(self):
        print("Area of rectangle=",self.arear)
        print("Perimeter of the rectangle=",self.peri)
l1=int(input("Enter the length of the 1st rectangle:"))
b1=int(input("Enter the breadth of the 1st rectangle:"))
l2=int(input("Enter the length of 2nd rectangle:"))
b2=int(input("Enter the breadth of 2nd rectangle:"))
r1=rect(l1,b1)
r2=rect(l2,b2)
r1.area()
r1.perimeter()
r2.area()
r2.perimeter()
r1.display()
r2.display()
r1.compare(r2)