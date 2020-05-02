from src.SortingAlgorithm.Sorter import Sorter
from src.SortingAlgorithm.InsertionSorter import InsertionSorter
from src.SortingAlgorithm.MergeSorter import MergeSorter
from src.SortingAlgorithm.BubbleSorter import BubbleSorter
from src.SortingAlgorithm.HeapSorter import HeapSorter
import src.UtilitiesSingleton

class SorterFactory:

    def __init__(self):
        self.logger = src.UtilitiesSingleton.Logger().getLogger(type(self).__name__)

        self.algorithms ={}
        self.algorithms['InsertionSort'] = InsertionSorter()
        self.algorithms['MergeSort'] = MergeSorter()
        self.algorithms['BubbleSort'] = BubbleSorter()
        self.algorithms['HeapSort'] = HeapSorter()


    def getSorter(self, algorithm) -> Sorter:
        self.logger.info('Selected {0} algorithm'.format(algorithm))
        return self.algorithms[algorithm]



