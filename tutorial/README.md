For this tutorial, we will construct the RGD mutant of microcin J25 (PDBID 2mmw).
In the /initial_files folder, transfer input.py to the LassoHTP home directory.
You will find the input sequence of the lasso peptide in mcc_J25.fasta.
The ring size of microcin J25 is 8 and the upper plug position is 11.

Initiate the workflow using python input.py. For the sake of tutorial
brevity, the initial setting for production MD is 1 ns. Using LassoHTP with
GPU-acceleration will make short work of this simulation. Feel free to 
increase the number of MD steps for a longer simulation.
