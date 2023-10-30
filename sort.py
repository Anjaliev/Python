fruits={'Apple':2,
        'Orange':14,
        'Graps':10,
        'Pinapple':61}
print("Fruits:",fruits)
l=list(fruits.items())
l.sort()
print("Ascending order is:",l)
l=list(fruits.items())
l.sort(reverse=True)
print("Descending order is:",l)
