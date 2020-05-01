from src.SortingAlgorithm.Sorter import Sorter
from src.SortingAlgorithm.InsertionSorter import InsertionSorter
from src.SortingAlgorithm.MergeSorter import MergeSorter

class SorterFactory:

    def __init__(self):
        self.algorithms ={}
        self.algorithms['InsertionSort'] = InsertionSorter()
        self.algorithms['MergeSort'] = MergeSorter()
        self.algorithms['BubbleSort'] = MergeSorter()


    def getSorter(self, algorithm) -> Sorter:
        return self.algorithms[algorithm]



