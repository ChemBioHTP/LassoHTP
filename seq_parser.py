import sys
sys.path.insert(0, '/usr/home/LassoHTP/lasso_extension')
from lasso_peptide_gen import *

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
    #lis = ['A' + str(idx+1) + char for idx, char in enumerate(seq)]
    #    return 'A' + str(idx+1) + char
    return lis

def construct_scaffold(seq:str, ring_len: int, upper_plug:int):
    """constructs scaffold from given sequence
    """
    seq_len=len(seq)
    ring = ring_len
    loop = upper_plug
    isopeptide = ''
    tail_length = seq_len - ( ring + loop )
    for idx, char in enumerate(seq):
        idx +=1
        if idx == ring:
           isopeptide = 'e' if char in 'E' else 'd'
    outfile = f"{ring}{isopeptide}_{loop}_{tail_length}.pdb"
    lasso_peptide_gen(ring, loop, tail_length, isopeptide, outfile)

def outfile_pointer():
    """moves outfile to working directory.
    """
    #os
    pass
