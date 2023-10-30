print("Rectangle!")
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
c=lambda x,y:x*y
print("Area of rectangle:"+str(c(l,b)))
print("Square!")
s=int(input("Enter the side:"))
c=lambda x:x*x
print("Area of square:"+str(c(s)))
print("Triangle!")
b=int(input("Enter the base:"))
h=int(input("Enter the heigth:"))
c=lambda x,y:0.5*x*y
print("Area of triangle:"+str(c(b,h)))
