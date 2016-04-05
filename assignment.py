"""James Mogg, 21/03/2016, items for hire"""
"""input item name string
    input item decription string
    input item price
    check for input in fields
   return to in file list
 return to menu"""

def loading_items(load):
    
    return

"""open file list
    list the items available
    input number of item for hire
    return input to file list
    return to menu"""

def hiring_items (hire):
    return
newlist = []
in_file = open("items.csv", "r")

for line in in_file:
    item = line.strip().split(",")
    name = item[0]
    description = item[1]
    price = item[2]
    hired = item[3]
newlist.append((item[0], item[1], item[2], item[3]))

user_input = str(input("(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd am item \n (Q)uit")).upper()

while user_input != "Q":
    if user_input == "L":
        print("you chose List")
    elif user_input == "H":
        print("you chose hire")
    elif user_input == "R":
        print("you chose return")
    elif user_input == "A":
        print("you chose add")
    else:
        print("Invalid")
    user_input = str(input("(L)ist all items \n(H)ire and item \n(R)eturn an item \n(A)dd am item \n (Q)uit")).upper()