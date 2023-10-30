from statistics import mean
from math import pi
from time import time,ctime
seconds=time()
print("The value of pi=",pi)
print("Epoch time=",seconds)
print("Local time=",ctime(seconds))
print("The average of list value=",end=" ")
print(mean([1,2,3,3,2,2,2]))