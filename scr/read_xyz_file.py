# import openbabel as ob
from openbabel import openbabel as ob

obConversion = ob.OBConversion()
obConversion.SetInAndOutFormats( "xyz", "xyz")

obmol = ob.OBMol()
obConversion.ReadFile(obmol,"../files/dd.xyz")

obmol.CorrectForPH()
# obmol.AddHydrogens()
# print (obmol.NumAtoms())
# print (obmol.NumBonds())


print ('Before')
print (obmol.NumAtoms())

obmol.AddHydrogens()
print ('After')
print (obmol.NumAtoms())

outMDL = obConversion.WriteFile(obmol,"../files/dd2.xyz")
