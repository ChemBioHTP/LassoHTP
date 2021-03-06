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

/tutorial contains a demo using the RGD mutant of microcin J25.
