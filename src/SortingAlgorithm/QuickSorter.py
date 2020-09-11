from src.SortingAlgorithm.Sorter import Sorter

class QuickSorter(Sorter):

    def sort(self, collection, asc):
        self.quicksort(collection, 0, len(collection)-1, asc)
    
    def quicksort(self, collection, p, r, asc):
        if p < r:
            q = self.partition(collection, p, r, asc)
            self.quicksort(collection, p, q - 1, asc)
            self.quicksort(collection, q + 1, r, asc)

    def partition(self, collection, p, r, asc):
        x = collection[r]
        i = p - 1
        for j in range(p, r):
            if asc and collection[j] <= x:
                i = i + 1
                 #swap position
                temp = collection[j]
                collection[j] = collection[i]
                collection[i] = temp
            elif not asc and collection[j] > x:
                i = i + 1
                 #swap position
                temp = collection[j]
                collection[j] = collection[i]
                collection[i] = temp
        temp = collection[i+1]
        collection[i+1] = collection[r]
        collection[r] = temp
        return i+1



    