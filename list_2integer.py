list1=[23,86,85,37]
list2=[87,65,85,20,6]
print("List 1:",list1)
print("List 2:",list2)
print("Length of List 1=",len(list1))
print("Length of List 2=",len(list2))
if len(list1)==len(list2):
    print("Length of two list are same!")
else:
    print("Length of two list are not same!")
print("Sum of List 1=",sum(list1))
print("Sum of List 2=",sum(list2))
if sum(list1)==sum(list2):
    print('Sum of two list are same!')
else:
    print("Sum of two list are not same!")
check=any(item in list1 for item in list2)
print("any value occure in both:",check)