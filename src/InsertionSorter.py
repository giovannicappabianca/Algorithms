from Sorter import Sorter

class InsertionSorter(Sorter):
    
    def sort(self, collection, asc):
        for j in range(1, len(collection)):
            key = collection[j]
            i = j - 1
            if asc: 
                condition = collection[i] > key
            else: 
                condition = collection[i] < key
            while i >= 0 and condition:
                collection[i+1] = collection[i]
                i = i - 1
                if asc: 
                    condition = collection[i] > key
                else: 
                    condition = collection[i] < key
            collection[i+1] = key

            
