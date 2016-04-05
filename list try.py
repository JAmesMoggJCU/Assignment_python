
newlist = []
in_file = open("items.csv", "r")

for line in in_file:
    item = line.strip().split(",")
    name = item[0]
    description = item[1]
    price = item[2]
    hired = item[3]
newlist.append((item[0], item[1], item[2], item[3]))
list(item[3])
for newlist in item[3]:
    if item[3] = "out"

in_file.close()
print(newlist)

