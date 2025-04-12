import sys

class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name.lower()
        self.weight = weight
        self.price = price
        
    def __hash__(self):
        return hash((self.name, self.weight, self.price))
    
    def __eq__(self, other):
        if isinstance(other, ShopItem):
            return (self.name == other.name and 
                self.weight == other.weight and 
                self.price == other.price)
        else:
            return False

lst_in = list(map(str.strip, sys.stdin.readlines()))
shop_items = {}

for line in lst_in:
    name_part, data = line.split(':')
    name = name_part.strip()
    weight, price = map(float, data.strip().split())
    item = ShopItem(name, weight, price)
    if item in shop_items:
        shop_items[item][1] += 1
    else:
        shop_items[item] = [item, 1]