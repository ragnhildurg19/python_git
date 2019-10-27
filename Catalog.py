'''Í þessu verkefni eigið þið að útfæra tvo klasa Item og Catalog.  Báðir klasar eiga að vera í skránni catalog.py

Item hefur tvær "private" tilvikabreytur (e. instance variables), name og category. 
Catalog hefur tvær "private" tilvikabreytur, name og collection.
Catalog heldur utan um safn (e. collection) af Item.
Bæði Item og Catalog útfæra nokkrar tilvikaaðgerðir (e. instance methods).  
Þið eigið að geta fundið út hvaða aðgerðir (e. methods) eru nauðsynlegar með því að skoða eftirfarandi aðalforrit og úttak þess:

Athugið að þegar þegar einstök item tiltekins catalog eru prentuð út þá er einn tab-character í upphafi línunnar.'''

class Item():
    def __init__(self, name="", category=""):
        self.__name = name
        self.__category = category
    
    def get_name(self):
        '''Return the private variable'''
        # Only this class can read the private variable
        # so we return it to use it in another class
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_category(self, category):
        self.__category = category
    
    def __str__(self):
        item_str = "Name: {}, Category: {}".format(self.__name, self.__category)
        return item_str

class Catalog():
    def __init__(self, name=""):
        self.__name = name
        self.__collection = []

    def add(self, item):
        self.__collection.append(item)
    
    def remove(self, remove_item):
        self.__collection.remove(remove_item)
    
    def __str__(self):
        catalog_str = "Catalog Films: {}\n\t".format(self.__collection)
        return catalog_str

item1 = Item("Green Book", "Biography")
print(item1)

item2 = Item("The God", "Crime")
print(item2)
item2.set_name("The Godfather")
print(item2)

item3 = Item("Schindler's List", "Biography")
print(item3)
item3.set_category("Drama")
print(item3)

catalog = Catalog('Films')
print(catalog)
catalog.add(item1)
#catalog.add(item2)
#catalog.add(item3)
print(catalog)

#catalog.remove(item2)
#print(catalog)

#catalog.set_name("Favorite Movies")
#print(catalog)

#print(catalog.find_item_by_name("Green Book"))
#print(catalog.find_item_by_name("The Godfather"))

#catalog.clear()
#print(catalog)
