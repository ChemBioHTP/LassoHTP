from Class_PDB import *
from Class_Conf import *
from seq_parser import *

def main():
    #initial PDB
    #use tleap to randomly mutate the PDB
        PDB1=PDB('8e_11_2.pdb',wk_dir='mccJ25_RGD')
        sequence=seq_flags('GGAGHVPEYFVRGDTPISFYG',8) #lasso seq
        print(PDB1.Add_MutaFlag(sequence))
        PDB1.PDB2PDBwLeap()
    # remove causal protonation from leap (Not sure if it's better to be before Min or not)
        #PDB1.rm_allH()
        #PDB1.get_protonation()
    #use minimization to relax each mutated PDB
        PDB1.PDB2FF()
        PDB1.PDBMin()
    #run MD
        PDB1.rm_wat()
        PDB1.PDB2FF()
        PDB1.conf_prod['nstlim'] = 500 # Edit MD configuration (see default in Class_Conf.py - Config.Amber)
        PDB1.PDBMD(tag='_mccJ25_RGD')

if __name__ == "__main__":
    main()
