from Sorter import Sorter
from SorterFactory import SorterFactory

sf = SorterFactory()
s = sf.getSorter('InsertionSort')
a = [31, 41, 59, 26, 41, 58]
s.sort(a)
print(a)
