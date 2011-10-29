# The code in this file was provided by Samir Talwar for us to build on at the workshop.
# His original code can be found here: http://github.com/SamirTalwar/Lists

class FunctionalList:

    @staticmethod
    def of(*items):
        def fromArray(items, start, end):
            if start == end:
                return Nil()
            else:
                return Cons(
                    items[start],
                    fromArray(items, start + 1, end)
                )

        return fromArray(items, 0, len(items))

    def map(self, mapping):
        if self.isEmpty():
            return Nil()
        else:
            return Cons(mapping(self.head), self.tail.map(mapping))


class Nil(FunctionalList):
    def isEmpty(self):
        return True

    def __str__(self):
        return 'Nil'

class Cons(FunctionalList):
    def __init__(self, head, tail):
        self._head = head
        self._tail = tail

    def __str__(self):
        return str(self._head) + ' ' + str(self._tail)

    def isEmpty(self):
        return False

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

