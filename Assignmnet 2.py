from kivy.app import App
from kivy.lang import Builder
from ItemList import Item_Lists
from kivy.uix.button import Button
from Items import Item

class ItemsForHireApp(App):

    """def __init__(self, **kwargs):

        super(ItemsForHireApp, self).__init__(**kwargs)
        self.items_list = []
        in_file = open("items.csv", "r")
        for line in in_file:
            item_match = line.strip().replace(" ", "").split(",")
            name = item_match[0]
            description = item_match[1]
            price = item_match[2]

            self.items_list.append((item_match[0], item_match[1], item_match[2]))"""

    def build(self):
        # Window.size = (350, 700)
        self.itemlisting = Item_Lists("items.csv")
        self.title = "Items For Hire"
        self.root = Builder.load_file('Assignment.kv')
        self.list_buttons()
        return self.root

    def press_add(self):
        self.root.ids.popup.open()

    def press_cancel(self):
        self.root.ids.popup.dismiss()

    def press_save(self):
        self.root.ids.popup.dismiss()

    def list_buttons(self):
        for printing_items in self.itemlisting.item_list:
            if printing_items.in_out == "out":
                item_button = Button(text=printing_items.name)
                item_button.background_color = (1,0,0,1)
                self.root.ids.entriesBox.add_widget(item_button)
            else:
                item_button = Button(text=printing_items.name)
                item_button.background_color = (1,1,0,1)
                self.root.ids.entriesBox.add_widget(item_button)

    def save_item(self, Item_Name, Item_Description, Item_Price):
        self.itemlisting.item_list.append(Item(Item_Name, Item_Description, Item_Price, "in"))
        item_button = Button(text=Item_Name)
        item_button.background_color = (1,1,0,1)
        self.root.ids.entriesBox.add_widget(item_button)
        self.root.ids.popup.dismiss()


    def show_all_items(self):
        # this is the function that prints all items in the list
        #print("All items on file (* indicates item is currently out):")
        #item_count_number = -1
        """for printing_items in self.itemlisting.item_list:
            print(printing_items)
            if len(printing_items[3]) == 3:
                item_count_number += 1
                print("{0} = {1} = ${2} *".format(item_count_number, printing_items[0:2], printing_items[2]))
            else:
                item_count_number += 1
                print("{0} = {1} = ${2}".format(item_count_number, printing_items[0:2], printing_items[2]))"""


ItemsForHireApp().run()
