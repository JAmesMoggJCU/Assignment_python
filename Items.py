class Item:
    def __init__(self, name="defualt item", description="defualt description", price=0, in_out="in"):
        self.name = name
        self.description = description
        self.price = price
        self.in_out = in_out

    def __str__(self):
        return "{} {} ${} {}".format(self.name, self.description, self.price, self.in_out)
