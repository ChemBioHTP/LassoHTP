from Class_PDB import *

def topology_sort(self):
    '''
    sort the sequence of the lasso peptide into sections
    representative of its topology
    '''
    self.upperLoop=[]
    self.tail=[]
    self.plugs=[]
    self.ring=[]
    self.upperPlug=[]
    self.lowerPlug=[]
    self.essentialRes=[] #this residue connects the ring and tail

    #these ranges can be changed to accomodate for
    #different lasso peptide structures.
    upperRange=range(7)
    plugRange=range(7,9)
    tailRange=range(10,14)
    ringRange=range(15,21) # 21 = 7mr, 22 = 8mr, 23 = 9mr

    #pluglocation
    uPlugRes = 7
    lPlugRes = 8

    #sort the PDB
    with open(self.path) as f:
        lines = [line.split() for line in f]
        i = 4 #by residue number
        for l in lines:
            if i < len(l): #avoid 'END'
                if int(l[i]) in upperRange:
                    self.upperLoop.append(str(l[i]))
                if int(l[i]) in plugRange:
                    self.plugs.append(str(l[i]))
                    if int(l[i]) == uPlugRes:
                        self.upperPlug.append(str(l[i]))
                    if int(l[i]) == lPlugRes:
                        self.lowerPlug.append(str(l[i]))
                if int(l[i]) in tailRange:
                    self.tail.append(str(l[i]))
                if int(l[i]) in ringRange:
                    self.ring.append(str(l[i]))
                if (l[i-1]) == 'ASX':
                    self.essentialRes.append(str(l[i]))
            else:
                None

    self.upperLoop = list(set(self.upperLoop))
    self.tail = list(set(self.tail))
    self.plugs = list(set(self.plugs))
    self.ring = list(set(self.ring))
    self.upperPlug = list(set(self.upperPlug))
    self.lowerPlug = list(set(self.lowerPlug))
    self.essentialRes = list(set(self.essentialRes))

    return self.upperLoop, self.tail, self.plugs, self.ring, self.upperPlug, self.lowerPlug, self.essentialRes
   
def partition(self):
    '''
    partition the lasso structure into parts
    '''

    a = list(self.topology_sort())

    upperLoop = a[0] #loop
    tail = a[1] #tail
    plugs = a[2] #plugs
    ring = a[3] #ring
    upperPlug = a[4] #upper plug
    lowerPlug = a[5] #lower plug
    essentialRes = a[6]

    sect = 'loop' #blank string: mutate any topological section.

    self.get_stru()

    chain = choice(self.stru.chains)
    resi = choice(chain.residues)

    if sect == 'loop':
        if str(resi.id) not in upperLoop:
            while str(resi.id) not in upperLoop:
                resi = choice(chain.residues)
    elif sect == 'tail':
        while str(resi.id) not in tail:
            resi = choice(chain.residues)
    elif sect == 'plugs':
        while str(resi.id) not in plugs:
            resi = choice(chain.residues)
    elif sect == 'ring':
        while str(resi.id) not in ring:
            resi = choice(chain.residues)
    elif sect == 'upper plug':
        while str(resi.id) not in upperPlug:
            resi = choice(chain.residues)
    elif sect == 'lower plug':
        while str(resi.id) not in lowerPlug:
            resi = choice(chain.residues)
    elif sect == '':
        resi = choice(chain.residues)
