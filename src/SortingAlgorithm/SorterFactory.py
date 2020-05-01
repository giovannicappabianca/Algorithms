from src.SortingAlgorithm.Sorter import Sorter
from src.SortingAlgorithm.InsertionSorter import InsertionSorter
from src.SortingAlgorithm.MergeSorter import MergeSorter
import src.UtilitiesSingleton

class SorterFactory:

    def __init__(self):
        self.logger = src.UtilitiesSingleton.Logger().getLogger(type(self).__name__)

        self.algorithms ={}
        self.algorithms['InsertionSort'] = InsertionSorter()
        self.algorithms['MergeSort'] = MergeSorter()
        self.algorithms['BubbleSort'] = MergeSorter()
        self.algorithms['HeapSort'] = MergeSorter()


    def getSorter(self, algorithm) -> Sorter:
        self.logger.info('Selected {0} algorithm'.format(algorithm))
        return self.algorithms[algorithm]



