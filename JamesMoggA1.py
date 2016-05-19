"""James Mogg, 21/03/2016, items for hire, https://github.com/JAmesMoggJCU/Assignment_python.git"""
"""
input item name string
    input item decription string
    input item price
    check for input in fields
   return to in file list
 return to menu
 """

def loading_items():
 input1 = str(input("please enter item name here:"))
 input2 = str(input("please enter item description:"))
 input3 = float(str(input("please enter item price: $")))
 input4 = "in"
 newlist.append((input1, input2, input3, input4))
 print(input1, input2, "$",input3, "now available for hire")
 return

"""open file list
    list the items available
    input number of item for hire
    return input to file list
    return to menu"""

def hiring_items():
    item_count = -1
    for list_print_hire in newlist:
        if len(list_print_hire[3]) != 3:
            item_count += 1
            print("{0} = {1} = ${2}".format(item_count, list_print_hire[0:2],list_print_hire[2]))

    ItemToCheck = str(input("enter the name of an item"))

    for i,item in enumerate(newlist):
        if item[0] == ItemToCheck:
            temp = list(newlist[i])
            temp[3] = "out"
            newlist[i]=tuple(temp)
    return
"""list items that need to be returned
get user wants to return
return the item to the list
"""

def returning_items():
    item_count = -1
    for list_print_hire in newlist:
        if len(list_print_hire[3]) == 3:
            item_count += 1
            print("{0} = {1} = ${2}*".format(item_count, list_print_hire[0:2],list_print_hire[2]))

    ItemToCheck = str(input("enter the name of an item"))

    for i,item in enumerate(newlist):
        if item[0] == ItemToCheck:
            temp = list(newlist[i])
            temp[3] = "in"
            newlist[i]=tuple(temp)
    return
#list of tuple for items refrenced
newlist = []
in_file = open("items.csv", "r")
#splits the data from the csv and creates it into a tuple
for line in in_file:
    item = line.strip().replace("","").split(",")
    name = item[0]
    description = item[1]
    price = item[2]
    hired = item[3]
    newlist.append((item[0], item[1], item[2], item[3]))

in_file.close()
# start of loop
user_input = str(input("(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd am item \n(Q)uit")).upper()

while user_input != "Q":
    if user_input == "L":
        #start list count at 0
        item_count = -1
        for list_print_list in newlist:
            #length of out is same so check for error
            if len(list_print_list[3]) == 3:
                item_count += 1
                #print the number then the name and description then price
                print("{0} = {1} = ${2} *".format(item_count, list_print_list[0:2],list_print_list[2]))
            else:
                item_count += 1
                print("{0} = {1} = ${2} ".format(item_count, list_print_list[0:2],list_print_list[2]))
    elif user_input == "H":
        hiring_items()
    elif user_input == "R":
        returning_items()
    elif user_input == "A":
        loading_items()
    else:
        print("Invalid")
    user_input = str(input("(L)ist all items \n(H)ire and item \n(R)eturn an item \n(A)dd am item \n(Q)uit")).upper()

#opens file and writes in the data that was collected during the user inputs
file_write = open("items.csv", "w")
for items in newlist:
    write = str(items)
    write.split("( )")
    print(write)
    file_write.write(write.strip("( )").replace("'","").strip() + "\n")
file_write.close()
print("have a nice day")