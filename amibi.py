# Created on 2018-03-19 19:44:13 by amit

#imports
import numpy as np

#global parameters
dnalen = 20
mutationchance = 0.50

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
        if (position == 0):
            return self.dna[:segments]
        if (position == 1):
            return self.dna[segments:]

#World functions
def mutate(originaldna):
    dna = originaldna[:]
    for i in range(len(dna)):
        r = np.random.uniform()
        if (r <= mutationchance):
            if (originaldna[i] == 0):
                dna[i] == 1
            if (originaldna[i] == 1):
                dna[i] = 0
    return dna


def makechild(p1, p2):
    r = np.random.randint(1, 10)
    dna1 = p1.creategamete(0, r)
    dna2 = p2.creategamete(1, r)
    childdna = mutate(dna1 + dna2)
    return amibi(childdna)

#testing code
family = [amibi(randdnagen()) for i in range(10)]

mom = family[0]
dad = family[1]
child = makechild(mom, dad)

print(mom.dna)
print(dad.dna)
print(child.dna)