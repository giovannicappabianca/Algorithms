from src.SortingAlgorithm.Sorter import Sorter
from src.SortingAlgorithm.InsertionSorter import InsertionSorter

class SorterFactory:

    def __init__(self):
        self.algorithms ={}
        self.algorithms['InsertionSort'] = InsertionSorter()

    def getSorter(self, algorithm) -> Sorter:
        return self.algorithms[algorithm]



