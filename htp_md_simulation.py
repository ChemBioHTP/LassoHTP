 def _ligand_parm(self, paths, method='AM1BCC', renew=0):
        '''
        Turn ligands to prepi (w/net charge), parameterize with parmchk
        return [(perpi_1, frcmod_1), ...]
        -----------
        method  : method use for ligand charge. Only support AM1BCC now.
        renew   : 0:(default) use old parm files if exist. 1: renew parm files everytime
        * WARN: The parm file for ligand will always be like xxx/ligand_1.frcmod. Remember to enable renew when different object is sharing a same path.
        * BUG: Antechamber has a bug that if current dir has temp files from previous antechamber run (ANTECHAMBER_AC.AC, etc.) sqm will fail. Now remove them everytime.
        '''
        parm_paths = []
        self.prepi_path = {}

        for lig_pdb, net_charge in paths:
            if method == 'AM1BCC':
                out_prepi = lig_pdb[:-3]+'prepin'
                out_frcmod = lig_pdb[:-3]+'frcmod'
                with open(lig_pdb) as f:
                    for line in f:
                        pdbl=PDB_line(line)
                        if pdbl.line_type == 'ATOM' or pdbl.line_type == 'HETATM':
                            lig_name = pdbl.resi_name
                # if renew
                if os.path.isfile(out_prepi) and os.path.isfile(out_frcmod) and not renew:
                    if Config.debug >= 1:
                        print('Parm files exist: ' + out_prepi + ' ' + out_frcmod)
                        print('Using old parm files.')
                else:

        return parm_paths
        
def _combine_parm(self, lig_parms, prm_out_path='', o_dir='', ifsavepdb=0, ifsolve=1, box_type='oct', box_size=Config.Amber.box_size, igb=None, if_prm_only=0):
    '''
    combine different parmeter files and make finally inpcrd and prmtop
    -------
    structure: pdb
    ligands: prepi, frcmod
    metalcenters, artificial residues: TODO
    '''
    if box_type == None:
        box_type = Config.Amber.box_type

    leap_path= self.cache_path+'/leap.in'
    sol_path= self.path_name+'_ff.pdb'
    with open(leap_path, 'w') as of:
        of.write('source leaprc.protein.ff14SBmod'+line_feed) #using modified ff14SB - Reecan
        of.write('source leaprc.gaff'+line_feed)
        of.write('source leaprc.water.tip3p'+line_feed)
        # ligands
        of.write('loadAmberParams ../ligands/ligand_ASX.frcmod1'+line_feed)
        of.write('loadAmberParams ../ligands/ligand_ASX.frcmod2'+line_feed)
        of.write('loadAmberPrep ../ligands/ligand_ASX.prepin'+line_feed)
        for prepi, frcmod in lig_parms:
            of.write('loadAmberParams '+frcmod+line_feed)
            of.write('loadAmberPrep '+prepi+line_feed)
        of.write('a = loadpdb '+self.path+line_feed)
        #no need to change this for l.p.'s of any ring size. - Reecan
        of.write('bond a.2.N a.ASX.C'+line_feed) # lasso peptide thread
        of.write('bond a.ASX.CG a.14.N'+line_feed) #isopeptide
        # igb Radii
        if igb != None:
            radii = radii_map[str(igb)]
            of.write('set default PBRadii '+ radii +line_feed)
        of.write('center a'+line_feed)
        # solvation
        if ifsolve:
           # of.write('addions a Na+ 0'+line_feed)
           # of.write('addions a Cl- 0'+line_feed)
            if box_type == 'box':
                of.write('solvatebox a TIP3PBOX '+box_size+line_feed)
            if box_type == 'oct':
                of.write('solvateOct a TIP3PBOX '+box_size+line_feed)
            if box_type != 'box' and box_type != 'oct':
                raise Exception('PDB._combine_parm().box_type: Only support box and oct now!')
        # save
        if prm_out_path == '':
            if o_dir == '':
                of.write('saveamberparm a '+self.path_name+'.prmtop '+self.path_name+'.inpcrd'+line_feed)
                self.prmtop_path=self.path_name+'.prmtop'
                self.inpcrd_path=self.path_name+'.inpcrd'
            else:
                of.write('saveamberparm a '+o_dir+self.name+'.prmtop '+o_dir+self.name+'.inpcrd'+line_feed)
                self.prmtop_path=o_dir+self.name+'.prmtop'
                self.inpcrd_path=o_dir+self.name+'.inpcrd'
        else:
            if o_dir == '':
                if if_prm_only:
                    mkdir('./tmp')
                    of.write('saveamberparm a '+prm_out_path+' ./tmp/tmp.inpcrd'+line_feed)
                    self.prmtop_path=prm_out_path
                    self.inpcrd_path=None
                else:
                    of.write('saveamberparm a '+prm_out_path+' '+self.path_name+'.inpcrd'+line_feed)
                    self.prmtop_path=prm_out_path
                    self.inpcrd_path=self.path_name+'.inpcrd'
            else:
                if if_prm_only:
                    mkdir('./tmp')
                    of.write('saveamberparm a '+prm_out_path+' ./tmp/tmp.inpcrd'+line_feed)
                    self.prmtop_path=prm_out_path
                    self.inpcrd_path=None
                else:
                    of.write('saveamberparm a '+prm_out_path+' '+o_dir+self.name+'.inpcrd'+line_feed)
                    self.prmtop_path=prm_out_path
                    self.inpcrd_path=o_dir+self.name+'.inpcrd'

        if ifsavepdb:
            of.write('savepdb a '+sol_path+line_feed)
        of.write('quit'+line_feed)

    os.system('tleap -s -f '+leap_path+' > '+leap_path[:-2]+'out')

    return self.prmtop_path, self.inpcrd_path
