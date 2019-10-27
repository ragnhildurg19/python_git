class Item():
    def __init__(self, name="", category=""):
        self.name = name
        self.category = category

    def set_name(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category
    
    def __str__(self):
        item_str = "Name: {}, Category: {}".format(self.name, self.category)
        return item_str

class Catalog():
    def __init__(self, name, collection="", Item=None):
        self.name = name
        self.collection = collection
        if Item is None:
            self.collection = []
        else:
            self.collection = Item

    def add(self, Item):
        if Item not in self.collection:
            self.collection.append(Item)
    
    def remove(self, Item):
        if Item in self.collection:
            self.collection.remove(Item)
    
    def __str__(self):
        catalog_str = "Catalog Films: {}\n\t".format(self.collection)
        return catalog_str
