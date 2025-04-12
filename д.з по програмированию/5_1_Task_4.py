class WordString:
    def __init__(self, string=""):
        self.__string = string

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value
        
    def __len__(self):
        return len(self.string.split())

    def __call__(self, indx):
        words = self.string.split()
        if 0 <= indx < len(words):
            return words[indx]
        return ""