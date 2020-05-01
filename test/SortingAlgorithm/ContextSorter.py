from src.SortingAlgorithm.Sorter import Sorter
from src.SortingAlgorithm.SorterFactory import SorterFactory
import src.UtilitiesSingleton
import os

class SortingAlgorithmTester():

    def __init__(self):
        
        self.config = src.UtilitiesSingleton.ConfigParser().getConfigParser('{0}test{0}config.ini'.format(os.path.sep))
        self.logger = src.UtilitiesSingleton.Logger().getLogger(type(self).__name__)
        self.sf = SorterFactory()
    
    def integer_values_test(self):
        s = self.sf.getSorter(self.config.get('SortingAlgorithm','algorithm'))
        a = [31, 41, 59, 26, 41, 58, 70, 3, 7]
        s.sort(a, self.config.getboolean('SortingAlgorithm','asc_order'))
        self.logger.info(a)

sat = SortingAlgorithmTester()
sat.integer_values_test()