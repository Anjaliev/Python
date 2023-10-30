string=input("Enter the string:")
if len(string)>=3:
    string+='ly' if string.endswith('ing')else 'ing'
print(string)
