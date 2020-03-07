from Sorter import Sorter

class InsertionSorter(Sorter):
    
    def sort(self, collection):
        for j in range(1, len(collection)-1):
            key = collection[j]
            i = j - 1
            while i >= 0 and collection[i] > key:
                collection[i+1] = collection[i]
                i = i - 1
            collection[i+1] = key

            
