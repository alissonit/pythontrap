#CONSTRUINDO UMA CLASSE ITERATOR
class GenItem(object):
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if self.first > self.last:
            raise StopIteration
        else:
            self.first += 1
            return self.first - 1

n_list = GenItem(1,10)    
print(list(n_list))