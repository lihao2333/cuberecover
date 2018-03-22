#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import re
import pycuber as pc 
def getcolors(cmd):
    mycube = pc.Cube()
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
        cube.append(value) 
    re.sub('(?P<value>\[[a-z]\])', f_cube, s_cube)
    final_dic = {}
    for i in range(54):
        final_dic[dic[i]] = cube[i]
    print(final_dic)
getcolors("")
