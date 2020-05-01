from src.SortingAlgorithm.Sorter import Sorter

class BubbleSorter(Sorter):
    
    def sort(self, collection, asc):
        for i in range(1, len(collection)):
            for j in range (len(collection), i + 1, -1):
                if asc: 
                    condition =  collection[j] < collection[i]
                else:
                    condition =  collection[j] > collection[i]
                if condition:
                    #swap position
                    temp = collection[j]
                    collection[j] = collection[i]
                    collection[i] = temp

            
