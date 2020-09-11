from src.SortingAlgorithm.Sorter import Sorter
from src.SortingAlgorithm.InsertionSorter import InsertionSorter
from src.SortingAlgorithm.MergeSorter import MergeSorter
from src.SortingAlgorithm.BubbleSorter import BubbleSorter
from src.SortingAlgorithm.HeapSorter import HeapSorter
from src.SortingAlgorithm.QuickSorter import QuickSorter
import src.UtilitiesSingleton

class SorterFactory:

    def __init__(self):
        self.logger = src.UtilitiesSingleton.Logger().getLogger(type(self).__name__)

        self.algorithms ={}
        self.algorithms['insertionsort'] = InsertionSorter()
        self.algorithms['mergesort'] = MergeSorter()
        self.algorithms['bubblesort'] = BubbleSorter()
        self.algorithms['heapsort'] = HeapSorter()
        self.algorithms['quicksort'] = QuickSorter()



    def getSorter(self, algorithm) -> Sorter:
        self.logger.info('Selected {0} algorithm'.format(algorithm))
        return self.algorithms[algorithm.lower()]



