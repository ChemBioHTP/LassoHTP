import sys
import shutil
import subprocess
import os
from lasso_extension.lasso_peptide_gen import *

path = os.getcwd()

def get_cwd(directory):
    """get directory
    """

    if os.path.isdir(directory):
        cwd = f"{path}/{directory}"
    else:
        os.mkdir(path+ "/" + directory)
        cwd = os.path.abspath(path + "/" + directory)

    return cwd

#def get_cwd(directory):
#    """get directory
#    """
#    
#    if(directory):
#        cwd = os.getcwd()
#    else:
#        os.mkdir(directory)
#        cwd = os.path.abspath(directory) 
#    
#    return cwd

def seq_parse(seq:str, ring_len: int, upper_plug: int):

    sequence = seq
    seq_len = len(sequence)
    ring = ring_len
    loop = upper_plug
    isopeptide = ''
    tail_length = seq_len - ( ring + loop )

    for idx , char in enumerate(seq):
        idx += 1
        if idx == ring:
            isopeptide = 'e' if char in 'E' else 'd'

    return sequence, ring, loop, tail_length, isopeptide


def seq_flags(seq: str, ring_num: int):
    """generates flags from sequence
    """
    lis = []
    for idx, char in enumerate(seq):
        idx +=1
        if idx == ring_num: #acidic residue
            continue
        lis.append('A' + str(idx) + char)
    return lis

def construct_scaffold(seq:str, ring_len: int, upper_plug:int, wk_dir):
    """constructs scaffold from given sequence
    """
    cwd = get_cwd(wk_dir)

    seq, ring, loop, tail_length, isopeptide = seq_parse(seq, ring_len, upper_plug)
    outfile = f"{ring}{isopeptide}_{loop}_{tail_length}.pdb"
    lasso_peptide_gen(ring, loop, tail_length, isopeptide, outfile)
    out_path = "lasso_extension/output_structures/" + outfile
    outfile_mover(out_path, cwd)

    return out_path

def outfile_mover(lasso,wk_dir):
    """moves outfile to working directory.
    """
    filePath = shutil.copy(lasso, wk_dir)
    #print(filePath)
    #command = ['cp', "/" + lasso, "/" + wk_dir + "/" + lasso ]
    #subprocess.run(command)
