
newlist = []
in_file = open("items.csv", "r")

for line in in_file:
    item = line.strip().split(",")
    name = item[0]
    description = item[1]
    price = item[2]
    hired = item[3]

    newlist.append((item[0], item[1], item[2], item[3]))
in_file.close()
"""
input1 = str(input("please enter item name here:"))
input2 = str(input("please enter item description:"))
input3 = float(str(input("please enter item price: $")))
input4 = "in"
newlist.append((input1, input2, input3, input4))
#print(newlist)"""
"""t = ('275', '54000', '0.0', '5000.0', '0.0')
lst = list(t)
lst[0] = '300'
t = tuple(lst)
print(t)
list = [('1','2','3','4'),
        ('2','3','4','5'),
        ('3','4','5','6'),
        ('4','5','6','7')]
list = [l + (''.join(l),) for l in list]
print(list)"""

"""for item in newlist:
    print(item[0:3])"""


ItemToCheck = str(input("enter the name of an item"))

for i,item in enumerate(newlist):
    if item[0] == ItemToCheck:
       temp = list(newlist[i])
       temp[3] = "in"
       newlist[i]=tuple(temp)
print(newlist)


"""a=[(1,'Rach', 'Mell', '5.11', '160'),(2, 'steve', 'Rob', '6.1', '200'), (1,'Rach', 'Mell', '5.11', '160')]

for i,e in enumerate(a):
    if e[0]==2:
        temp=list(a[i])
        temp[2]='Roberto'
        a[i]=tuple(temp)


for hell in newlist:
    print(hell[0:])"""