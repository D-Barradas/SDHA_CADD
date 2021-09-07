#!/usr/bin/env python
# coding: utf-8

import os
import zipfile
from biobb_structure_utils.utils.cat_pdb import cat_pdb
from biobb_io.api.pdb import pdb
from biobb_model.model.fix_side_chain import fix_side_chain
from optparse import OptionParser
from biobb_md.gromacs.pdb2gmx import pdb2gmx


##Parse the options
usage = "USAGE: python Create_topologies_using_BioXcelBB.py --f1 receptor_file.pdb --f2 ligand_file.pdbqt\n"
parser = OptionParser(usage=usage)

##options
parser.add_option("--f1",help="First molecule pdb", dest="f1")
parser.add_option("--f2",help="Second molecule pdbqt", dest="f2")
#parser.add_option("--f3",help="Folder name", dest="f3")

(options, args) = parser.parse_args()

if (options.f1) and (options.f2) :
    print ("start ...")

else:

    print ("Not enough input arguments supplied")
    print (usage)
    quit()


# Create and launch bb
#proteinFile = "../files/receptor_md.pdb"
proteinFile = options.f1
ligandCode = "%s"% ( options.f2.split("_")[-1].split(".")[0])
print (ligandCode)

fixed_pdb = "../files/receptor_md_fixed.pdb"
if os.path.isfile(fixed_pdb) == False:
    try :
        fix_side_chain(input_pdb_path=proteinFile,
             output_pdb_path=fixed_pdb)

    except :
        print ("Receptor file found, skiping fixing")

# Create Protein system topology
# Check file existance
if os.path.isfile("../files/receptor_md_fixed_pdb2gmx.gro") == False :
    try :
        # Create inputs/outputs
        output_pdb2gmx_gro = '../files/receptor_md_fixed_pdb2gmx.gro'
        output_pdb2gmx_top_zip = '../files/receptor_md_fixed_pdb2gmx_top.zip'
        prop = { 'force_field' : 'amber99sb-ildn', 'water_type': 'spce' }

        # Create and launch bb
        pdb2gmx(input_pdb_path=fixed_pdb,
        output_gro_path=output_pdb2gmx_gro,
        output_top_zip_path=output_pdb2gmx_top_zip,
        properties=prop)

    except :
        print ("Receptor topology found ")
        print (f"properties : {prop}")

else :
    output_pdb2gmx_gro = '../files/receptor_md_fixed_pdb2gmx.gro'
    output_pdb2gmx_top_zip = '../files/receptor_md_fixed_pdb2gmx_top.zip'


import openbabel as ob


obConversion = ob.OBConversion()
obConversion.SetInAndOutFormats( "pdbqt", "pdb")

obmol = ob.OBMol()
#obConversion.ReadFile(obmol,"../files/ligand_vina_out_CHEMBL126.pdbqt")
obConversion.ReadFile(obmol,options.f2)

obmol.CorrectForPH()
obmol.AddHydrogens()


print (obmol.NumAtoms())
print (obmol.NumBonds())

#outMDL = obConversion.WriteFile(obmol,"%s.pdb"%(options.f2.split(".")[0]))
outMDL = obConversion.WriteFile(obmol,f'{ligandCode}.pdb')



# Create Ligand system topology, STEP 1
# Reduce_add_hydrogens: add Hydrogen atoms to a small molecule (using Reduce tool from Ambertools package)
# Import module
from biobb_chemistry.ambertools.reduce_add_hydrogens import reduce_add_hydrogens


# In[10]:


# Create prop dict and inputs/outputs
### my ligands are already minized but comes with a lot of models

ligandFile = "%s.pdb"%(ligandCode)
#ligandFile = "../files/ligand_vina_out_CHEMBL126.pdb"
output_reduce_h = ligandCode+".reduce.H.pdb"
prop = {
    'nuclear' : 'true'
}


# Create and launch bb
reduce_add_hydrogens(input_path=ligandFile,
                   output_path=output_reduce_h,
                   properties=prop)


# In[11]:


# Create Ligand system topology, STEP 2
# Babel_minimize: Structure energy minimization of a small molecule after being modified adding hydrogen atoms
# Import module
from biobb_chemistry.babelm.babel_minimize import babel_minimize

# Create prop dict and inputs/outputs
output_babel_min = ligandCode+".reduce.H.min.mol2"
#output_babel_min = "../files/ligand_vina_out_CHEMBL126.reduce.H.min.mol2"
prop = {
    'method' : 'sd',
    'criteria' : '1e-10',
    'force_field' : 'GAFF'
}


# Create and launch bb
babel_minimize(input_path=output_reduce_h,
              output_path=output_babel_min,
              properties=prop)


# In[12]:


# Create Ligand system topology, STEP 3
# Acpype_params_gmx: Generation of topologies for GROMACS with ACPype
# Import module
from biobb_chemistry.acpype.acpype_params_gmx import acpype_params_gmx


# In[13]:


# Create prop dict and inputs/outputs
mol_charge = 0


#ligandCode = "CHEMBL126"
output_acpype_gro = ligandCode+'_params.gro'
output_acpype_itp = ligandCode+'_params.itp'
output_acpype_top = ligandCode+'_params.top'
output_acpype = ligandCode+'_params'
prop = {
    'basename' : output_acpype,
    'charge' : mol_charge
}

# Create and launch bb
acpype_params_gmx(input_path=output_babel_min,
# acpype_params_gmx(input_path="../files/ligand_vina_out_CHEMBL126.mol2",

                output_path_gro=output_acpype_gro,
                output_path_itp=output_acpype_itp,
                output_path_top=output_acpype_top,
                properties=prop)


# In[14]:


# MakeNdx: Creating index file with a new group (small molecule heavy atoms)
from biobb_md.gromacs.make_ndx import make_ndx

# Create prop dict and inputs/outputs
output_ligand_ndx = ligandCode+'_index.ndx'
prop = {
    'selection': "0 & ! a H*"
}

# Create and launch bb
make_ndx(input_structure_path=output_acpype_gro,
        output_ndx_path=output_ligand_ndx,
        properties=prop)


# In[15]:


# Genrestr: Generating the position restraints file
from biobb_md.gromacs.genrestr import genrestr

# Create prop dict and inputs/outputs
output_restraints_top = ligandCode+'_posres.itp'
prop = {
    'force_constants': "1000 1000 1000",
    'restrained_group': "System"
}

# Create and launch bb
genrestr(input_structure_path=output_acpype_gro,
         input_ndx_path=output_ligand_ndx,
         output_itp_path=output_restraints_top,
         properties=prop)


# In[16]:


# biobb analysis module
from biobb_analysis.gromacs.gmx_trjconv_str import gmx_trjconv_str
from biobb_structure_utils.utils.cat_pdb import cat_pdb

# Convert gro (with hydrogens) to pdb (PROTEIN)
pdbCode = "SDHA"

proteinFile_H = pdbCode+'_'+ligandCode+'_complex_H.pdb'
prop = {
    'selection' : 'System'
}

# Create and launch bb
gmx_trjconv_str(input_structure_path=output_pdb2gmx_gro,
              input_top_path=output_pdb2gmx_gro,
              output_str_path=proteinFile_H,
              properties=prop)

# Convert gro (with hydrogens) to pdb (LIGAND)
ligandFile_H = ligandCode+'_complex_H.pdb'
prop = {
    'selection' : 'System'
}

# Create and launch bb
gmx_trjconv_str(input_structure_path=output_acpype_gro,
              input_top_path=output_acpype_gro,
              output_str_path=ligandFile_H,
              properties=prop)


# Concatenating both PDB files: Protein + Ligand
complexFile_H = pdbCode+'_'+ligandCode+'_H.pdb'

# Create and launch bb
cat_pdb(input_structure1=proteinFile_H,
       input_structure2=ligandFile_H,
       output_structure_path=complexFile_H)


# In[17]:


# AppendLigand: Append a ligand to a GROMACS topology
# Import module
from biobb_md.gromacs_extra.append_ligand import append_ligand

# Create prop dict and inputs/outputs
output_complex_top = pdbCode+'_'+ligandCode+'_complex.top.zip'

posresifdef = "POSRES_"+ligandCode.upper()
prop = {
    'posres_name': posresifdef
}

# Create and launch bb
append_ligand(input_top_zip_path=output_pdb2gmx_top_zip,
             input_posres_itp_path=output_restraints_top,
             input_itp_path=output_acpype_itp,
             output_top_zip_path=output_complex_top,
             properties=prop)


# In[19]:


# Editconf: Create solvent box
# Import module
from biobb_md.gromacs.editconf import editconf

# Create prop dict and inputs/outputs
output_editconf_gro = pdbCode+'_'+ligandCode+'_complex_editconf.gro'

prop = {
    'box_type': 'octahedron',
    'distance_to_molecule': 1.0,
    'center_molecule': True
}

# Create and launch bb
editconf(input_gro_path=complexFile_H,
         output_gro_path=output_editconf_gro,
         properties=prop)


# In[20]:


# Solvate: Fill the box with water molecules
from biobb_md.gromacs.solvate import solvate

# Create prop dict and inputs/outputs
output_solvate_gro = pdbCode+'_'+ligandCode+'_solvate.gro'
output_solvate_top_zip = pdbCode+'_'+ligandCode+'_solvate_top.zip'

# Create and launch bb
solvate(input_solute_gro_path=output_editconf_gro,
        output_gro_path=output_solvate_gro,
        input_top_zip_path=output_complex_top,
        output_top_zip_path=output_solvate_top_zip)


# In[21]:


# Grompp: Creating portable binary run file for ion generation
from biobb_md.gromacs.grompp import grompp

# Create prop dict and inputs/outputs
prop = {
    'mdp':{
        'nsteps':'5000'
    },
    'simulation_type':'minimization',
    'maxwarn': 1
}
output_gppion_tpr = pdbCode+'_'+ligandCode+'_complex_gppion.tpr'

# Create and launch bb
grompp(input_gro_path=output_solvate_gro,
       input_top_zip_path=output_solvate_top_zip,
       output_tpr_path=output_gppion_tpr,
       properties=prop)


# In[22]:


# Genion: Adding ions to reach a 0.05 molar concentration
from biobb_md.gromacs.genion import genion

# Create prop dict and inputs/outputs
prop={
    'neutral':True,
    'concentration':0.05
}
output_genion_gro = pdbCode+'_'+ligandCode+'_genion.gro'
output_genion_top_zip = pdbCode+'_'+ligandCode+'_genion_top.zip'

# Create and launch bb
genion(input_tpr_path=output_gppion_tpr,
       output_gro_path=output_genion_gro,
       input_top_zip_path=output_solvate_top_zip,
       output_top_zip_path=output_genion_top_zip,
       properties=prop)


# In[23]:


# import nglview
# import ipywidgets


# In[24]:


# #Show protein
# view = nglview.show_structure_file(output_genion_gro)
# view.clear_representations()
# view.add_representation(repr_type='cartoon', selection='protein', color='sstruc')
# view.add_representation(repr_type='licorice', radius='.5', selection=ligandCode)
# view.add_representation(repr_type='line', linewidth='1', selection='SOL', opacity='.3')
# view.add_representation(repr_type='ball+stick', selection='NA')
# view.add_representation(repr_type='ball+stick', selection='CL')
# view._remote_call('setSize', target='Widget', args=['','600px'])
# view.camera='orthographic'

# view.render_image()
# view.download_image(filename=f'../files/{pdbCode}_{ligandCode}_genion.png')

# view


# In[25]:


### gather thisn in the apropiate folder


# In[26]:


# gather_files = [ x for x in os.listdir(".") if ligandCode in x ]


# In[ ]:





# In[27]:


def clean_WS():
    os.system(f"mkdir -p ../files/{ligandCode}")
    gather_files = [ x for x in os.listdir(".") if ligandCode in x ]
    erase_log_files = [ x for x in os.listdir(".") if "log" == x[0:3]]
    erase_itp = [ x for x in os.listdir(".") if ".itp" == x[-4:]]
    erase_pdb2gmx = [ x for x in os.listdir(".") if "pdb2gmx" in x]
    for x in gather_files:
        os.system(f"mv {x} ../files/{ligandCode}/")
    for x in erase_log_files:
        if os.path.isfile(x) :
            os.remove(x)

    for x in erase_itp :
         if os.path.isfile(x) :
            os.remove(x)

    for x in erase_pdb2gmx :
         if os.path.isfile(x) :
            os.remove(x)

    print (len (gather_files))
    print (len (erase_log_files))
    print (len (erase_itp))
    print (len (erase_pdb2gmx))


# In[28]:


clean_WS()


# # At this poitn I could proceed with gromacs protocol
