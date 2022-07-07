from Class_PDB import *
from Class_Conf import *
from seq_parser import *

def main():
    #specify the annotated sequence and working directory
        seq, ring_length, upper_plug, wk_dir = 'GGAGHVPEYFVRGDTPISFYG', 8, 11, ''
        proto_lasso=construct_scaffold(seq, ring_length, upper_plug, wk_dir)
        print(proto_lasso)
        PDB1=PDB(proto_lasso,wk_dir)
        sequence=seq_flags(seq, 8) #lasso seq
        print(PDB1.Add_MutaFlag(sequence))
        PDB1.PDB2PDBwLeap()
    #use minimization to relax each mutated lasso
        PDB1.PDB2FF()
        PDB1.PDBMin()
    #run MD
        PDB1.rm_wat()
        PDB1.PDB2FF()
        PDB1.conf_prod['nstlim'] = 500 # Edit MD configuration (see default in Class_Conf.py - Config.Amber)
        PDB1.PDBMD(tag='_mccJ25_RGD') #dir to store MD input files

if __name__ == "__main__":
    main()
