import math

class StringInputAdapter():

    def _buildStringCollection(self, stringCollection):
        pairLongIntCollection = []
        for stringElement in stringCollection:
            
            longIntElement = 0
            i = 20 # assumption: a work could have at most 20 character
            dim = 0
            for a in stringElement:
                longIntElement = longIntElement + ord(a)*pow(256, i)
                i = i - 1
                dim = dim +1
            while dim < 20:
                longIntElement = longIntElement + 256*pow(256, i)
                i = i - 1
                dim = dim +1
            pairLongIntCollection.append((longIntElement,stringElement))

        return pairLongIntCollection

    def sortStringCollection(self, stringCollection, sorter, asc):
        pairLongIntCollection = self._buildStringCollection(stringCollection)
        keysCollection = [a_tuple[0] for a_tuple in pairLongIntCollection]

        print(keysCollection)
        sorter.sort(keysCollection, asc)

        orderedStringCollection = []
        for key in keysCollection:
            orderedStringCollection.extend([a_tuple[1] for a_tuple in pairLongIntCollection if a_tuple[0]==key])
        return orderedStringCollection
    

