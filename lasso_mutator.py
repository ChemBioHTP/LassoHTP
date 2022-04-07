def PDB2PDBwLeap(self):
        '''
        Apply mutations using tleap. Save mutated structure PDB in self.path
        ------------------------------
        Use MutaFlag in self.MutaFlags
        Grammer (from Add_MutaFlag):
        X : Original residue name. Leave X if unknow.
            Only used for build filenames. **Do not affect any calculation.**
        A : Chain index. Determine by 'TER' marks in the PDB file. (Do not consider chain_indexs in the original file.)
        11: Residue index. Strictly correponding residue indexes in the original file. (NO sort applied)
        Y : Target residue name.

        **WARNING** if there are multiple mutations on the same index, only the first one will be used.
        '''

        #Judge if there are same MutaIndex (c_id + r_id)
        for i in range(len(self.MutaFlags)):
            for j in range(len(self.MutaFlags)):
                if i >= j:
                    pass
                else:
                    if (self.MutaFlags[i][1], self.MutaFlags[i][2]) == (self.MutaFlags[j][1], self.MutaFlags[j][2]):
                        if Config.debug >= 1:
                            print("PDB2PDBwLeap: There are multiple mutations at the same index, only the first one will be used: "+self.MutaFlags[i][0]+self.MutaFlags[i][1]+self.MutaFlags[i][2])

        # Prepare a label for the filename
        tot_Flag_name=''
        for Flag in self.MutaFlags:
            Flag_name=self._build_MutaName(Flag)
            tot_Flag_name=tot_Flag_name+'_'+Flag_name

        # Operate the PDB
        out_PDB_path1=self.cache_path+'/'+self.name+tot_Flag_name+'_tmp.pdb'
        out_PDB_path2=self.path_name+tot_Flag_name+'.pdb'

        self._get_file_path()
        with open(self.path,'r') as f:
           with open(out_PDB_path1,'w') as of:
                chain_count = 1
                for line in f:
                    pdb_l = PDB_line(line)

                    TER_flag = 0
                    if pdb_l.line_type == 'TER':
                        TER_flag = 1
                    # add chain count in next loop for next line
                    if TER_flag:
                        chain_count += 1
                    match=0
                    # only match in the dataline and keep all non data lines
                    if pdb_l.line_type == 'ATOM':
                        for Flag in self.MutaFlags:
                            # Test for every Flag for every lines
                            t_chain_id=Flag[1]
                            t_resi_id =Flag[2]

                            if chr(64+chain_count) == t_chain_id:
                                if pdb_l.resi_id == int(t_resi_id):

                                    # do not write old line if match a MutaFlag
                                    match=1
                                    # Keep OldAtoms of targeted old residue
                                    resi_2 = Flag[3]
                                    OldAtoms=['N','H','CA','HA','CB','C','O']
                                    #fix for mutations of Gly & Pro
                                    if resi_2 == 'G':
                                        OldAtoms=['N','H','CA','C','O']
                                    if resi_2 == 'P':
                                        OldAtoms=['N','CA','HA','CB','C','O']

                                    for i in OldAtoms:
                                        if i == pdb_l.atom_name:
                                            new_line=line[:17]+Resi_map[resi_2]+line[20:]

                                            of.write(new_line)
                                            break
                                    #Dont run for other Flags after first Flag matches.
                                    break
                     if not match:
                        of.write(line)


        # Run tLeap
        #make input
        #added custom frcmod and atom bonds
        leapin_path = self.cache_path+'/leap_P2PwL.in'
        leap_input=open(leapin_path,'w')
        leap_input.write('source leaprc.protein.ff14SBmod\n')
        if 'asx' in leapin_path:
            leap_input.write('loadAmberParams ../ligands/ligand_ASX.frcmod1\n')
            leap_input.write('loadAmberParams ../ligands/ligand_ASX.frcmod2\n')
            leap_input.write('loadAmberPrep ../ligands/ligand_ASX.prepin\n')
            leap_input.write('a = loadpdb '+out_PDB_path1+'\n')
            leap_input.write('bond a.2.N a.ASX.C\n')
            leap_input.write('bond a.ASX.CG a.14.N\n')
        elif 'glx' in leapin_path:
            leap_input.write('loadAmberParams ../ligands/ligand_GLX.frcmod1\n')
            leap_input.write('loadAmberParams ../ligands/ligand_GLX.frcmod2\n')
            leap_input.write('loadAmberPrep ../ligands/ligand_GLX.prepin\n')
            leap_input.write('a = loadpdb '+out_PDB_path1+'\n')
            leap_input.write('bond a.2.N a.GLX.C01\n')
            leap_input.write('bond a.GLX.CD a.14.N\n')
        leap_input.write('savepdb a '+out_PDB_path2+'\n')
        #
       # leap_input.write('saveamberparm a '+out_PDB_path2+'.prmtop '+out_PDB_path2+'.inpcrd'+line_feed)
        #
        leap_input.write('quit\n')
        leap_input.close()
        #run
        os.system('tleap -s -f '+leapin_path+' > '+self.cache_path+'/leap_P2PwL.out')
        if Config.debug <= 1:
         os.system('rm leap.log')

        #Update the file
        self.path = out_PDB_path2
        self._update_name()

        return self.path
