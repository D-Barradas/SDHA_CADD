#!/usr/bin/env python
# coding: utf-8

# In[43]:


# Grompp: Creating portable binary run file for mdrun
import os
from biobb_md.gromacs.grompp import grompp
from biobb_md.gromacs.make_ndx import make_ndx
from biobb_md.gromacs.mdrun import mdrun
from biobb_analysis.gromacs.gmx_energy import gmx_energy
from optparse import OptionParser

##Parse the options
usage = "USAGE: python Create_topologies_using_BioXcelBB.py --f1 path_to_gmx_files\n"
parser = OptionParser(usage=usage)

##options
parser.add_option("--f1",help="First molecule pdb", dest="f1")

(options, args) = parser.parse_args()

if (options.f1)  :
    print ("start ...")

else:

    print ("Not enough input arguments supplied")
    print (usage)
    quit()


#ligandCode = "CHEMBL126"
pdbCode = "SDHA"
ligandCode = "%s"%(options.f1 )


output_genion_gro = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_genion.gro"
output_genion_top_zip = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_genion_top.zip"

if os.path.isfile(output_genion_gro):
    print ("Check pass")
    os.system(f"mkdir -p ../files/{ligandCode}/figures/")
else :
    print (f"file {output_genion_gro} or file {output_genion_top_zip} missing")
    quit ()


output_gppmin_tpr = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_gppmin.tpr"


# Create prop dict and inputs/outputs
prop = {
    'mdp':{
        'nsteps':'5000',
        'emstep': 0.01,
        'emtol':'500'
    },
    'simulation_type':'minimization'
}

# Create and launch bb
grompp(input_gro_path=output_genion_gro,
       input_top_zip_path=output_genion_top_zip,
       output_tpr_path=output_gppmin_tpr,
       properties=prop)


# In[9]:


# Mdrun: Running minimization


# In[7]:


# Create prop dict and inputs/outputs
output_min_trr = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_min.trr"
output_min_gro = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_min.gro"
output_min_edr = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_min.edr"
output_min_log = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_min.log"

# Create and launch bb\n
mdrun(input_tpr_path=output_gppmin_tpr,
      output_trr_path=output_min_trr,      
      output_gro_path=output_min_gro,      
      output_edr_path=output_min_edr,      
      output_log_path=output_min_log)


# GMXEnergy: Getting system energy by time  

# Create prop dict and inputs/outputs
output_min_ene_xvg = f"../files/{ligandCode}/figures/{pdbCode}_{ligandCode}_min_ene.xvg"
prop = {
    'terms':  ["Potential"]
}

# Create and launch bb
gmx_energy(input_energy_path=output_min_edr, 
          output_xvg_path=output_min_ene_xvg, 
          properties=prop)




# MakeNdx: Creating index file with a new group (protein-ligand complex)

# output_complex_ndx = pdbCode+'_'+ligandCode+'_index.ndx'
output_complex_ndx = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_index.ndx"

# Create prop dict and inputs/outputs
prop = {
    'selection': "\"Protein\"|\"Other\"" 
}


# Create and launch bb
make_ndx(input_structure_path=output_min_gro,
        output_ndx_path=output_complex_ndx,
        properties=prop)



# Create prop dict and inputs/outputs
# output_gppnvt_tpr = pdbCode+'_'+ligandCode+'gppnvt.tpr'
output_gppnvt_tpr = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_gppnvt.tpr"


# In[18]:


posresifdef = "POSRES_"+ligandCode.upper()


# In[19]:


prop = {
    'mdp':{
        'nsteps':'5000',
        'tc-grps': 'Protein_Other Water_and_ions',
        'Define': '-DPOSRES -D' + posresifdef
    },
    'simulation_type':'nvt'
}



# Create and launch bb
grompp(input_gro_path=output_min_gro,
       input_top_zip_path=output_genion_top_zip,
       input_ndx_path=output_complex_ndx,
       output_tpr_path=output_gppnvt_tpr,
       properties=prop)



# Create prop dict and inputs/outputs
output_nvt_trr = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_nvt.trr"
output_nvt_gro = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_nvt.gro"
output_nvt_edr = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_nvt.edr"
output_nvt_log = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_nvt.log"
output_nvt_cpt = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_nvt.cpt"



mdrun(input_tpr_path=output_gppnvt_tpr,    
        output_trr_path=output_nvt_trr,    
        output_gro_path=output_nvt_gro,     
        output_edr_path=output_nvt_edr,     
        output_log_path=output_nvt_log,     
        output_cpt_path=output_nvt_cpt)



# Create prop dict and inputs/outputs
output_nvt_temp_xvg = f"../files/{ligandCode}/figures/{pdbCode}_{ligandCode}_nvt_temp.xvg"

#output_nvt_temp_xvg = pdbCode+'_'+ligandCode+'_nvt_temp.xvg'
prop = {
    'terms':  ["Temperature"]
}

# Create and launch bb
gmx_energy(input_energy_path=output_nvt_edr, 
          output_xvg_path=output_nvt_temp_xvg, 
          properties=prop)



# Create prop dict and inputs/outputs
output_gppnpt_tpr = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_gppnpt.tpr"
# output_gppnpt_tpr = pdbCode+'_'+ligandCode+'_gppnpt.tpr'


# In[28]:


prop = {
    'mdp':{
        'type': 'npt',
        'nsteps':'5000',
        'tc-grps': 'Protein_Other Water_and_ions',
        'Define': '-DPOSRES -D' + posresifdef
    },
    'simulation_type':'npt'
}



# Create and launch bb
grompp(input_gro_path=output_nvt_gro,
       input_top_zip_path=output_genion_top_zip,
       input_ndx_path=output_complex_ndx,
       output_tpr_path=output_gppnpt_tpr,
       input_cpt_path=output_nvt_cpt,
       properties=prop)


# In[30]:


# Create prop dict and inputs/outputs
output_npt_trr = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_npt.trr"
output_npt_gro = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_npt.gro"
output_npt_edr = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_npt.edr"
output_npt_log = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_npt.log"
output_npt_cpt = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_npt.cpt"


# Create and launch bb\n
mdrun(input_tpr_path=output_gppnpt_tpr,
      output_trr_path=output_npt_trr,
      output_gro_path=output_npt_gro,      
      output_edr_path=output_npt_edr,      
      output_log_path=output_npt_log,      
      output_cpt_path=output_npt_cpt)


# In[33]:


# Create prop dict and inputs/outputs
output_npt_pd_xvg = f"../files/{ligandCode}/figures/{pdbCode}_{ligandCode}_npt_PD.xvg"
#output_npt_pd_xvg = pdbCode+'_'+ligandCode+'_npt_PD.xvg'
prop = {
    'terms':  ["Pressure","Density"]
}

# Create and launch bb
gmx_energy(input_energy_path=output_npt_edr, 
          output_xvg_path=output_npt_pd_xvg, 
          properties=prop)



# Create prop dict and inputs/outputs
prop = {
    'mdp':{
        'nsteps':'50000000' # 100 ns (50,000,000 steps x 2fs per step)
        #'nsteps':'500000' # 1 ns (500,000 steps x 2fs per step)
        #'nsteps':'5000' # 10 ps (5,000 steps x 2fs per step)
#         'nsteps':'25000' # 50 ps (25,000 steps x 2fs per step)
    },
    'simulation_type':'free'
}


# In[39]:


# output_gppmd_tpr = pdbCode+'_'+ligandCode + '_gppmd.tpr'
output_gppmd_tpr = f"../files/{ligandCode}/{pdbCode}_{ligandCode}_gppmd.tpr"


# In[40]:


# Create and launch bb
grompp(input_gro_path=output_npt_gro,
       input_top_zip_path=output_genion_top_zip,
       output_tpr_path=output_gppmd_tpr,
       input_cpt_path=output_npt_cpt,
       properties=prop)



def clean_WS(): 
    erase_log_files = [ x for x in os.listdir(".") if "log" == x[0:3]]
    for x in erase_log_files:
        if os.path.isfile(x) : 
            os.remove(x)
            
    print (len (erase_log_files))


clean_WS()

