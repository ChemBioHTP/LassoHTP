# LassoHTP
LassoHTP is a computational tool geared towards lasso peptide design and discovery. Major functionalities include the high throughput (HTP) construction of lasso peptides as well as HTP molecular dynamics (MD) simulations to predict lasso peptide thermodynamic parameters.

Lasso peptides are a unique class of ribosomally synthesized and post-translationally modified peptides (RiPP) that exhibit interesting bioactivities such as antimicrobial activity. Genome-based and bioengineering strategies are typically applied to lasso peptide discovery and design, and have largely neglected computational strategies. LassoHTP is one computational strategy that is in development.

<p align="center">
  <img width="650" height="300" src="https://github.com/so-dopamine/LassoHTP/blob/main/image.jpg">
</p>

LassoHTP contains three main modules:
1. Scaffold constructor
2. Mutant generator
3. MD simulator

The scaffold constructor module builds molecular templates, or scaffolds, of a lasso peptide with variable ring size, upper loop length, and tail length.

The mutant generator module mutates each of the residues on a given molecular template to fit a specified peptide sequence. Users can also randomly mutate the template as well as selectively mutate one or more topological sections of the template.

The HTP MD simulation module performs multiscale-MD on LassoHTP-constructed lasso peptides. The module automates minimization, heating, and equilibration for each constructed lasso peptide as well as the curation of each MD stage's input file. Production MD uses umbrella sampling to optimize sampling for each lasso peptide. The HTP component can also propogate multiple trajectories and in turn ensembles that can be used to calculate conformational entropies.

The scaffold library consists of only one scaffold per topology that involves a unique combination of ring size (e.g., seven-, eight-, or nine-membered ring), loop size (e.g, 2-18 amino acids), and linker type (e.g., Asp or Glu). Specifically, the library consists of 70 scaffold structures with 18 seven-membered ring structures, 34 eight-membered ring structures, and 18 nine-membered ring structures. Most of the scaffolds (56 out of 70) were constructed using steered molecular dynamics simulations. The rest of the scaffolds were constructed by using PDB structure as template. The PDB IDs of these templates are 6mw6 (ring size: 8; loop size: 9; linker: Asp/Glu), 2mmw (ring size: 8; loop size: 11; linker: Asp/Glu), 6por (ring size: 8; loop size: 18; linker: Asp/Glu), 5zcn (ring size: 9; loop size: 4; linker: Asp/Glu), 5gvo (ring size: 9; loop size: 5; linker: Asp/Glu), 5d9e (ring size: 9; loop size: 6; linker: Asp/Glu), and 2mlj (ring size: 9; loop size: 7; linker: Asp/Glu).  

/tutorial contains a demo using the RGD mutant of microcin J25.

# Requirements
## External Program
- AmberTool/Amber
- Anaconda/miniconda

## Python Packages
- python >= 3.6
- numpy
- pdb2pqr
- openbabel
