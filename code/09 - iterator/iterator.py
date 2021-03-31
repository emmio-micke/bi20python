class reverse_iter:
    def __init__(self, list):
        self.list = list

    def __iter__(self):
        self.index = len(self.list)
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            value = self.list[self.index]
            return value
        else:
            raise StopIteration


it = reverse_iter([1, 2, 3, 4])
myiter = iter(it)

for x in myiter:
    print(x)
