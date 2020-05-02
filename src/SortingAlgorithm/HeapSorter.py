import math
from src.SortingAlgorithm.Sorter import Sorter

class HeapSorter(Sorter):
    
    def sort(self, collection, asc):
        heapstructure = _Heapstructure(collection)
        if asc:
            self.build_max_heap(heapstructure)
            for i in range(heapstructure.heapsize, 0, -1):
                temp = heapstructure.get(0)
                heapstructure.set(0, heapstructure.get(i))
                heapstructure.set(i, temp)
                heapstructure.heapsize = heapstructure.heapsize - 1
                self.max_heapify(heapstructure, 0)
        else:
            self.build_min_heap(collection)
            size_collection = len(collection)-1
            for i in range(size_collection, 1, -1):
                temp = collection[0]
                collection[0] = collection[i]
                collection[i] = temp
                collection.pop()
                self.min_heapify(collection, i)


    def max_heapify(self, heapstructure, i):
        l = self._left(i)
        r = self._right(i)
        if l <= heapstructure.heapsize and heapstructure.get(l) > heapstructure.get(i):
            largest = l
        else:
            largest = i
        if r <= heapstructure.heapsize and heapstructure.get(r) > heapstructure.get(largest):
            largest = r
        if largest != i:
            temp = heapstructure.get(i)
            heapstructure.set(i, heapstructure.get(largest))
            heapstructure.set(largest, temp)
            self.max_heapify(heapstructure, largest)

    def build_max_heap(self, heapstructure):
        for i in range(math.floor((heapstructure.heapsize)/2), -1, -1):
            self.max_heapify(heapstructure, i)

    def min_heapify(self, collection, i):
        l = self._left(i)
        r = self._right(i)
        if l <= len(collection) and collection[l] < collection[i]:
            lowest = l
        else:
            lowest = i
        if r <= len(collection) and collection[r] < collection[lowest]:
            lowest = r
        if lowest != i:
            temp = collection[i]
            collection[i] = collection[lowest]
            collection[lowest] = temp
            self.min_heapify(collection[lowest])

    def build_min_heap(self, collection):
        for i in range(math.floor(len(collection)-1), 0, -1):
            self.min_heapify(collection, i)


    def _parent(self, i):
        return math.floor((i-1)/2)

    def _right(self, i):
        return 2*i+2

    def _left(self, i):
        return 2*i+1 
    
class _Heapstructure():

    def __init__(self, collection):
        self.collection = collection
        self.heapsize = len(collection)-1
    
    def get(self, i):
        return self.collection[i]
    
    def set(self, i, value):
        self.collection[i] = value
    
    