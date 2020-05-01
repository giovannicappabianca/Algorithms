import math
from src.SortingAlgorithm.Sorter import Sorter

class MergeSorter(Sorter):
    
    def sort(self, collection, asc):
        if asc:
            self._mergesort(collection, 0, len(collection)-1)
        else:
            self._mergesort_desc(collection, 0, len(collection)-1)
        
    
    
    def _mergesort(self, collection, p, r):
        if p < r:
            q = math.floor((r+p)/2)
            self._mergesort(collection, p, q)
            self._mergesort(collection, q+1, r)
            self._merge_asc(collection, p, q, r)


    def _merge_asc(self, collection, p, q, r):
        left = collection[p:q+1]
        right = collection[q+1:r+1]
        i = 0
        j = 0
        k = p
        while k < r and i < (q - p + 1) and j < (r - q):
            if(left[i] < right[j]):
                collection[k]=left[i]
                i = i + 1
            else:
                collection[k]=right[j]
                j = j + 1
            k = k + 1
        #in order to insert in collection the remaining left and right elements
        while i < (q-p+1):
            collection[k] = left[i]
            i = i + 1
            k = k+1
        while j < (r-q):
            collection[k] = right[j]
            j = j + 1
            k = k+1

    def _mergesort_desc(self, collection, p, r):
        if p < r:
            q = math.floor((r+p)/2)
            self._mergesort_desc(collection, p, q)
            self._mergesort_desc(collection, q+1, r)
            self._merge_desc(collection, p, q, r)


    def _merge_desc(self, collection, p, q, r):
        left = collection[p:q+1]
        right = collection[q+1:r+1]
        i = 0
        j = 0
        k = p
        while k < r and i < (q - p + 1) and j < (r - q):
            if(left[i] > right[j]):
                collection[k] = left[i]
                i = i + 1
            else:
                collection[k]=right[j]
                j = j + 1
            k = k + 1
        #in order to insert in collection the remaining left and right elements
        while i < (q-p+1):
            collection[k] = left[i]
            i = i + 1
            k = k+1
        while j < (r-q):
            collection[k] = right[j]
            j = j + 1
            k = k+1