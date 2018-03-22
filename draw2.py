import matplotlib
import matplotlib.pyplot as plt

from matplotlib.patches import Polygon
import re
import pycuber as pc 
def f_dic(matched):
    value = matched.group('value')
    value = value[1:-1]
    dic.append(value)
def f_cube(matched):
    value = matched.group('value')
    value = value[1:-1]
    value = {'r':'red','b':'blue','w':'white','o':'orange','y':'yellow','g':'green'}[value]
    cube.append(value) 
def getcolors(mycube,cmd):
    mycube(cmd)
    s_cube = str(mycube)
    s_dic = '''
                 [U1][U2][U3]
                 [U4][U5][U6]
                 [U7][U8][U9]
     [L1][L2][L3][F1][F2][F3][R1][R2][R3][B1][B2][B3]
     [L4][L5][L6][F4][F5][F6][R4][R5][R6][B4][B5][B6]
     [L7][L8][L9][F7][F8][F9][R7][R8][R9][B7][B8][B9]
                 [D1][D2][D3]
                 [D4][D5][D6]
                 [D7][D8][D9]
    '''
    dic = []
    cube = []
    def f_dic(matched):
        value = matched.group('value')
        value = value[1:-1]
        dic.append(value)
    re.sub('(?P<value>\[[A-Z]\d])', f_dic, s_dic)
    def f_cube(matched):
        value = matched.group('value')
        value = value[1:-1]
        value = {'r':'red','b':'blue','w':'white','o':'orange','y':'yellow','g':'green'}[value]
        cube.append(value) 
    re.sub('(?P<value>\[[a-z]\])', f_cube, s_cube)
    final_dic = {}
    for i in range(54):
        final_dic[dic[i]] = cube[i]
    return final_dic

colortab={
        "U":"yellow",
        "D":"white",
        "F":"green",
        "R":"orange",
        "B":"blue",
        "L":"red",
        }
def genpointsA(base):
    points = []
    for j in (2,1,0):
        for i in range(3):
            points.append((base[0]+i*a,base[1]+j*a))
    return points
def genpointsB(base):
    points = []
    for j in (2,1,0):
        for i in range(3):
            points.append([(base[0]+i*a+j*b,base[1]+j*b),
                    (base[0]+i*a+(j+1)*b,base[1]+(j+1)*b),
                    (base[0]+(i+1)*a+(j+1)*b,base[1]+(j+1)*b),
                    (base[0]+(i+1)*a+j*b,base[1]+j*b)])
    return points
def genpointsC(base):
    points = []
    for j in (2,1,0):
        for i in range(3):
            points.append([
                    (base[0]+i*b,base[1]+j*a+i*b),
                    (base[0]+i*b,base[1]+(j+1)*a+i*b),
                    (base[0]+(i+1)*b,base[1]+(j+1)*a+(i+1)*b),
                    (base[0]+(i+1)*b,base[1]+j*a+(i+1)*b),
                    ])
    return points
    
ox=10
oy=10
a=2
b=a/1.414
edgecolor="#000000"
rects = []
fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlim([0, 30])
plt.ylim([0, 30])

points = genpointsA((ox,oy))
for i in range(9):
    rect = matplotlib.patches.Rectangle(points[i], a, a, edgecolor=edgecolor,facecolor="#FFFFFF")
    rects.append(rect)
    ax.add_patch(rect)
points = genpointsB((ox,oy+3*a))
for i in range(9):
    rect = Polygon((points[i][0],points[i][1],points[i][2],points[i][3]),True, edgecolor=edgecolor,facecolor="#FFFFFF")
    rects.append(rect)
    ax.add_patch(rect)
points = genpointsC((ox+3*a,oy))

s_dic = '''
             [U1][U2][U3]
             [U4][U5][U6]
             [U7][U8][U9]
 [L1][L2][L3][F1][F2][F3][R1][R2][R3][B1][B2][B3]
 [L4][L5][L6][F4][F5][F6][R4][R5][R6][B4][B5][B6]
 [L7][L8][L9][F7][F8][F9][R7][R8][R9][B7][B8][B9]
             [D1][D2][D3]
             [D4][D5][D6]
             [D7][D8][D9]
'''
dic = []
re.sub('(?P<value>\[[A-Z]\d])', f_dic, s_dic)

for i in range(9):
    rect = Polygon((points[i][0],points[i][1],points[i][2],points[i][3]),True, edgecolor=edgecolor,facecolor="#FFFFFF")
    rects.append(rect)
    ax.add_patch(rect)
cmds = "R R R R".split(" ")
mycube = pc.Cube()
for no,cmd in enumerate(cmds):
    mycube(cmd)
    s_cube = str(mycube)
    cube = []
    re.sub('(?P<value>\[[a-z]\])', f_cube, s_cube)
    color_dic = {}
    for i in range(54):
        color_dic[dic[i]] = cube[i]
    for i in range(9):
        rects[i].set_facecolor(color_dic[['F1','F2','F3','F4','F5','F6','F7','F8','F9'][i]])
    for i in range(9):
        rects[i+9].set_facecolor(color_dic[['U1','U2','U3','U4','U5','U6','U7','U8','U9'][i]])
    for i in range(9):
        rects[i+18].set_facecolor(color_dic[['R1','R2','R3','R4','R5','R6','R7','R8','R9'][i]])
    plt.savefig("cmd_{0}.jpg".format(no))
