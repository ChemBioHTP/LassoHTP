import sys
sys.path.insert(0, '/usr/LassoHTP/lasso_extension')
import subprocess
import os
from lasso_extension.lasso_peptide_gen import *

module_file_dir = os.path.split(os.path.realpath(__file__))[0]
def get_cwd(directory):
    """get directory
    """
    
    if(not directory):
        cwd = os.getcwd()
    else:
        cwd = os.path.abspath(directory) 
    
    return cwd

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
    out_path = f"{module_file_dir}/lasso_extension/output_structures/" + outfile
    outfile_mover(out_path, cwd)   
 
    return out_path

def outfile_mover(lasso,wk_dir):
    """moves outfile to working directory.
    """
    command = ['cp', lasso, wk_dir]
    subprocess.run(command)
