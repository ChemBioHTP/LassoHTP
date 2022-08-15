import sys
import shutil
import subprocess
import os

def get_cwd(directory):
    """gets directory and returns path
    """
    if(not directory):
        cwd = os.getcwd()
    else:
        if os.path.isdir(directory):
            cwd = os.path.abspath(directory)
            return cwd
        else:
            os.mkdir(directory)
            cwd = os.path.abspath(directory)

    return cwd

def locate_tail_ext_module():
    """gives path of /lasso_extension
    """
    lhtp_dir = get_cwd('')
    tail_ext_dir = lhtp_dir + '/lasso_extension'

    return tail_ext_dir

tail_ext_dir = locate_tail_ext_module()
sys.path.insert(0,tail_ext_dir)
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
    print(filePath)
