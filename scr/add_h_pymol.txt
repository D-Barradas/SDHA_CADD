from pymol import cmd

cmd.load("../files/dd.xyz")
cmd.h_add()
cmd.exporting.save(filename="../files/dd.pdb",format="pdb")
# cmd.save("../files/dd.pdb",format="pdb")