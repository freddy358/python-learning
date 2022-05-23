class Cat:
    def __init__(self, color, cat_type, size):
        self.color = color
        self.cat_type = cat_type


    def set_size(self):
        if self.cat_type == "indoor":
            self.size = "small"
        else:
            self.size = "undefined"

class Tiger(Cat):
    def __init__(self, color, cat_type, size):
        Cat.__init__(self, color, cat_type, size)

    def set_size(self):
        if self.cat_type == "wild":
            self.size = "big"
        else:
            self.size = "undefined"


shir = Tiger(color="sari", cat_type="wild", size=13)

print(shir.size)