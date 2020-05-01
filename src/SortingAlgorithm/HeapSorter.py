import math
from src.SortingAlgorithm.Sorter import Sorter

class HeapSorter(Sorter):
    
    def sort(self, collection, asc):
        if asc:
            self.build_max_heap(collection)
            size_collection = len(collection)-1
            for i in range(size_collection, 1, -1):
                temp = collection[0]
                collection[0] = collection[i]
                collection[i] = temp
                collection.pop()
                self.max_heapify(collection, i)
        else:
            self.build_min_heap(collection)
            size_collection = len(collection)-1
            for i in range(size_collection, 1, -1):
                temp = collection[0]
                collection[0] = collection[i]
                collection[i] = temp
                collection.pop()
                self.min_heapify(collection, i)


    def max_heapify(self, collection, i):
        l = self._left(i)
        r = self._right(i)
        if l <= len(collection) and collection[l] > collection[i]:
            largest = l
        else:
            largest = i
        if r <= len(collection) and collection[r] > collection[largest]:
            largest = r
        if largest <> i:
            temp = collection[i]
            collection[i] = collection[largest]
            collection[largest] = temp
            self.max_heapify(collection[largest])

    def build_max_heap(self, collection):
        for i in range(math.floor(len(collection)-1), 0, -1):
            self.max_heapify(collection, i)

    def min_heapify(self, collection, i):
        l = self._left(i)
        r = self._right(i)
        if l <= len(collection) and collection[l] < collection[i]:
            lowest = l
        else:
            lowest = i
        if r <= len(collection) and collection[r] < collection[lowest]:
            lowest = r
        if lowest <> i:
            temp = collection[i]
            collection[i] = collection[lowest]
            collection[lowest] = temp
            self.min_heapify(collection[lowest])

    def build_min_heap(self, collection):
        for i in range(math.floor(len(collection)-1), 0, -1):
            self.min_heapify(collection, i)


    def _parent(self, i):
        return math.floor(i/2)

    def _right(self, i):
        return 2*i

    def _left(self, i):
        return 2*i + 1 
    
   