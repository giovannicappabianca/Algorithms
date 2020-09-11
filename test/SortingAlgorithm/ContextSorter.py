from src.SortingAlgorithm.Sorter import Sorter
from src.SortingAlgorithm.SorterFactory import SorterFactory
import InputTester_pb2 as InputTester_pb2

import src.UtilitiesSingleton
import os

class SortingAlgorithmTester():

    def __init__(self):
        
        self.config = src.UtilitiesSingleton.ConfigParser().getConfigParser('{0}test{0}config.ini'.format(os.path.sep))
        self.logger = src.UtilitiesSingleton.Logger().getLogger(type(self).__name__)
        self.sf = SorterFactory()
        self.it = None
        '''if os.path.exists(filename):
            with open(filename, "rb") as f:
                self.it = InputTester_pb2.InputTest().FromString(f.read())'''
               

    
    def integer_values_test_from_config_file(self):
        if self.it is None:
            algorithm = self.config.get('SortingAlgorithm','algorithm')
            order = self.config.getboolean('SortingAlgorithm','asc_order')
            a = [31, 41, 59, 26, 41, 58, 70, 3, 7]
        else:
            algorithm = self.it.sortingAlgorithm
            order = self.it.is_asc
            a = self.it.input_list
        s = self.sf.getSorter(algorithm)
        s.sort(a, order)
        self.logger.info(a)
        i = 1
        wrong = False
        while i < len(a) and not(wrong):
            if a[i-1] > a[i]:
                wrong = True
            i = i + 1
        if wrong : self.logger.error("sorting did not work as expected. Check result")
        

    def createInstanceTestFile(self, filename):

        testInstance = InputTester_pb2.InputTest()
        testInstance.sortingAlgorithm = InputTester_pb2.BUBBLESORT
        testInstance.is_asc=True
        testInstance.input_list.extend([31, 41, 59, 26, 41, 58, 70, 3, 7])

        with open(filename, "wb") as f:
            self.logger.info("created instance")
            bytesAsString = testInstance.SerializeToString()
            f.write(bytesAsString)

    def integer_values_test_with_protobuf(self, filename):
        
        with open(filename, "rb") as f:
            testInstance = InputTester_pb2.InputTest().FromString(f.read())
        
        s = self.sf.getSorter(InputTester_pb2.SortingAlgorithm.Name(testInstance.sortingAlgorithm))
        a = testInstance.input_list

        self.logger.info('before sorting {}'.format(a))
        s.sort(a, testInstance.is_asc)
        self.logger.info('after: {}'.format(a))
        i = 1
        wrong = False
        while i < len(a) and not(wrong):
            if a[i-1] > a[i]:
                wrong = True
            i = i + 1
        if wrong : self.logger.error("sorting did not work as expected. Check result")

filename = "instanceTest.bin"
sat = SortingAlgorithmTester()
#sat.integer_values_test_from_config_file()
sat.createInstanceTestFile(filename) #create file with protobuf
sat.integer_values_test_with_protobuf(filename) # test instance on protobuf bin file