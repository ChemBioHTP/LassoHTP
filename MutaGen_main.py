from Class_PDB import *
from Class_Conf import *
from seq_parser import *

#This is the main file
def main():
    #initial PDB
    #use tleap to randomly mutate the PDB
        PDB1=PDB('',wk_dir='')
        sequence=seq_flags('',) #lasso seq
        print(PDB1.Add_MutaFlag(sequence))
        PDB1.PDB2PDBwLeap()
    #use minimization to relax each mutated PDB
        PDB1.PDB2FF()
        PDB1.PDBMin()
    #run MD
        PDB1.rm_wat()
        PDB1.PDB2FF()
        PDB1.conf_prod['nstlim'] = 50500000 # Edit MD configuration (see default in Class_Conf.py - Config.Amber)
        PDB1.PDBMD(tag='_')

if __name__ == "__main__":
    main()
