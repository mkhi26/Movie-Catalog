from Nucleo.NodeLinkedList import *
from Nucleo.Movie import *
from Nucleo import NodeN
class Compare:

    def __init__(self):
        self.alphabet = ',./;!@#$%*()-+0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def compare(self, obj1, obj2):
        if isinstance(obj1, NodeN.NodeN):
 
            obj1= obj1.value
            
        if isinstance(obj2, NodeN.NodeN):
            obj2 = obj2.value

        if(isinstance(obj1, Node)):
            obj1 = obj1.value.value
        if(isinstance(obj2, Node)):
            obj2 = obj2.value.value
        obj1 = '%s' % obj1
        obj2 = '%s' % obj2

        min = self.min(obj1, obj2)
        min = self.min(obj1, obj2)
        for i in range(0, min): 

            if(self.alphabet.find(obj1[i]) < self.alphabet.find(obj2[i])):
                return -1

            elif(self.alphabet.find(obj1[i]) > self.alphabet.find(obj2[i])):
                return 1

        if(len(obj1) < len(obj2)):
            return -1

        elif(len(obj1) > len(obj2)):
            return 1

        return 0


    def min(self, str1, str2):
        min = len(str1)
        size2 = len(str2)
        if(min > size2):
            min = size2
        return min