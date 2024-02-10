# LassoHTP2

The updated version of LassoHTP accommodates isopeptide bonds formed by Asp, Glu, and Asn. It supports loop lengths ranging from 3 to 50 residues.

Lasso peptide within 30 residues takes 10 to 60 minutes.

## Step 1 Environment

Ensure your Linux environment (python=3.9) includes the following software:
- **Amber:**  `pmemd.cuda`
- **PyMOL:**  `pymol -c`

Or use the same environment as EnzyHTP (https://enzyhtp-doc.readthedocs.io/en/latest/install.html#install-enviroment-for-enzyhtp)
## Step 2 Path

1. Download and unzip LassoHTP2 package
`tar -xzvf LassoHTP2_v1.tar.gz`

2. Update the package path in `main.py` and `main_arg.py`. For example:
`sys.path.append('/your/path/to/LassoHTP2_v2/construc_package')`

## Step 3 Lasso constructor

For the script version, modify the following inputs in `main.py`:

```python
    sequence = "WGDGSIDYFNRPMHIHDWQIMDSGYYG"  
    ring_len = 7  
    loop_len = 7 
    workdir = "./test1"  
    direction = "right"  # Direction of lasso peptide folding: 'right' (right-handed) or 'left' (left-handed), default is 'right'.
```

For the command line version, execute a single command, for example:

`python main_arg.py -seq WGDGSIDYFNRPMHIHDWQIMDSGYYG -ring_len 7 -loop_len 7 -fold_dir left -wkdir ./test1`

## Step 4 Output Structure

The directory under the work directory you specified will include `raw_output` and `final_output`, where `final_output` contains two constructed structures:

- `min1_clean.pdb` is the initial build structure for the lasso peptide, where the tail region appears rigid.
- `relax_cluster_clean.pdb` is the structure after MD relaxation. The most popular clustered structure is considered the representative structure. 