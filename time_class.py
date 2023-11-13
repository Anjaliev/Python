class Time:
    def __init__(self, h, m, s):
        self.h1 = h
        self.m1 = m
        self.s1 = s
    def __add__(self, t):
        sum1 = self.h1 + t.h1
        sum2 = self.m1 + t.m1
        sum3 = self.s1 + t.s1
        if sum3 >= 60:
            sum3 = sum3 - 60
            sum2 =sum2 + 1
        if sum2 >= 60:
            sum2 = sum2 - 60
            sum1 = sum1 + 1
        print(sum1, ":", sum2,":", sum3);

print("TIME 1")
h1 = int(input("Enter the hour in time1:"))
m1 = int(input("Enter the minute in time1:"))
s1 = int(input("Enter the second in time1:"))
t1 = Time(h1, m1, s1)
print("TIME 2")
h2 = int(input("Enter the hour in time2:"))

m2 = int(input("Enter the minute in time2:"))
s2 = int(input("Enter the second in time2:"))
t2 = Time(h2, m2, s2)
print("The sum of both time=")
t1 + t2

