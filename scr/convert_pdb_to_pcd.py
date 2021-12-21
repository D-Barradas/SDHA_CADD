from color_constant import *

pdb_path = '../files/6vax.pdb'
pcd_path = '../files/6vax.pcd'

RES_3=['ALA','CYS','ASP','GLU','PHE','GLY','HIS','ILE','LYS','LEU','MET','ASN','PRO','GLN','ARG','SER','THR','VAL','TRP',       'TYR','HID','CYX']
RES_1=['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y','H','C']

print (colors["khaki"]) 
## source from https://web.njit.edu/~walsh/rgb.html
# colors = [
# (184,115,51),  
# (217,135,25),  
# (133,99,99),   
# (181,166,66),
# (140,120,83),
# (166,125,61	),  
# (217,217,25),
# (207,181,59),
# (204,153,0),
# (205,127,50),
# (230,232,250),
# (192,192,192),
# (84,84,84),
# (35,107,142),
# (35,142,35),
# (209,146,117),
# (79,79,47),
# (35,142,104),
# (2,157,116),
# (205,198,115),
# (47,79,47),
# (142,35,35)
# ]

names = ['aliceblue', 'antiquewhite', 'antiquewhite1', 'antiquewhite2', 'antiquewhite3', 'antiquewhite4', 'aqua', 
'aquamarine1', 'aquamarine2', 'aquamarine3', 'aquamarine4', 'azure1', 'azure2', 'azure3', 'azure4', 'banana', 
'beige', 'bisque1', 'bisque2', 'bisque3', 'bisque4', 'black', 'blanchedalmond', 'blue', 'blue2', 'blue3', 'blue4', 
'blueviolet', 'brick', 'brown', 'brown1', 'brown2', 'brown3', 'brown4', 'burlywood', 'burlywood1', 'burlywood2', 
'burlywood3', 'burlywood4', 'burntsienna', 'burntumber', 'cadetblue', 'cadetblue1', 'cadetblue2', 'cadetblue3', 
'cadetblue4', 'cadmiumorange', 'cadmiumyellow', 'carrot', 'chartreuse1', 'chartreuse2', 'chartreuse3', 'chartreuse4',
'chocolate', 'chocolate1', 'chocolate2', 'chocolate3', 'chocolate4', 'cobalt', 'cobaltgreen', 'coldgrey', 'coral',
'coral1', 'coral2', 'coral3', 'coral4', 'cornflowerblue', 'cornsilk1', 'cornsilk2', 'cornsilk3', 'cornsilk4', 
'crimson', 'cyan2', 'cyan3', 'cyan4', 'darkgoldenrod', 'darkgoldenrod1', 'darkgoldenrod2', 'darkgoldenrod3', 
'darkgoldenrod4', 'darkgray', 'darkgreen', 'darkkhaki', 'darkolivegreen', 'darkolivegreen1', 'darkolivegreen2', 
'darkolivegreen3', 'darkolivegreen4', 'darkorange', 'darkorange1', 'darkorange2', 'darkorange3', 'darkorange4', 
'darkorchid', 'darkorchid1', 'darkorchid2', 'darkorchid3', 'darkorchid4', 'darksalmon', 'darkseagreen', 
'darkseagreen1', 'darkseagreen2', 'darkseagreen3', 'darkseagreen4', 'darkslateblue', 'darkslategray', 
'darkslategray1', 'darkslategray2', 'darkslategray3', 'darkslategray4', 'darkturquoise', 'darkviolet', 'deeppink1',
'deeppink2', 'deeppink3', 'deeppink4', 'deepskyblue1', 'deepskyblue2', 'deepskyblue3', 'deepskyblue4', 'dimgray',
'dodgerblue1', 'dodgerblue2', 'dodgerblue3', 'dodgerblue4', 'eggshell', 'emeraldgreen', 'firebrick', 'firebrick1',
'firebrick2', 'firebrick3', 'firebrick4', 'flesh', 'floralwhite', 'forestgreen', 'gainsboro', 'ghostwhite', 
'gold1', 'gold2', 'gold3', 'gold4', 'goldenrod', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'gray',
'gray1', 'gray10', 'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 
'gray2', 'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 
'gray3', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 
'gray4', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray5', 
'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray6', 
'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray7', 
'gray70', 'gray71', 'gray72', 'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray8', 
'gray80', 'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray9', 
'gray90', 'gray91', 'gray92', 'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99', 'green', 'green1', 
'green2', 'green3', 'green4', 'greenyellow', 'honeydew1', 'honeydew2', 'honeydew3', 'honeydew4', 'hotpink', 
'hotpink1', 'hotpink2', 'hotpink3', 'hotpink4', 'indianred', 'indianred1', 'indianred2', 'indianred3', 
'indianred4', 'indigo', 'ivory1', 'ivory2', 'ivory3', 'ivory4', 'ivoryblack', 'khaki', 'khaki1', 'khaki2',
'khaki3', 'khaki4', 'lavender', 'lavenderblush1', 'lavenderblush2', 'lavenderblush3', 'lavenderblush4', 
'lawngreen', 'lemonchiffon1', 'lemonchiffon2', 'lemonchiffon3', 'lemonchiffon4', 'lightblue', 'lightblue1', 
'lightblue2', 'lightblue3', 'lightblue4', 'lightcoral', 'lightcyan1', 'lightcyan2', 'lightcyan3', 'lightcyan4', 
'lightgoldenrod1', 'lightgoldenrod2', 'lightgoldenrod3', 'lightgoldenrod4', 'lightgoldenrodyellow', 'lightgrey', 
'lightpink', 'lightpink1', 'lightpink2', 'lightpink3', 'lightpink4', 'lightsalmon1', 'lightsalmon2', 
'lightsalmon3', 'lightsalmon4', 'lightseagreen', 'lightskyblue', 'lightskyblue1', 'lightskyblue2', 
'lightskyblue3', 'lightskyblue4', 'lightslateblue', 'lightslategray', 'lightsteelblue', 'lightsteelblue1', 
'lightsteelblue2', 'lightsteelblue3', 'lightsteelblue4', 'lightyellow1', 'lightyellow2', 'lightyellow3', 
'lightyellow4', 'limegreen', 'linen', 'magenta', 'magenta2', 'magenta3', 'magenta4', 'manganeseblue', 'maroon', 
'maroon1', 'maroon2', 'maroon3', 'maroon4', 'mediumorchid', 'mediumorchid1', 'mediumorchid2', 'mediumorchid3', 
'mediumorchid4', 'mediumpurple', 'mediumpurple1', 'mediumpurple2', 'mediumpurple3', 'mediumpurple4', 
'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'melon', 
'midnightblue', 'mint', 'mintcream', 'mistyrose1', 'mistyrose2', 'mistyrose3', 'mistyrose4', 'moccasin', 
'navajowhite1', 'navajowhite2', 'navajowhite3', 'navajowhite4', 'navy', 'oldlace', 'olive', 'olivedrab', 
'olivedrab1', 'olivedrab2', 'olivedrab3', 'olivedrab4', 'orange', 'orange1', 'orange2', 'orange3', 'orange4', 
'orangered1', 'orangered2', 'orangered3', 'orangered4', 'orchid', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 
'palegoldenrod', 'palegreen', 'palegreen1', 'palegreen2', 'palegreen3', 'palegreen4', 'paleturquoise1', 
'paleturquoise2', 'paleturquoise3', 'paleturquoise4', 'palevioletred', 'palevioletred1', 'palevioletred2', 
'palevioletred3', 'palevioletred4', 'papayawhip', 'peachpuff1', 'peachpuff2', 'peachpuff3', 'peachpuff4', 
'peacock', 'pink', 'pink1', 'pink2', 'pink3', 'pink4', 'plum', 'plum1', 'plum2', 'plum3', 'plum4', 'powderblue',
'purple', 'purple1', 'purple2', 'purple3', 'purple4', 'raspberry', 'rawsienna', 'red1', 'red2', 'red3', 'red4',
'rosybrown', 'rosybrown1', 'rosybrown2', 'rosybrown3', 'rosybrown4', 'royalblue', 'royalblue1', 'royalblue2',
'royalblue3', 'royalblue4', 'salmon', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'sandybrown', 'sapgreen',
'seagreen1', 'seagreen2', 'seagreen3', 'seagreen4', 'seashell1', 'seashell2', 'seashell3', 'seashell4', 
'sepia', 'sgibeet', 'sgibrightgray', 'sgichartreuse', 'sgidarkgray', 'sgigray12', 'sgigray16', 'sgigray32',
'sgigray36', 'sgigray52', 'sgigray56', 'sgigray72', 'sgigray76', 'sgigray92', 'sgigray96', 'sgilightblue', 
'sgilightgray', 'sgiolivedrab', 'sgisalmon', 'sgislateblue', 'sgiteal', 'sienna', 'sienna1', 'sienna2', 
'sienna3', 'sienna4', 'silver', 'skyblue', 'skyblue1', 'skyblue2', 'skyblue3', 'skyblue4', 'slateblue', 
'slateblue1', 'slateblue2', 'slateblue3', 'slateblue4', 'slategray', 'slategray1', 'slategray2', 
'slategray3', 'slategray4', 'snow1', 'snow2', 'snow3', 'snow4', 'springgreen', 'springgreen1', 
'springgreen2', 'springgreen3', 'steelblue', 'steelblue1', 'steelblue2', 'steelblue3', 'steelblue4', 
'tan', 'tan1', 'tan2', 'tan3', 'tan4', 'teal', 'thistle', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 
'tomato1', 'tomato2', 'tomato3', 'tomato4', 'turquoise', 'turquoise1', 'turquoise2', 'turquoise3', 
'turquoise4', 'turquoiseblue', 'violet', 'violetred', 'violetred1', 'violetred2', 'violetred3', 'violetred4', 
'warmgrey', 'wheat', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'white', 'whitesmoke', 'yellow1', 'yellow2', 'yellow3', 
'yellow4']

all_atms=['N','CA','C','O',
          'CB','CG','CD','CD1','CD2','CE1','CE2','CE3','CZ2','CZ3','CH2','CG1','CG2','CZ','CE','OXT',  
          'ND', 'ND1','ND2','NE1','NZ','NE','NE2','NH1','NH2','OD1','OD2','OE1','OE2','OG','OG1','OH','SD',
          'SG','S','SE','SEG'
          ]
print (colors["aqua"], "all_atms:", len(all_atms), colors["aqua"][0])
## make a dictionary using Residue name as key and color as value
color_dict = {}
for i in range(len(RES_3)):
    color_dict[RES_3[i]] = names[i]

# ## make a dictionary using atom name from all_atm as key and color as value
color_dict_atm = {}
for i in range(len(all_atms)):
    color_dict_atm[all_atms[i]] = names[i]

# print (len(RES_3))

#read the pdb file , and store the coordinates in a list
with open(pdb_path, 'r') as f:
    lines = f.readlines()
    x, y, z , res, atm  = [] , [] , [] ,[] ,[]
    for line in lines:
        if line[0:4] == 'ATOM':
            x.append(float(line[30:38]))
            y.append(float(line[38:46]))
            z.append(float(line[46:54]))
            res.append(line[17:20])
            # atm.append(line[77])
            atm.append(line[12:16])

header = """# .PCD v.7 - Point Cloud Data file format
VERSION .7
FIELDS x y z rgb
SIZE 4 4 4 4 4 4
TYPE F F F F F F
COUNT 1 1 1 1 1 1
WIDTH 1
HEIGHT XXXX
VIEWPOINT 0 0 0 1 0 0 0
POINTS XXXX
DATA ascii
"""
num_of_points = len(x)
# print (header.replace('XXXX', str(num_of_points)))

# for a, b, c ,r, t in zip(x,y,z,res, atm ):
#     print(a,b,c, color_dict[r], t)

## write the pcd file
with open(pcd_path, 'w') as f:
    f.write(header.replace('XXXX', str(num_of_points)))
    for a, b, c ,r, t in zip(x,y,z,res, atm ):
        # print ( t.split()[0] ) 
        f.write(str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + 
        str(colors[color_dict[r]][0]) + ' ' +
        str(colors[color_dict[r]][1]) + ' ' + 
        str(colors[color_dict[r]][2]) + '\n')

        ### this is for atom color
        # f.write(str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + 
        # str(colors [ color_dict_atm[t.split()[0] ] ] [0 ] ) + ' ' +
        # str(colors [ color_dict_atm[t.split()[0] ] ] [1 ] ) + ' ' + 
        # str(colors [ color_dict_atm[t.split()[0] ] ] [-1] )  + '\n')

# for a, b, c ,r, t in zip(x,y,z,res, atm ):
#     print(a,b,c, color_dict[r][0], color_dict[r][1], color_dict[r][2])