class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []
    
    @property
    def total_weight(self):
        return sum(thing.weight for thing in self.__things)

    def add_thing(self, thing):
        if self.total_weight + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.__things.append(thing)

    def __check_index(self, index):
        if not (0 <= index < len(self.__things)):
            raise IndexError('неверный индекс')

    def __getitem__(self, index):
        self.__check_index(index)
        return self.__things[index]
    
    def __setitem__(self, index, thing):
        self.__check_index(index)
        new_weight = self.total_weight - self.__things[index].weight + thing.weight
        if new_weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.__things[index] = thing
    
    def __delitem__(self, index):
        self.__check_index(index)
        del self.__things[index]