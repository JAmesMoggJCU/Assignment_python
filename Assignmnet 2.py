from kivy.app import App
from kivy.lang import Builder

class ItemsForHire(App):
    def __init__(self, **kwargs):
        super(ItemsForHire, self). __init__(**kwargs)

    def build(self):
        self.title = 'Items For Hire'
        self.root = Builder.load_file('Assignment.kv')
        self.create_menu_buttons()
        return self.root

    def Hire_button (self):

    #def List_Item_Button (self):
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


    #def Add_New_Item_Button (self):

    #def Return_Item_Button (self):

    #def Continue_Button (self):
