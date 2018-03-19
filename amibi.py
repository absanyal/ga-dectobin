# Created on 2018-03-19 19:44:13 by amit

#imports
import numpy as np

#global parameters
dnalen = 10

# Generator of ID numbers
def id_num():
    i = 1
    while (True):
        yield i
        i += 1
id_no = id_num()

#Generate random dna
def randdnagen():
    return [np.random.choice([0, 1]) for i in range(dnalen)]

# Creature Class
class amibi:
    
    def __init__(self, dna):
        self.idno = next(id_no)
        self.dna = dna
    
    def creategamete(self, position, segments):
        if (position == 'front'):
            return self.dna[:segments]
        else:
            return self.dna[segments:]

#testing code
family = [amibi(randdnagen()) for i in range(10)]

for a in family:
    print(a.dna)