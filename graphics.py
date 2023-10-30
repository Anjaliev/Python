from shape.circle import *
from shape.rectangle import *
from shape.dgraphisc.cuboid import *
from shape.dgraphisc.sphere import *
r=int(input("Enter the radious of circle:"))
area_c(r)
peri_c(r)
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
area_r(l,b)
peri_r(l,b)
l=int(input("Enter the length of cuboid:"))
w=int(input("Enter the width of cuboid:"))
h=int(input("Enter the height of cuboid:"))
area_cu(l,w,h)
peri_cu(l,w,h)
r=int(input("Enter the radious of sphere:"))
area_s(r)
peri_s(r)
