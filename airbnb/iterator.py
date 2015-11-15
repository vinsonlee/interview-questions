#!/usr/bin/env python

# Given an array of arrays, implement an iterator class to allow the client
# to traverse and remove elements in the array list. This iterator should
# provide three public class member functions:
#
# boolean has_next()
#  return true or false if there is another element in the set
#
# int next()
#   return the value of the next element in the array
#
# void remove()
#   remove the last element returned by the iterator.
#   That is, remove the element that the previous next() returned
#
# Given:  [[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]]
# Print:  1 2 3 4 5 6 7 8 9 10
#
# it = new Iterator(arr)
# while(it.has_next())
#     print(it.next() + " ")


class Iterator:
    def __init__(self, array):
        self.array = array
        self.prev_i = None
        self.prev_j = None
        self.next_i = None
        self.next_j = None

        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                self.next_i = i
                self.next_j = j
                break

            if self.next_i:
                break

    def has_next(self):
        if self.next_i:
            return True
        else:
            return False

    def next(self):
        item = self.array[self.next_i][self.next_j]

        i = self.next_i
        j = self.next_j

        while True:
            # Advance indexes by 1.
            j += 1
            if len(self.array[i]) <= j:
                i += 1
                j = 0

            # Check that end of array is passed.
            if i >= len(self.array):
                i = None
                j = None
                break

            # Check that array has more elements.
            if len(self.array[i]) > 0:
                break

        self.prev_i = self.next_i
        self.prev_j = self.next_j
        self.next_i = i
        self.next_j = j
        return item

    # XXX - The indexes need to be fixed up after removing an element.
    def remove(self):
        if self.prev_i:
            del self.array[self.prev_i][self.prev_j]
            self.prev_i = None
            self.prev_j = None

if __name__ == '__main__':
    array = [[], [1, 2, 3], [4, 5], [], [], [6], [7, 8], [], [9], [10], []]
    it = Iterator(array)
    while it.has_next():
        print it.next(),
    print

    array = []
    it = Iterator(array)
    while it.has_next():
        print it.next(),

    array = [[], [], []]
    while it.has_next():
        print it.next(),

    array = [[], [1, 2, 3], [4, 5], [], [], [6], [7, 8], [], [9], [10], []]
    it = Iterator(array)
    print array
    print it.next(),
    print it.next()
    it.remove()
    print array
    print it.next(),
    print it.next()
    it.remove()
    print array
