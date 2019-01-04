import Normalization.CreateList

class Normalize:

    def __init__(self):
        print("welcome to Normalize class")

    def generateData(self):
        obj = Normalization.CreateList.BuildList()
        obj.generateList()
        print("Data has been generated")

