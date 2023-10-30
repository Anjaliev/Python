s=str(input("Enter a string:"))
firstchar=s[0]
s=s.replace(firstchar,'$')
s=firstchar+s[1:]
print(s)