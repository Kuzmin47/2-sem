class NewList:
    def __init__(self, lst=None):
        self.lst = lst if lst is not None else []

    def __sub__(self, other):
        if isinstance(other, (list, NewList)):
            other_list = other.lst if isinstance(other, NewList) else other
            other_counts = {}
            for item in other_list:
                key = (item, type(item))
                other_counts[key] = other_counts.get(key, 0) + 1

                new_list = []
                temp_counts = other_counts.copy()

                for item in self.lst:
                    key = (item, type(item))
                    if key in temp_counts and temp_counts[key] > 0:
                        temp_counts[key] -=1
                    else:
                        new_list.append(item)
            return NewList(new_list)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, list):
            return NewList(other) - self
        return NotImplemented

    def get_list(self):
        return self.lst