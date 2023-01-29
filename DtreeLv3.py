import numpy as np
from Dtreefunc import *
from Preprocessing import *
import pandas as pd


def findmaxgainLv3L2(dataset):  
    M=3 #row

    a1=np.zeros(2)
    a1CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of A1)

    a2=np.zeros(4) 
    a2CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A2)

    a3=np.zeros(4) #wait for generate range
    a3CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of age)

    a4=np.zeros(4)
    a4CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of age)

    a5=np.zeros(3)
    a5CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of age)

    a6=np.zeros(14)
    a6CI=[[0 for i in range(M)] for j in range(14)] # zero matrix 14 rows 3 columns (class and info gain of age)

    a7=np.zeros(9)
    a7CI=[[0 for i in range(M)] for j in range(9)] # zero matrix 9 rows 3 columns (class and info gain of age)

    a8=np.zeros(4)          # zero array for count sample in A8 
    a8CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A8)

    a10=np.zeros(2)
    a10CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of age)

    a11=np.zeros(2) #wait to generate range
    a11CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of age)

    a12=np.zeros(2)
    a12CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of age)

    a13=np.zeros(3)
    a13CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of age)


    a15=np.zeros(3) #wait to generate change
    a15CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of age)

    a16=np.zeros(2) 

    #วน loop เพื่อนับข้อมูล แยกตามรายละเอียด attb และ class
    for i in range(0,len(dataset)):
        #A1
        if (dataset.iloc[i][0] == 'b'):  #A1 = 'b'   
            a1[0]+=1 # total sample A1 = 'b'
            if (dataset.iloc[i][0] == 'b') and (dataset.iloc[i][15] == '+'):
                a1CI[0][0]+=1 #class +
            else:
                a1CI[0][1]+=1 #class -
        elif(dataset.iloc[i][0] == 'a'):    #A1 = 'a'
            a1[1]+=1 # total sample A1 = 'a'
            if (dataset.iloc[i][0] == 'a') and (dataset.iloc[i][15] == '+'):
                a1CI[1][0]+=1 #class +
            else:
                a1CI[1][1]+=1 #class -

        #A2
        if (float(dataset.iloc[i][1]) <= 25):   
            a2[0]+=1 # total sample A2 <=25
            if (float(dataset.iloc[i][1]) <= 25) and (dataset.iloc[i][15] == '+'):
                a2CI[0][0]+=1 #A2 <= 25 and class +
            else:
                a2CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][1]) >25 and float(dataset.iloc[i][1])<=30): 
            a2[1]+=1 # total sample 25 < A2 <= 30 
            if (float(dataset.iloc[i][1]) >25 and float(dataset.iloc[i][1])<=30) and (dataset.iloc[i][15] == '+'):
                a2CI[1][0]+=1 #25 < A2 <= 30  and class +
            else:
                a2CI[1][1]+=1 #25 < A2 <= 30 and class -
        elif(float(dataset.iloc[i][1]) > 30 and float(dataset.iloc[i][1])<=40): 
            a2[2]+=1 # total sample 30 < A2 <= 40
            if (float(dataset.iloc[i][1]) > 30 and float(dataset.iloc[i][1])<=40) and (dataset.iloc[i][15] == '+'):
                a2CI[2][0]+=1 #30 < A2 <= 40 and class +
            else:
                a2CI[2][1]+=1 #class -
        elif(float(dataset.iloc[i][1]) > 40): 
            a2[3]+=1 # total sample A2>40
            if (float(dataset.iloc[i][1]) > 40) and (dataset.iloc[i][15] == '+'):
                a2CI[3][0]+=1 #A2>40 and class +
            else:
                a2CI[3][1]+=1 #class -

        #A3
        if (float(dataset.iloc[i][2]) <=1): 
            a3[0]+=1 # total sample A3<=1
            if (float(dataset.iloc[i][2]) <=1) and (dataset.iloc[i][15] == '+'):
                a3CI[0][0]+=1 #class +
            else:
                a3CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][2]) >1 and float(dataset.iloc[i][2])<=3): 
            a3[1]+=1 # total sample >1 A3<=3
            if (float(dataset.iloc[i][2]) >1 and float(dataset.iloc[i][2])<=3) and (dataset.iloc[i][15] == '+'):
                a3CI[1][0]+=1 #class +
            else:
                a3CI[1][1]+=1 #class -
        elif(float(dataset.iloc[i][2]) > 3 and float(dataset.iloc[i][2])<=8): 
            a3[2]+=1 # total sample 3 > A3 <=8
            if (float(dataset.iloc[i][2]) > 3 and float(dataset.iloc[i][2])<=8) and (dataset.iloc[i][15] == '+'):
                a3CI[2][0]+=1 #class +
            else:
                a3CI[2][1]+=1 #class -
        elif(float(dataset.iloc[i][2]) > 8): 
            a3[3]+=1 # total sample A3>8
            if (float(dataset.iloc[i][2]) > 8) and (dataset.iloc[i][15] == '+'):
                a3CI[3][0]+=1 #class +
            else:
                a3CI[3][1]+=1 #class -
        
            
        #A4
        if (dataset.iloc[i][3] == 'u'): 
            a4[0]+=1 # total sample A4 = u
            if (dataset.iloc[i][3] == 'u') and (dataset.iloc[i][15] == '+'):
                a4CI[0][0]+=1 #count A4 = u and class +
            else:
                a4CI[0][1]+=1 #class -
        elif(dataset.iloc[i][3] == 'y'): 
            a4[1]+=1 # total sample A4 = y
            if (dataset.iloc[i][3] == 'y') and (dataset.iloc[i][15] == '+'):
                a4CI[1][0]+=1 #count A4 = y and class +
            else:
                a4CI[1][1]+=1 #class -
        elif(dataset.iloc[i][3] == 'l'): 
            a4[2]+=1 # total sample A4 = l
            if (dataset.iloc[i][3] == 'l') and (dataset.iloc[i][15] == '+'):
                a4CI[2][0]+=1 #count A4 = l and class +
            else:
                a4CI[2][1]+=1 #class -
        elif(dataset.iloc[i][3] == 't'): 
            a4[3]+=1 # total sample A4 = t
            if (dataset.iloc[i][3] == 't') and (dataset.iloc[i][15] == '+'):
                a4CI[3][0]+=1 #count A4 = t and class +
            else:
                a4CI[3][1]+=1 #class -

        #A5
        if (dataset.iloc[i][4] == 'g'): 
            a5[0]+=1 # total sample A5 = g
            if (dataset.iloc[i][4] == 'g') and (dataset.iloc[i][15] == '+'):
                a5CI[0][0]+=1 #class +
            else:
                a5CI[0][1]+=1 #class -
        elif(dataset.iloc[i][4] == 'p'): 
            a5[1]+=1 # total sample A5 = p
            if (dataset.iloc[i][4] == 'p') and (dataset.iloc[i][15] == '+'):
                a5CI[1][0]+=1 #class +
            else:
                a5CI[1][1]+=1 #class -
        elif(dataset.iloc[i][4] == 'gg'): 
            a5[2]+=1 # total sample A5 = gg
            if (dataset.iloc[i][4] == 'gg') and (dataset.iloc[i][15] == '+'):
                a5CI[2][0]+=1 #class +
            else:
                a5CI[2][1]+=1 #class -

        #A6
        if (dataset.iloc[i][5] == 'c'): 
            a6[0]+=1 # total sample A6 = c
            if (dataset.iloc[i][5] == 'c') and (dataset.iloc[i][15] == '+'):
                a6CI[0][0]+=1 #class +
            else:
                a6CI[0][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'd'): 
            a6[1]+=1 # total sample A6 = d
            if (dataset.iloc[i][5] == 'd') and (dataset.iloc[i][15] == '+'):
                a6CI[1][0]+=1 #class +
            else:
                a6CI[1][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'cc'): 
            a6[2]+=1 # total sample A6 = cc
            if (dataset.iloc[i][5] == 'cc') and (dataset.iloc[i][15] == '+'):
                a6CI[2][0]+=1 #class +
            else:
                a6CI[2][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'i'): 
            a6[3]+=1 # total sample A6 = i
            if (dataset.iloc[i][5] == 'i') and (dataset.iloc[i][15] == '+'):
                a6CI[3][0]+=1 #class +
            else:
                a6CI[3][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'j'): 
            a6[4]+=1 # total sample A6 = j
            if (dataset.iloc[i][5] == 'j') and (dataset.iloc[i][15] == '+'):
                a6CI[4][0]+=1 #class +
            else:
                a6CI[4][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'k'): 
            a6[5]+=1 # total sample A6 = k
            if (dataset.iloc[i][5] == 'k') and (dataset.iloc[i][15] == '+'):
                a6CI[5][0]+=1 #class +
            else:
                a6CI[5][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'm'): 
            a6[6]+=1 # total sample A6 = m
            if (dataset.iloc[i][5] == 'm') and (dataset.iloc[i][15] == '+'):
                a6CI[6][0]+=1 #class +
            else:
                a6CI[6][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'r'): 
            a6[7]+=1 # total sample A6 = r
            if (dataset.iloc[i][5] == 'r') and (dataset.iloc[i][15] == '+'):
                a6CI[7][0]+=1 #class +
            else:
                a6CI[7][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'q'): 
            a6[8]+=1 # total sample A6 = q
            if (dataset.iloc[i][5] == 'q') and (dataset.iloc[i][15] == '+'):
                a6CI[8][0]+=1 #class +
            else:
                a6CI[8][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'w'): 
            a6[9]+=1 # total sample A6 = w
            if (dataset.iloc[i][5] == 'w') and (dataset.iloc[i][15] == '+'):
                a6CI[9][0]+=1 #class +
            else:
                a6CI[9][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'x'): 
            a6[10]+=1 # total sample A6 = x
            if (dataset.iloc[i][5] == 'x') and (dataset.iloc[i][15] == '+'):
                a6CI[10][0]+=1 #class +
            else:
                a6CI[10][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'e'): 
            a6[11]+=1 # total sample A6 = e
            if (dataset.iloc[i][5] == 'e') and (dataset.iloc[i][15] == '+'):
                a6CI[11][0]+=1 #class +
            else:
                a6CI[11][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'aa'): 
            a6[12]+=1 # total sample A6 = aa
            if (dataset.iloc[i][5] == 'aa') and (dataset.iloc[i][15] == '+'):
                a6CI[12][0]+=1 #class +
            else:
                a6CI[12][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'ff'): 
            a6[13]+=1 # total sample A6 = ff
            if (dataset.iloc[i][5] == 'ff') and (dataset.iloc[i][15] == '+'):
                a6CI[13][0]+=1 #class +
            else:
                a6CI[13][1]+=1 #class -

        #A7
        if (dataset.iloc[i][6] == 'v'): 
            a7[0]+=1 # total sample A6 = v
            if (dataset.iloc[i][6] == 'v') and (dataset.iloc[i][15] == '+'):
                a7CI[0][0]+=1 #class +
            else:
                a7CI[0][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'h'): 
            a7[1]+=1 # total sample A6 = h
            if (dataset.iloc[i][6] == 'h') and (dataset.iloc[i][15] == '+'):
                a7CI[1][0]+=1 #class +
            else:
                a7CI[1][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'bb'): 
            a7[2]+=1 # total sample A6 = bb
            if (dataset.iloc[i][6] == 'bb') and (dataset.iloc[i][15] == '+'):
                a7CI[2][0]+=1 #class +
            else:
                a7CI[2][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'j'): 
            a7[3]+=1 # total sample A6 = j
            if (dataset.iloc[i][6] == 'j') and (dataset.iloc[i][15] == '+'):
                a7CI[3][0]+=1 #class +
            else:
                a7CI[3][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'n'): 
            a7[4]+=1 # total sample A6 = n
            if (dataset.iloc[i][6] == 'n') and (dataset.iloc[i][15] == '+'):
                a7CI[4][0]+=1 #class +
            else:
                a7CI[4][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'z'): 
            a7[5]+=1 # total sample A6 = z
            if (dataset.iloc[i][6] == 'z') and (dataset.iloc[i][15] == '+'):
                a7CI[5][0]+=1 #class +
            else:
                a7CI[5][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'dd'): 
            a7[6]+=1 # total sample A6 = dd
            if (dataset.iloc[i][6] == 'dd') and (dataset.iloc[i][15] == '+'):
                a7CI[6][0]+=1 #class +
            else:
                a7CI[6][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'ff'): 
            a7[7]+=1 # total sample A6 = ff
            if (dataset.iloc[i][6] == 'ff') and (dataset.iloc[i][15] == '+'):
                a7CI[7][0]+=1 #class +
            else:
                a7CI[7][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'o'): 
            a7[8]+=1 # total sample A6 = o
            if (dataset.iloc[i][6] == 'o') and (dataset.iloc[i][15] == '+'):
                a7CI[8][0]+=1 #class +
            else:
                a7CI[8][1]+=1 #class -
        
        #A8
        if (float(dataset.iloc[i][7]) <= 0.2): 
            a8[0]+=1 # total sample A8<=0.2
            if (float(dataset.iloc[i][7]) <= 0.2) and (dataset.iloc[i][15] == '+'):
                a8CI[0][0]+=1 #class +
            else:
                a8CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][7]) >0.2 and float(dataset.iloc[i][7])<=1): 
            a8[1]+=1 # total sample 0.2 < A8 <= 1
            if (float(dataset.iloc[i][7]) >0.2 and float(dataset.iloc[i][7])<=1) and (dataset.iloc[i][15] == '+'):
                a8CI[1][0]+=1 #class +
            else:
                a8CI[1][1]+=1 #class -
        elif(float(dataset.iloc[i][7]) >1 and float(dataset.iloc[i][7])<=3): 
            a8[2]+=1 # total sample 1 < A8 <= 3
            if (float(dataset.iloc[i][7]) >1 and float(dataset.iloc[i][7])<=3) and (dataset.iloc[i][15] == '+'):
                a8CI[2][0]+=1 #class +
            else:
                a8CI[2][1]+=1 #class -
        elif(float(dataset.iloc[i][7]) > 3): 
            a8[3]+=1 # total sample  A8 >3
            if (float(dataset.iloc[i][7]) > 3) and (dataset.iloc[i][15] == '+'):
                a8CI[3][0]+=1 #class +
            else:
                a8CI[3][1]+=1 #class -

        #A9
        #upper level

        #A10
        if (dataset.iloc[i][9] == 't'): 
            a10[0]+=1 # total sample A10 = t
            if (dataset.iloc[i][9] == 't') and (dataset.iloc[i][15] == '+'):
                a10CI[0][0]+=1 #class +
            else:
                a10CI[0][1]+=1 #class -
        elif (dataset.iloc[i][9] == 'f'): 
            a10[1]+=1 # total sample A10 = f
            if (dataset.iloc[i][9] == 'f') and (dataset.iloc[i][15] == '+'):
                a10CI[1][0]+=1 #class +
            else:
                a10CI[1][1]+=1 #class -

        #A11
        if (float(dataset.iloc[i][10]) <= 3): 
            a11[0]+=1 # total sample A11<=3
            if (float(dataset.iloc[i][10]) <= 3) and (dataset.iloc[i][15] == '+'):
                a11CI[0][0]+=1 #class +
            else:
                a11CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][10]) >3): 
            a11[1]+=1 # total sample A11>3
            if (float(dataset.iloc[i][10]) >3) and (dataset.iloc[i][15] == '+'):
                a11CI[1][0]+=1 #class +
            else:
                a11CI[1][1]+=1 #class -
        

        #A12
        if (dataset.iloc[i][11] == 't'): 
            a12[0]+=1 # total sample A12 = t
            if (dataset.iloc[i][11] == 't') and (dataset.iloc[i][15] == '+'):
                a12CI[0][0]+=1 #class +
            else:
                a12CI[0][1]+=1 #class -
        elif (dataset.iloc[i][11] == 'f'): 
            a12[1]+=1 # total sample A12 = t
            if (dataset.iloc[i][11] == 'f') and (dataset.iloc[i][15] == '+'):
                a12CI[1][0]+=1 #class +
            else:
                a12CI[1][1]+=1 #class -

        #A13
        if (dataset.iloc[i][12] == 'g'): 
            a13[0]+=1 # total sample A13 = g
            if (dataset.iloc[i][12] == 'g') and (dataset.iloc[i][15] == '+'):
                a13CI[0][0]+=1 #class +
            else:
                a13CI[0][1]+=1 #class -
        elif (dataset.iloc[i][12] == 'p'): 
            a13[1]+=1 # total sample A13 = p
            if (dataset.iloc[i][12] == 'p') and (dataset.iloc[i][15] == '+'):
                a13CI[1][0]+=1 #class +
            else:
                a13CI[1][1]+=1 #class -
        elif (dataset.iloc[i][12] == 's'): 
            a13[2]+=1 # total sample A13 = s
            if (dataset.iloc[i][12] == 's') and (dataset.iloc[i][15] == '+'):
                a13CI[2][0]+=1 #class +
            else:
                a13CI[2][1]+=1 #class -

        #A14
        #This level

        #A15
        if (float(dataset.iloc[i][14]) <= 5): 
            a15[0]+=1 # total sample A15<=5
            if (float(dataset.iloc[i][14]) <= 5) and (dataset.iloc[i][15] == '+'):
                a15CI[0][0]+=1 #class +
            else:
                a15CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][14]) > 5 and float(dataset.iloc[i][14]) <=395): 
            a15[1]+=1 # total sample 5<A15<=395
            if (float(dataset.iloc[i][14]) > 5 and float(dataset.iloc[i][14]) <=395) and (dataset.iloc[i][15] == '+'):
                a15CI[1][0]+=1 #class +
            else:
                a15CI[1][1]+=1 #class -
        elif (float(dataset.iloc[i][14]) > 395): 
            a15[2]+=1 # total sample A15 > 395
            if (float(dataset.iloc[i][14]) >395) and (dataset.iloc[i][15] == '+'):
                a15CI[2][0]+=1 #class +
            else:
                a15CI[2][1]+=1 #class -
        

        #A16
        if (dataset.iloc[i][15] == '+'): 
            a16[0]+=1 # total sample A16 = +
        elif (dataset.iloc[i][15] == '-'): 
            a16[1]+=1 # total sample A16 = -



    # calculate information gain of dataset and attb
    # base on class
    # calculate Info(D)
    InD=entropy(a16[1],a16[0])

    # calculate each attribute's Info
    # calculate entropy all catagaries of A1
    a1CI[0][2] = entropy(a1CI[0][0],a1CI[0][1])
    a1CI[1][2] = entropy(a1CI[1][0],a1CI[1][1])

    # calculate entropy all catagaries of A2
    a2CI[0][2] = entropy(a2CI[0][0],a2CI[0][1])
    a2CI[1][2] = entropy(a2CI[1][0],a2CI[1][1])
    a2CI[2][2] = entropy(a2CI[2][0],a2CI[2][1])
    a2CI[3][2] = entropy(a2CI[3][0],a2CI[3][1])

    # calculate entropy all catagaries of A3
    a3CI[0][2] = entropy(a3CI[0][0],a3CI[0][1])
    a3CI[1][2] = entropy(a3CI[1][0],a3CI[1][1])
    a3CI[2][2] = entropy(a3CI[2][0],a3CI[2][1])
    a3CI[3][2] = entropy(a3CI[3][0],a3CI[3][1])

    # calculate entropy all catagaries of A4
    a4CI[0][2] = entropy(a4CI[0][0],a4CI[0][1])
    a4CI[1][2] = entropy(a4CI[1][0],a4CI[1][1])
    a4CI[2][2] = entropy(a4CI[2][0],a4CI[2][1])
    a4CI[3][2] = entropy(a4CI[3][0],a4CI[3][1])

    # calculate entropy all catagaries of A5
    a5CI[0][2] = entropy(a5CI[0][0],a5CI[0][1])
    a5CI[1][2] = entropy(a5CI[1][0],a5CI[1][1])
    a5CI[2][2] = entropy(a5CI[2][0],a5CI[2][1])

    # calculate entropy all catagaries of A6
    a6CI[0][2] = entropy(a6CI[0][0],a6CI[0][1])
    a6CI[1][2] = entropy(a6CI[1][0],a6CI[1][1])
    a6CI[2][2] = entropy(a6CI[2][0],a6CI[2][1])
    a6CI[3][2] = entropy(a6CI[3][0],a6CI[3][1])
    a6CI[4][2] = entropy(a6CI[4][0],a6CI[4][1])
    a6CI[5][2] = entropy(a6CI[5][0],a6CI[5][1])
    a6CI[6][2] = entropy(a6CI[6][0],a6CI[6][1])
    a6CI[7][2] = entropy(a6CI[7][0],a6CI[7][1])
    a6CI[8][2] = entropy(a6CI[8][0],a6CI[8][1])
    a6CI[9][2] = entropy(a6CI[9][0],a6CI[9][1])
    a6CI[10][2] = entropy(a6CI[10][0],a6CI[10][1])
    a6CI[11][2] = entropy(a6CI[11][0],a6CI[11][1])
    a6CI[12][2] = entropy(a6CI[12][0],a6CI[12][1])
    a6CI[13][2] = entropy(a6CI[13][0],a6CI[13][1])

    # calculate entropy all catagaries of A7
    a7CI[0][2] = entropy(a7CI[0][0],a7CI[0][1])
    a7CI[1][2] = entropy(a7CI[1][0],a7CI[1][1])
    a7CI[2][2] = entropy(a7CI[2][0],a7CI[2][1])
    a7CI[3][2] = entropy(a7CI[3][0],a7CI[3][1])
    a7CI[4][2] = entropy(a7CI[4][0],a7CI[4][1])
    a7CI[5][2] = entropy(a7CI[5][0],a7CI[5][1])
    a7CI[6][2] = entropy(a7CI[6][0],a7CI[6][1])
    a7CI[7][2] = entropy(a7CI[7][0],a7CI[7][1])
    a7CI[8][2] = entropy(a7CI[8][0],a7CI[8][1])

    # calculate entropy all catagaries of A8
    a8CI[0][2] = entropy(a8CI[0][0],a8CI[0][1])
    a8CI[1][2] = entropy(a8CI[1][0],a8CI[1][1])
    a8CI[2][2] = entropy(a8CI[2][0],a8CI[2][1])
    a8CI[3][2] = entropy(a8CI[3][0],a8CI[3][1])

    # calculate entropy all catagaries of A9
    # a9CI[0][2] = entropy(a9CI[0][0],a9CI[0][1])
    # a9CI[1][2] = entropy(a9CI[1][0],a9CI[1][1])

    # calculate entropy all catagaries of A10
    a10CI[0][2] = entropy(a10CI[0][0],a10CI[0][1])
    a10CI[1][2] = entropy(a10CI[1][0],a10CI[1][1])

    # calculate entropy all catagaries of A11
    a11CI[0][2] = entropy(a11CI[0][0],a11CI[0][1])
    a11CI[1][2] = entropy(a11CI[1][0],a11CI[1][1])

    # calculate entropy all catagaries of A12
    a12CI[0][2] = entropy(a12CI[0][0],a12CI[0][1])
    a12CI[1][2] = entropy(a12CI[1][0],a12CI[1][1])

    # calculate entropy all catagaries of A13
    a13CI[0][2] = entropy(a13CI[0][0],a13CI[0][1])
    a13CI[1][2] = entropy(a13CI[1][0],a13CI[1][1])
    a13CI[2][2] = entropy(a13CI[2][0],a13CI[2][1])

    # calculate entropy all catagaries of A14
    # a14CI[0][2] = entropy(a14CI[0][0],a14CI[0][1])
    # a14CI[1][2] = entropy(a14CI[1][0],a14CI[1][1])
    # a14CI[2][2] = entropy(a14CI[2][0],a14CI[2][1])
    # a14CI[3][2] = entropy(a14CI[3][0],a14CI[3][1])
    # a14CI[4][2] = entropy(a14CI[4][0],a14CI[4][1])
    # a14CI[5][2] = entropy(a14CI[5][0],a14CI[5][1])
    # a14CI[6][2] = entropy(a14CI[6][0],a14CI[6][1])
    # a14CI[7][2] = entropy(a14CI[7][0],a14CI[7][1])
    # a14CI[8][2] = entropy(a14CI[8][0],a14CI[8][1])
    # a14CI[9][2] = entropy(a14CI[9][0],a14CI[9][1])
    # a14CI[10][2] = entropy(a14CI[10][0],a14CI[10][1])
    # a14CI[11][2] = entropy(a14CI[11][0],a14CI[11][1])

    # calculate entropy all catagaries of A15
    a15CI[0][2] = entropy(a15CI[0][0],a15CI[0][1])
    a15CI[1][2] = entropy(a15CI[1][0],a15CI[1][1])
    a15CI[2][2] = entropy(a15CI[2][0],a15CI[2][1])



    # calculate Info 
    Info_A1 = inforD(a1,[a1CI[0][2],a1CI[1][2]])
    Info_A2 = inforD(a2,[a2CI[0][2],a2CI[1][2],a2CI[2][2],a2CI[3][2]]) 
    Info_A3 = inforD(a3,[a3CI[0][2],a3CI[1][2],a3CI[2][2],a3CI[3][2]]) 
    Info_A4 = inforD(a4,[a4CI[0][2],a4CI[1][2],a4CI[2][2],a4CI[3][2]])
    Info_A5 = inforD(a5,[a5CI[0][2],a5CI[1][2],a5CI[2][2]])
    Info_A6 = inforD(a6,[a6CI[0][2],a6CI[1][2],a6CI[2][2],a6CI[3][2],a6CI[4][2],a6CI[5][2],a6CI[6][2],a6CI[7][2],a6CI[8][2],a6CI[9][2],a6CI[10][2],a6CI[11][2],a6CI[12][2],a6CI[13][2]])
    Info_A7 = inforD(a7,[a7CI[0][2],a7CI[1][2],a7CI[2][2],a7CI[3][2],a7CI[4][2],a7CI[5][2],a7CI[6][2],a7CI[7][2],a7CI[8][2]])
    Info_A8 = inforD(a8,[a8CI[0][2],a8CI[1][2],a8CI[2][2],a8CI[3][2]]) 
    # Info_A9 = inforD(a9,[a9CI[0][2],a9CI[1][2]])
    Info_A10 = inforD(a10,[a10CI[0][2],a10CI[1][2]])
    Info_A11 = inforD(a11,[a11CI[0][2],a11CI[1][2]]) 
    Info_A12 = inforD(a12,[a12CI[0][2],a12CI[1][2]])
    Info_A13 = inforD(a13,[a13CI[0][2],a13CI[1][2],a13CI[2][2]])
    # Info_A14 = inforD(a14,[a14CI[0][2],a14CI[1][2],a14CI[2][2],a14CI[3][2],a14CI[4][2],a14CI[5][2],a14CI[6][2],a14CI[7][2],a14CI[8][2],a14CI[9][2],a14CI[10][2],a14CI[11][2]])
    Info_A15 = inforD(a15,[a15CI[0][2],a15CI[1][2],a15CI[2][2]]) 

    # แสดงผลการทำงานรอบแรก
    print("A1 count is", a1)
    print("A2 count is",a2)
    print("A3 count is",a3)
    print("A4 count is",a4)
    print("A5 count is", a5)
    print("A6 count is",a6)
    print("A7 count is", a7)
    print("A8 count is", a8)
    # print("A9 count is", a9)
    print("A10 count is", a10)
    print("A11 count is", a11)
    print("A12 count is", a12)
    print("A13 count is", a13)
    # print("A14 count is", a14)
    print("A15 count is", a15)
    print("A16 count is", a16)
    """

    """
    print("\n***Gain results of Lv.3 Left 2 dataset***")
    print("InD is %5.3f"% InD)
    gainA1=InD-Info_A1
    print("Gain (A1) is %5.3f"% gainA1)
    gainA2=InD-Info_A2
    print("Gain (A2) is %5.3f"% gainA2)
    gainA3=InD-Info_A3
    print("Gain (A3) is %5.3f"% gainA3)
    gainA4=InD-Info_A4
    print("Gain (A4) is %5.3f"% gainA4)
    gainA5=InD-Info_A5
    print("Gain (A5) is %5.3f"% gainA5)
    gainA6=InD-Info_A6
    print("Gain (A6) is %5.3f"% gainA6)
    gainA7=InD-Info_A7
    print("Gain (A7) is %5.3f"% gainA7)
    gainA8=InD-Info_A8
    print("Gain (A8) is %5.3f"% gainA8)
    # gainA9=InD-Info_A9
    # print("Gain (A9) is %5.3f"% gainA9)
    gainA10=InD-Info_A10
    print("Gain (A10) is %5.3f"% gainA10)
    gainA11=InD-Info_A11
    print("Gain (A11) is %5.3f"% gainA11)
    gainA12=InD-Info_A12
    print("Gain (A12) is %5.3f"% gainA12)
    gainA13=InD-Info_A13
    print("Gain (A13) is %5.3f"% gainA13)
    # gainA14=InD-Info_A14
    # print("Gain (A14) is %5.3f"% gainA14)
    gainA15=InD-Info_A15
    print("Gain (A15) is %5.3f"% gainA15)

    Result_All=[gainA1,gainA2,gainA3,gainA4,gainA5,gainA6,gainA7,gainA8,gainA10,gainA11,gainA12,gainA13,gainA15]
    max_gain=max(Result_All)    #find max gain
    pos=np.argmax(Result_All)   #position of max gain
    print("max gain of attb is %5.3f" % max_gain,"position is",pos)


    X4L11=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age <=30
    X4L12=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L13=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L14=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L15=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L16=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L17=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L18=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L19=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L110=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L111=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L112=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L113=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L114=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40


    for i in range(len(dataset)):
        if (dataset.iloc[i][5] == 'c'): 
            X4L11.append(dataset.iloc[i])
            
        elif(dataset.iloc[i][5] == 'd'): 
            X4L12.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'cc'): 
            X4L13.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'i'): 
            X4L14.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'j'): 
            X4L15.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'k'): 
            X4L16.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'm'): 
            X4L17.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'r'): 
            X4L18.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'q'): 
            X4L19.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'w'): 
            X4L110.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'x'): 
            X4L111.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'e'): 
            X4L112.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'aa'): 
            X4L113.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'ff'): 
            X4L114.append(dataset.iloc[i])
    crx4L11 = pd.DataFrame(X4L11)
    crx4L12 = pd.DataFrame(X4L12)
    crx4L13 = pd.DataFrame(X4L13)
    crx4L14 = pd.DataFrame(X4L14)
    crx4L15 = pd.DataFrame(X4L15)
    crx4L16 = pd.DataFrame(X4L16)
    crx4L17 = pd.DataFrame(X4L17)
    crx4L18 = pd.DataFrame(X4L18)
    crx4L19 = pd.DataFrame(X4L19)
    crx4L110 = pd.DataFrame(X4L110)
    crx4L111 = pd.DataFrame(X4L111)
    crx4L112 = pd.DataFrame(X4L112)
    crx4L113 = pd.DataFrame(X4L113)
    crx4L114 = pd.DataFrame(X4L114)
    

    crx4L11.to_csv('data/lv4/crx4L21.csv', index=False, header=False)
    crx4L12.to_csv('data/lv4/crx4L22.csv', index=False, header=False)
    crx4L13.to_csv('data/lv4/crx4L23.csv', index=False, header=False)
    crx4L14.to_csv('data/lv4/crx4L24.csv', index=False, header=False)
    crx4L15.to_csv('data/lv4/crx4L25.csv', index=False, header=False)
    crx4L16.to_csv('data/lv4/crx4L26.csv', index=False, header=False)
    crx4L17.to_csv('data/lv4/crx4L27.csv', index=False, header=False)
    crx4L18.to_csv('data/lv4/crx4L28.csv', index=False, header=False)
    crx4L19.to_csv('data/lv4/crx4L29.csv', index=False, header=False)
    crx4L110.to_csv('data/lv4/crx4L210.csv', index=False, header=False)
    crx4L111.to_csv('data/lv4/crx4L211.csv', index=False, header=False)
    crx4L112.to_csv('data/lv4/crx4L212.csv', index=False, header=False)
    crx4L113.to_csv('data/lv4/crx4L213.csv', index=False, header=False)
    crx4L114.to_csv('data/lv4/crx4L214.csv', index=False, header=False)
  





def findmaxgainLv3L3(dataset):  
    M=3 #row

    a1=np.zeros(2)
    a1CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of A1)

    a2=np.zeros(4) 
    a2CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A2)

    a3=np.zeros(4) #wait for generate range
    a3CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of age)

    a4=np.zeros(4)
    a4CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of age)

    a5=np.zeros(3)
    a5CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of age)

    a6=np.zeros(14)
    a6CI=[[0 for i in range(M)] for j in range(14)] # zero matrix 14 rows 3 columns (class and info gain of age)

    a7=np.zeros(9)
    a7CI=[[0 for i in range(M)] for j in range(9)] # zero matrix 9 rows 3 columns (class and info gain of age)

    a8=np.zeros(4)          # zero array for count sample in A8 
    a8CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A8)

    a10=np.zeros(2)
    a10CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of age)

    a11=np.zeros(2) #wait to generate range
    a11CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of age)

    a12=np.zeros(2)
    a12CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of age)

    a13=np.zeros(3)
    a13CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of age)


    a15=np.zeros(3) #wait to generate change
    a15CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of age)

    a16=np.zeros(2) 

    #วน loop เพื่อนับข้อมูล แยกตามรายละเอียด attb และ class
    for i in range(0,len(dataset)):
        #A1
        if (dataset.iloc[i][0] == 'b'):  #A1 = 'b'   
            a1[0]+=1 # total sample A1 = 'b'
            if (dataset.iloc[i][0] == 'b') and (dataset.iloc[i][15] == '+'):
                a1CI[0][0]+=1 #class +
            else:
                a1CI[0][1]+=1 #class -
        elif(dataset.iloc[i][0] == 'a'):    #A1 = 'a'
            a1[1]+=1 # total sample A1 = 'a'
            if (dataset.iloc[i][0] == 'a') and (dataset.iloc[i][15] == '+'):
                a1CI[1][0]+=1 #class +
            else:
                a1CI[1][1]+=1 #class -

        #A2
        if (float(dataset.iloc[i][1]) <= 25):   
            a2[0]+=1 # total sample A2 <=25
            if (float(dataset.iloc[i][1]) <= 25) and (dataset.iloc[i][15] == '+'):
                a2CI[0][0]+=1 #A2 <= 25 and class +
            else:
                a2CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][1]) >25 and float(dataset.iloc[i][1])<=30): 
            a2[1]+=1 # total sample 25 < A2 <= 30 
            if (float(dataset.iloc[i][1]) >25 and float(dataset.iloc[i][1])<=30) and (dataset.iloc[i][15] == '+'):
                a2CI[1][0]+=1 #25 < A2 <= 30  and class +
            else:
                a2CI[1][1]+=1 #25 < A2 <= 30 and class -
        elif(float(dataset.iloc[i][1]) > 30 and float(dataset.iloc[i][1])<=40): 
            a2[2]+=1 # total sample 30 < A2 <= 40
            if (float(dataset.iloc[i][1]) > 30 and float(dataset.iloc[i][1])<=40) and (dataset.iloc[i][15] == '+'):
                a2CI[2][0]+=1 #30 < A2 <= 40 and class +
            else:
                a2CI[2][1]+=1 #class -
        elif(float(dataset.iloc[i][1]) > 40): 
            a2[3]+=1 # total sample A2>40
            if (float(dataset.iloc[i][1]) > 40) and (dataset.iloc[i][15] == '+'):
                a2CI[3][0]+=1 #A2>40 and class +
            else:
                a2CI[3][1]+=1 #class -

        #A3
        if (float(dataset.iloc[i][2]) <=1): 
            a3[0]+=1 # total sample A3<=1
            if (float(dataset.iloc[i][2]) <=1) and (dataset.iloc[i][15] == '+'):
                a3CI[0][0]+=1 #class +
            else:
                a3CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][2]) >1 and float(dataset.iloc[i][2])<=3): 
            a3[1]+=1 # total sample >1 A3<=3
            if (float(dataset.iloc[i][2]) >1 and float(dataset.iloc[i][2])<=3) and (dataset.iloc[i][15] == '+'):
                a3CI[1][0]+=1 #class +
            else:
                a3CI[1][1]+=1 #class -
        elif(float(dataset.iloc[i][2]) > 3 and float(dataset.iloc[i][2])<=8): 
            a3[2]+=1 # total sample 3 > A3 <=8
            if (float(dataset.iloc[i][2]) > 3 and float(dataset.iloc[i][2])<=8) and (dataset.iloc[i][15] == '+'):
                a3CI[2][0]+=1 #class +
            else:
                a3CI[2][1]+=1 #class -
        elif(float(dataset.iloc[i][2]) > 8): 
            a3[3]+=1 # total sample A3>8
            if (float(dataset.iloc[i][2]) > 8) and (dataset.iloc[i][15] == '+'):
                a3CI[3][0]+=1 #class +
            else:
                a3CI[3][1]+=1 #class -
        
            
        #A4
        if (dataset.iloc[i][3] == 'u'): 
            a4[0]+=1 # total sample A4 = u
            if (dataset.iloc[i][3] == 'u') and (dataset.iloc[i][15] == '+'):
                a4CI[0][0]+=1 #count A4 = u and class +
            else:
                a4CI[0][1]+=1 #class -
        elif(dataset.iloc[i][3] == 'y'): 
            a4[1]+=1 # total sample A4 = y
            if (dataset.iloc[i][3] == 'y') and (dataset.iloc[i][15] == '+'):
                a4CI[1][0]+=1 #count A4 = y and class +
            else:
                a4CI[1][1]+=1 #class -
        elif(dataset.iloc[i][3] == 'l'): 
            a4[2]+=1 # total sample A4 = l
            if (dataset.iloc[i][3] == 'l') and (dataset.iloc[i][15] == '+'):
                a4CI[2][0]+=1 #count A4 = l and class +
            else:
                a4CI[2][1]+=1 #class -
        elif(dataset.iloc[i][3] == 't'): 
            a4[3]+=1 # total sample A4 = t
            if (dataset.iloc[i][3] == 't') and (dataset.iloc[i][15] == '+'):
                a4CI[3][0]+=1 #count A4 = t and class +
            else:
                a4CI[3][1]+=1 #class -

        #A5
        if (dataset.iloc[i][4] == 'g'): 
            a5[0]+=1 # total sample A5 = g
            if (dataset.iloc[i][4] == 'g') and (dataset.iloc[i][15] == '+'):
                a5CI[0][0]+=1 #class +
            else:
                a5CI[0][1]+=1 #class -
        elif(dataset.iloc[i][4] == 'p'): 
            a5[1]+=1 # total sample A5 = p
            if (dataset.iloc[i][4] == 'p') and (dataset.iloc[i][15] == '+'):
                a5CI[1][0]+=1 #class +
            else:
                a5CI[1][1]+=1 #class -
        elif(dataset.iloc[i][4] == 'gg'): 
            a5[2]+=1 # total sample A5 = gg
            if (dataset.iloc[i][4] == 'gg') and (dataset.iloc[i][15] == '+'):
                a5CI[2][0]+=1 #class +
            else:
                a5CI[2][1]+=1 #class -

        #A6
        if (dataset.iloc[i][5] == 'c'): 
            a6[0]+=1 # total sample A6 = c
            if (dataset.iloc[i][5] == 'c') and (dataset.iloc[i][15] == '+'):
                a6CI[0][0]+=1 #class +
            else:
                a6CI[0][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'd'): 
            a6[1]+=1 # total sample A6 = d
            if (dataset.iloc[i][5] == 'd') and (dataset.iloc[i][15] == '+'):
                a6CI[1][0]+=1 #class +
            else:
                a6CI[1][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'cc'): 
            a6[2]+=1 # total sample A6 = cc
            if (dataset.iloc[i][5] == 'cc') and (dataset.iloc[i][15] == '+'):
                a6CI[2][0]+=1 #class +
            else:
                a6CI[2][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'i'): 
            a6[3]+=1 # total sample A6 = i
            if (dataset.iloc[i][5] == 'i') and (dataset.iloc[i][15] == '+'):
                a6CI[3][0]+=1 #class +
            else:
                a6CI[3][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'j'): 
            a6[4]+=1 # total sample A6 = j
            if (dataset.iloc[i][5] == 'j') and (dataset.iloc[i][15] == '+'):
                a6CI[4][0]+=1 #class +
            else:
                a6CI[4][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'k'): 
            a6[5]+=1 # total sample A6 = k
            if (dataset.iloc[i][5] == 'k') and (dataset.iloc[i][15] == '+'):
                a6CI[5][0]+=1 #class +
            else:
                a6CI[5][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'm'): 
            a6[6]+=1 # total sample A6 = m
            if (dataset.iloc[i][5] == 'm') and (dataset.iloc[i][15] == '+'):
                a6CI[6][0]+=1 #class +
            else:
                a6CI[6][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'r'): 
            a6[7]+=1 # total sample A6 = r
            if (dataset.iloc[i][5] == 'r') and (dataset.iloc[i][15] == '+'):
                a6CI[7][0]+=1 #class +
            else:
                a6CI[7][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'q'): 
            a6[8]+=1 # total sample A6 = q
            if (dataset.iloc[i][5] == 'q') and (dataset.iloc[i][15] == '+'):
                a6CI[8][0]+=1 #class +
            else:
                a6CI[8][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'w'): 
            a6[9]+=1 # total sample A6 = w
            if (dataset.iloc[i][5] == 'w') and (dataset.iloc[i][15] == '+'):
                a6CI[9][0]+=1 #class +
            else:
                a6CI[9][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'x'): 
            a6[10]+=1 # total sample A6 = x
            if (dataset.iloc[i][5] == 'x') and (dataset.iloc[i][15] == '+'):
                a6CI[10][0]+=1 #class +
            else:
                a6CI[10][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'e'): 
            a6[11]+=1 # total sample A6 = e
            if (dataset.iloc[i][5] == 'e') and (dataset.iloc[i][15] == '+'):
                a6CI[11][0]+=1 #class +
            else:
                a6CI[11][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'aa'): 
            a6[12]+=1 # total sample A6 = aa
            if (dataset.iloc[i][5] == 'aa') and (dataset.iloc[i][15] == '+'):
                a6CI[12][0]+=1 #class +
            else:
                a6CI[12][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'ff'): 
            a6[13]+=1 # total sample A6 = ff
            if (dataset.iloc[i][5] == 'ff') and (dataset.iloc[i][15] == '+'):
                a6CI[13][0]+=1 #class +
            else:
                a6CI[13][1]+=1 #class -

        #A7
        if (dataset.iloc[i][6] == 'v'): 
            a7[0]+=1 # total sample A6 = v
            if (dataset.iloc[i][6] == 'v') and (dataset.iloc[i][15] == '+'):
                a7CI[0][0]+=1 #class +
            else:
                a7CI[0][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'h'): 
            a7[1]+=1 # total sample A6 = h
            if (dataset.iloc[i][6] == 'h') and (dataset.iloc[i][15] == '+'):
                a7CI[1][0]+=1 #class +
            else:
                a7CI[1][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'bb'): 
            a7[2]+=1 # total sample A6 = bb
            if (dataset.iloc[i][6] == 'bb') and (dataset.iloc[i][15] == '+'):
                a7CI[2][0]+=1 #class +
            else:
                a7CI[2][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'j'): 
            a7[3]+=1 # total sample A6 = j
            if (dataset.iloc[i][6] == 'j') and (dataset.iloc[i][15] == '+'):
                a7CI[3][0]+=1 #class +
            else:
                a7CI[3][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'n'): 
            a7[4]+=1 # total sample A6 = n
            if (dataset.iloc[i][6] == 'n') and (dataset.iloc[i][15] == '+'):
                a7CI[4][0]+=1 #class +
            else:
                a7CI[4][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'z'): 
            a7[5]+=1 # total sample A6 = z
            if (dataset.iloc[i][6] == 'z') and (dataset.iloc[i][15] == '+'):
                a7CI[5][0]+=1 #class +
            else:
                a7CI[5][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'dd'): 
            a7[6]+=1 # total sample A6 = dd
            if (dataset.iloc[i][6] == 'dd') and (dataset.iloc[i][15] == '+'):
                a7CI[6][0]+=1 #class +
            else:
                a7CI[6][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'ff'): 
            a7[7]+=1 # total sample A6 = ff
            if (dataset.iloc[i][6] == 'ff') and (dataset.iloc[i][15] == '+'):
                a7CI[7][0]+=1 #class +
            else:
                a7CI[7][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'o'): 
            a7[8]+=1 # total sample A6 = o
            if (dataset.iloc[i][6] == 'o') and (dataset.iloc[i][15] == '+'):
                a7CI[8][0]+=1 #class +
            else:
                a7CI[8][1]+=1 #class -
        
        #A8
        if (float(dataset.iloc[i][7]) <= 0.2): 
            a8[0]+=1 # total sample A8<=0.2
            if (float(dataset.iloc[i][7]) <= 0.2) and (dataset.iloc[i][15] == '+'):
                a8CI[0][0]+=1 #class +
            else:
                a8CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][7]) >0.2 and float(dataset.iloc[i][7])<=1): 
            a8[1]+=1 # total sample 0.2 < A8 <= 1
            if (float(dataset.iloc[i][7]) >0.2 and float(dataset.iloc[i][7])<=1) and (dataset.iloc[i][15] == '+'):
                a8CI[1][0]+=1 #class +
            else:
                a8CI[1][1]+=1 #class -
        elif(float(dataset.iloc[i][7]) >1 and float(dataset.iloc[i][7])<=3): 
            a8[2]+=1 # total sample 1 < A8 <= 3
            if (float(dataset.iloc[i][7]) >1 and float(dataset.iloc[i][7])<=3) and (dataset.iloc[i][15] == '+'):
                a8CI[2][0]+=1 #class +
            else:
                a8CI[2][1]+=1 #class -
        elif(float(dataset.iloc[i][7]) > 3): 
            a8[3]+=1 # total sample  A8 >3
            if (float(dataset.iloc[i][7]) > 3) and (dataset.iloc[i][15] == '+'):
                a8CI[3][0]+=1 #class +
            else:
                a8CI[3][1]+=1 #class -

        #A9
        #upper level

        #A10
        if (dataset.iloc[i][9] == 't'): 
            a10[0]+=1 # total sample A10 = t
            if (dataset.iloc[i][9] == 't') and (dataset.iloc[i][15] == '+'):
                a10CI[0][0]+=1 #class +
            else:
                a10CI[0][1]+=1 #class -
        elif (dataset.iloc[i][9] == 'f'): 
            a10[1]+=1 # total sample A10 = f
            if (dataset.iloc[i][9] == 'f') and (dataset.iloc[i][15] == '+'):
                a10CI[1][0]+=1 #class +
            else:
                a10CI[1][1]+=1 #class -

        #A11
        if (float(dataset.iloc[i][10]) <= 3): 
            a11[0]+=1 # total sample A11<=3
            if (float(dataset.iloc[i][10]) <= 3) and (dataset.iloc[i][15] == '+'):
                a11CI[0][0]+=1 #class +
            else:
                a11CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][10]) >3): 
            a11[1]+=1 # total sample A11>3
            if (float(dataset.iloc[i][10]) >3) and (dataset.iloc[i][15] == '+'):
                a11CI[1][0]+=1 #class +
            else:
                a11CI[1][1]+=1 #class -
        

        #A12
        if (dataset.iloc[i][11] == 't'): 
            a12[0]+=1 # total sample A12 = t
            if (dataset.iloc[i][11] == 't') and (dataset.iloc[i][15] == '+'):
                a12CI[0][0]+=1 #class +
            else:
                a12CI[0][1]+=1 #class -
        elif (dataset.iloc[i][11] == 'f'): 
            a12[1]+=1 # total sample A12 = t
            if (dataset.iloc[i][11] == 'f') and (dataset.iloc[i][15] == '+'):
                a12CI[1][0]+=1 #class +
            else:
                a12CI[1][1]+=1 #class -

        #A13
        if (dataset.iloc[i][12] == 'g'): 
            a13[0]+=1 # total sample A13 = g
            if (dataset.iloc[i][12] == 'g') and (dataset.iloc[i][15] == '+'):
                a13CI[0][0]+=1 #class +
            else:
                a13CI[0][1]+=1 #class -
        elif (dataset.iloc[i][12] == 'p'): 
            a13[1]+=1 # total sample A13 = p
            if (dataset.iloc[i][12] == 'p') and (dataset.iloc[i][15] == '+'):
                a13CI[1][0]+=1 #class +
            else:
                a13CI[1][1]+=1 #class -
        elif (dataset.iloc[i][12] == 's'): 
            a13[2]+=1 # total sample A13 = s
            if (dataset.iloc[i][12] == 's') and (dataset.iloc[i][15] == '+'):
                a13CI[2][0]+=1 #class +
            else:
                a13CI[2][1]+=1 #class -

        #A14
        #This level

        #A15
        if (float(dataset.iloc[i][14]) <= 5): 
            a15[0]+=1 # total sample A15<=5
            if (float(dataset.iloc[i][14]) <= 5) and (dataset.iloc[i][15] == '+'):
                a15CI[0][0]+=1 #class +
            else:
                a15CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][14]) > 5 and float(dataset.iloc[i][14]) <=395): 
            a15[1]+=1 # total sample 5<A15<=395
            if (float(dataset.iloc[i][14]) > 5 and float(dataset.iloc[i][14]) <=395) and (dataset.iloc[i][15] == '+'):
                a15CI[1][0]+=1 #class +
            else:
                a15CI[1][1]+=1 #class -
        elif (float(dataset.iloc[i][14]) > 395): 
            a15[2]+=1 # total sample A15 > 395
            if (float(dataset.iloc[i][14]) >395) and (dataset.iloc[i][15] == '+'):
                a15CI[2][0]+=1 #class +
            else:
                a15CI[2][1]+=1 #class -
        

        #A16
        if (dataset.iloc[i][15] == '+'): 
            a16[0]+=1 # total sample A16 = +
        elif (dataset.iloc[i][15] == '-'): 
            a16[1]+=1 # total sample A16 = -



    # calculate information gain of dataset and attb
    # base on class
    # calculate Info(D)
    InD=entropy(a16[1],a16[0])

    # calculate each attribute's Info
    # calculate entropy all catagaries of A1
    a1CI[0][2] = entropy(a1CI[0][0],a1CI[0][1])
    a1CI[1][2] = entropy(a1CI[1][0],a1CI[1][1])

    # calculate entropy all catagaries of A2
    a2CI[0][2] = entropy(a2CI[0][0],a2CI[0][1])
    a2CI[1][2] = entropy(a2CI[1][0],a2CI[1][1])
    a2CI[2][2] = entropy(a2CI[2][0],a2CI[2][1])
    a2CI[3][2] = entropy(a2CI[3][0],a2CI[3][1])

    # calculate entropy all catagaries of A3
    a3CI[0][2] = entropy(a3CI[0][0],a3CI[0][1])
    a3CI[1][2] = entropy(a3CI[1][0],a3CI[1][1])
    a3CI[2][2] = entropy(a3CI[2][0],a3CI[2][1])
    a3CI[3][2] = entropy(a3CI[3][0],a3CI[3][1])

    # calculate entropy all catagaries of A4
    a4CI[0][2] = entropy(a4CI[0][0],a4CI[0][1])
    a4CI[1][2] = entropy(a4CI[1][0],a4CI[1][1])
    a4CI[2][2] = entropy(a4CI[2][0],a4CI[2][1])
    a4CI[3][2] = entropy(a4CI[3][0],a4CI[3][1])

    # calculate entropy all catagaries of A5
    a5CI[0][2] = entropy(a5CI[0][0],a5CI[0][1])
    a5CI[1][2] = entropy(a5CI[1][0],a5CI[1][1])
    a5CI[2][2] = entropy(a5CI[2][0],a5CI[2][1])

    # calculate entropy all catagaries of A6
    a6CI[0][2] = entropy(a6CI[0][0],a6CI[0][1])
    a6CI[1][2] = entropy(a6CI[1][0],a6CI[1][1])
    a6CI[2][2] = entropy(a6CI[2][0],a6CI[2][1])
    a6CI[3][2] = entropy(a6CI[3][0],a6CI[3][1])
    a6CI[4][2] = entropy(a6CI[4][0],a6CI[4][1])
    a6CI[5][2] = entropy(a6CI[5][0],a6CI[5][1])
    a6CI[6][2] = entropy(a6CI[6][0],a6CI[6][1])
    a6CI[7][2] = entropy(a6CI[7][0],a6CI[7][1])
    a6CI[8][2] = entropy(a6CI[8][0],a6CI[8][1])
    a6CI[9][2] = entropy(a6CI[9][0],a6CI[9][1])
    a6CI[10][2] = entropy(a6CI[10][0],a6CI[10][1])
    a6CI[11][2] = entropy(a6CI[11][0],a6CI[11][1])
    a6CI[12][2] = entropy(a6CI[12][0],a6CI[12][1])
    a6CI[13][2] = entropy(a6CI[13][0],a6CI[13][1])

    # calculate entropy all catagaries of A7
    a7CI[0][2] = entropy(a7CI[0][0],a7CI[0][1])
    a7CI[1][2] = entropy(a7CI[1][0],a7CI[1][1])
    a7CI[2][2] = entropy(a7CI[2][0],a7CI[2][1])
    a7CI[3][2] = entropy(a7CI[3][0],a7CI[3][1])
    a7CI[4][2] = entropy(a7CI[4][0],a7CI[4][1])
    a7CI[5][2] = entropy(a7CI[5][0],a7CI[5][1])
    a7CI[6][2] = entropy(a7CI[6][0],a7CI[6][1])
    a7CI[7][2] = entropy(a7CI[7][0],a7CI[7][1])
    a7CI[8][2] = entropy(a7CI[8][0],a7CI[8][1])

    # calculate entropy all catagaries of A8
    a8CI[0][2] = entropy(a8CI[0][0],a8CI[0][1])
    a8CI[1][2] = entropy(a8CI[1][0],a8CI[1][1])
    a8CI[2][2] = entropy(a8CI[2][0],a8CI[2][1])
    a8CI[3][2] = entropy(a8CI[3][0],a8CI[3][1])

    # calculate entropy all catagaries of A9
    # a9CI[0][2] = entropy(a9CI[0][0],a9CI[0][1])
    # a9CI[1][2] = entropy(a9CI[1][0],a9CI[1][1])

    # calculate entropy all catagaries of A10
    a10CI[0][2] = entropy(a10CI[0][0],a10CI[0][1])
    a10CI[1][2] = entropy(a10CI[1][0],a10CI[1][1])

    # calculate entropy all catagaries of A11
    a11CI[0][2] = entropy(a11CI[0][0],a11CI[0][1])
    a11CI[1][2] = entropy(a11CI[1][0],a11CI[1][1])

    # calculate entropy all catagaries of A12
    a12CI[0][2] = entropy(a12CI[0][0],a12CI[0][1])
    a12CI[1][2] = entropy(a12CI[1][0],a12CI[1][1])

    # calculate entropy all catagaries of A13
    a13CI[0][2] = entropy(a13CI[0][0],a13CI[0][1])
    a13CI[1][2] = entropy(a13CI[1][0],a13CI[1][1])
    a13CI[2][2] = entropy(a13CI[2][0],a13CI[2][1])

    # calculate entropy all catagaries of A14
    # a14CI[0][2] = entropy(a14CI[0][0],a14CI[0][1])
    # a14CI[1][2] = entropy(a14CI[1][0],a14CI[1][1])
    # a14CI[2][2] = entropy(a14CI[2][0],a14CI[2][1])
    # a14CI[3][2] = entropy(a14CI[3][0],a14CI[3][1])
    # a14CI[4][2] = entropy(a14CI[4][0],a14CI[4][1])
    # a14CI[5][2] = entropy(a14CI[5][0],a14CI[5][1])
    # a14CI[6][2] = entropy(a14CI[6][0],a14CI[6][1])
    # a14CI[7][2] = entropy(a14CI[7][0],a14CI[7][1])
    # a14CI[8][2] = entropy(a14CI[8][0],a14CI[8][1])
    # a14CI[9][2] = entropy(a14CI[9][0],a14CI[9][1])
    # a14CI[10][2] = entropy(a14CI[10][0],a14CI[10][1])
    # a14CI[11][2] = entropy(a14CI[11][0],a14CI[11][1])

    # calculate entropy all catagaries of A15
    a15CI[0][2] = entropy(a15CI[0][0],a15CI[0][1])
    a15CI[1][2] = entropy(a15CI[1][0],a15CI[1][1])
    a15CI[2][2] = entropy(a15CI[2][0],a15CI[2][1])



    # calculate Info 
    Info_A1 = inforD(a1,[a1CI[0][2],a1CI[1][2]])
    Info_A2 = inforD(a2,[a2CI[0][2],a2CI[1][2],a2CI[2][2],a2CI[3][2]]) 
    Info_A3 = inforD(a3,[a3CI[0][2],a3CI[1][2],a3CI[2][2],a3CI[3][2]]) 
    Info_A4 = inforD(a4,[a4CI[0][2],a4CI[1][2],a4CI[2][2],a4CI[3][2]])
    Info_A5 = inforD(a5,[a5CI[0][2],a5CI[1][2],a5CI[2][2]])
    Info_A6 = inforD(a6,[a6CI[0][2],a6CI[1][2],a6CI[2][2],a6CI[3][2],a6CI[4][2],a6CI[5][2],a6CI[6][2],a6CI[7][2],a6CI[8][2],a6CI[9][2],a6CI[10][2],a6CI[11][2],a6CI[12][2],a6CI[13][2]])
    Info_A7 = inforD(a7,[a7CI[0][2],a7CI[1][2],a7CI[2][2],a7CI[3][2],a7CI[4][2],a7CI[5][2],a7CI[6][2],a7CI[7][2],a7CI[8][2]])
    Info_A8 = inforD(a8,[a8CI[0][2],a8CI[1][2],a8CI[2][2],a8CI[3][2]]) 
    # Info_A9 = inforD(a9,[a9CI[0][2],a9CI[1][2]])
    Info_A10 = inforD(a10,[a10CI[0][2],a10CI[1][2]])
    Info_A11 = inforD(a11,[a11CI[0][2],a11CI[1][2]]) 
    Info_A12 = inforD(a12,[a12CI[0][2],a12CI[1][2]])
    Info_A13 = inforD(a13,[a13CI[0][2],a13CI[1][2],a13CI[2][2]])
    # Info_A14 = inforD(a14,[a14CI[0][2],a14CI[1][2],a14CI[2][2],a14CI[3][2],a14CI[4][2],a14CI[5][2],a14CI[6][2],a14CI[7][2],a14CI[8][2],a14CI[9][2],a14CI[10][2],a14CI[11][2]])
    Info_A15 = inforD(a15,[a15CI[0][2],a15CI[1][2],a15CI[2][2]]) 

    # แสดงผลการทำงานรอบแรก
    print("A1 count is", a1)
    print("A2 count is",a2)
    print("A3 count is",a3)
    print("A4 count is",a4)
    print("A5 count is", a5)
    print("A6 count is",a6)
    print("A7 count is", a7)
    print("A8 count is", a8)
    # print("A9 count is", a9)
    print("A10 count is", a10)
    print("A11 count is", a11)
    print("A12 count is", a12)
    print("A13 count is", a13)
    # print("A14 count is", a14)
    print("A15 count is", a15)
    print("A16 count is", a16)
    """

    """
    print("\n***Gain results of Lv.3 Left 3 dataset***")
    print("InD is %5.3f"% InD)
    gainA1=InD-Info_A1
    print("Gain (A1) is %5.3f"% gainA1)
    gainA2=InD-Info_A2
    print("Gain (A2) is %5.3f"% gainA2)
    gainA3=InD-Info_A3
    print("Gain (A3) is %5.3f"% gainA3)
    gainA4=InD-Info_A4
    print("Gain (A4) is %5.3f"% gainA4)
    gainA5=InD-Info_A5
    print("Gain (A5) is %5.3f"% gainA5)
    gainA6=InD-Info_A6
    print("Gain (A6) is %5.3f"% gainA6)
    gainA7=InD-Info_A7
    print("Gain (A7) is %5.3f"% gainA7)
    gainA8=InD-Info_A8
    print("Gain (A8) is %5.3f"% gainA8)
    # gainA9=InD-Info_A9
    # print("Gain (A9) is %5.3f"% gainA9)
    gainA10=InD-Info_A10
    print("Gain (A10) is %5.3f"% gainA10)
    gainA11=InD-Info_A11
    print("Gain (A11) is %5.3f"% gainA11)
    gainA12=InD-Info_A12
    print("Gain (A12) is %5.3f"% gainA12)
    gainA13=InD-Info_A13
    print("Gain (A13) is %5.3f"% gainA13)
    # gainA14=InD-Info_A14
    # print("Gain (A14) is %5.3f"% gainA14)
    gainA15=InD-Info_A15
    print("Gain (A15) is %5.3f"% gainA15)

    Result_All=[gainA1,gainA2,gainA3,gainA4,gainA5,gainA6,gainA7,gainA8,gainA10,gainA11,gainA12,gainA13,gainA15]
    max_gain=max(Result_All)    #find max gain
    pos=np.argmax(Result_All)   #position of max gain
    print("max gain of attb is %5.3f" % max_gain,"position is",pos)
    


    X4L21=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age <=30
    X4L22=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L23=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L24=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L25=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L26=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L27=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L28=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L29=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L210=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L211=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L212=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L213=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L214=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40


    for i in range(len(dataset)):
        if (dataset.iloc[i][5] == 'c'): 
            X4L21.append(dataset.iloc[i])
            
        elif(dataset.iloc[i][5] == 'd'): 
            X4L22.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'cc'): 
            X4L23.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'i'): 
            X4L24.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'j'): 
            X4L25.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'k'): 
            X4L26.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'm'): 
            X4L27.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'r'): 
            X4L28.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'q'): 
            X4L29.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'w'): 
            X4L210.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'x'): 
            X4L211.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'e'): 
            X4L212.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'aa'): 
            X4L213.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'ff'): 
            X4L214.append(dataset.iloc[i])
  
    

    crx4L21 = pd.DataFrame(X4L21)
    crx4L22 = pd.DataFrame(X4L22)
    crx4L23 = pd.DataFrame(X4L23)
    crx4L24 = pd.DataFrame(X4L24)
    crx4L25 = pd.DataFrame(X4L25)
    crx4L26 = pd.DataFrame(X4L26)
    crx4L27 = pd.DataFrame(X4L27)
    crx4L28 = pd.DataFrame(X4L28)
    crx4L29 = pd.DataFrame(X4L29)
    crx4L210 = pd.DataFrame(X4L210)
    crx4L211 = pd.DataFrame(X4L211)
    crx4L212 = pd.DataFrame(X4L212)
    crx4L213 = pd.DataFrame(X4L213)
    crx4L214 = pd.DataFrame(X4L214)


    crx4L21.to_csv('data/lv4/crx4L31.csv', index=False, header=False)
    crx4L22.to_csv('data/lv4/crx4L32.csv', index=False, header=False)
    crx4L23.to_csv('data/lv4/crx4L33.csv', index=False, header=False)
    crx4L24.to_csv('data/lv4/crx4L34.csv', index=False, header=False)
    crx4L25.to_csv('data/lv4/crx4L35.csv', index=False, header=False)
    crx4L26.to_csv('data/lv4/crx4L36.csv', index=False, header=False)
    crx4L27.to_csv('data/lv4/crx4L37.csv', index=False, header=False)
    crx4L28.to_csv('data/lv4/crx4L38.csv', index=False, header=False)
    crx4L29.to_csv('data/lv4/crx4L39.csv', index=False, header=False)
    crx4L210.to_csv('data/lv4/crx4L310.csv', index=False, header=False)
    crx4L211.to_csv('data/lv4/crx4L311.csv', index=False, header=False)
    crx4L212.to_csv('data/lv4/crx4L312.csv', index=False, header=False)
    crx4L213.to_csv('data/lv4/crx4L313.csv', index=False, header=False)
    crx4L214.to_csv('data/lv4/crx4L314.csv', index=False, header=False)
    


def findmaxgainLv3L4(dataset):  
    M=3 #row

    a1=np.zeros(2)
    a1CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of A1)

    a2=np.zeros(4) 
    a2CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A2)

    a3=np.zeros(4) #wait for generate range
    a3CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of age)

    a4=np.zeros(4)
    a4CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of age)

    a5=np.zeros(3)
    a5CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of age)

    a6=np.zeros(14)
    a6CI=[[0 for i in range(M)] for j in range(14)] # zero matrix 14 rows 3 columns (class and info gain of age)

    a7=np.zeros(9)
    a7CI=[[0 for i in range(M)] for j in range(9)] # zero matrix 9 rows 3 columns (class and info gain of age)

    a8=np.zeros(4)          # zero array for count sample in A8 
    a8CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A8)

    a10=np.zeros(2)
    a10CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of age)

    a11=np.zeros(2) #wait to generate range
    a11CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of age)

    a12=np.zeros(2)
    a12CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of age)

    a13=np.zeros(3)
    a13CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of age)


    a15=np.zeros(3) #wait to generate change
    a15CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of age)

    a16=np.zeros(2) 

    #วน loop เพื่อนับข้อมูล แยกตามรายละเอียด attb และ class
    for i in range(0,len(dataset)):
        #A1
        if (dataset.iloc[i][0] == 'b'):  #A1 = 'b'   
            a1[0]+=1 # total sample A1 = 'b'
            if (dataset.iloc[i][0] == 'b') and (dataset.iloc[i][15] == '+'):
                a1CI[0][0]+=1 #class +
            else:
                a1CI[0][1]+=1 #class -
        elif(dataset.iloc[i][0] == 'a'):    #A1 = 'a'
            a1[1]+=1 # total sample A1 = 'a'
            if (dataset.iloc[i][0] == 'a') and (dataset.iloc[i][15] == '+'):
                a1CI[1][0]+=1 #class +
            else:
                a1CI[1][1]+=1 #class -

        #A2
        if (float(dataset.iloc[i][1]) <= 25):   
            a2[0]+=1 # total sample A2 <=25
            if (float(dataset.iloc[i][1]) <= 25) and (dataset.iloc[i][15] == '+'):
                a2CI[0][0]+=1 #A2 <= 25 and class +
            else:
                a2CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][1]) >25 and float(dataset.iloc[i][1])<=30): 
            a2[1]+=1 # total sample 25 < A2 <= 30 
            if (float(dataset.iloc[i][1]) >25 and float(dataset.iloc[i][1])<=30) and (dataset.iloc[i][15] == '+'):
                a2CI[1][0]+=1 #25 < A2 <= 30  and class +
            else:
                a2CI[1][1]+=1 #25 < A2 <= 30 and class -
        elif(float(dataset.iloc[i][1]) > 30 and float(dataset.iloc[i][1])<=40): 
            a2[2]+=1 # total sample 30 < A2 <= 40
            if (float(dataset.iloc[i][1]) > 30 and float(dataset.iloc[i][1])<=40) and (dataset.iloc[i][15] == '+'):
                a2CI[2][0]+=1 #30 < A2 <= 40 and class +
            else:
                a2CI[2][1]+=1 #class -
        elif(float(dataset.iloc[i][1]) > 40): 
            a2[3]+=1 # total sample A2>40
            if (float(dataset.iloc[i][1]) > 40) and (dataset.iloc[i][15] == '+'):
                a2CI[3][0]+=1 #A2>40 and class +
            else:
                a2CI[3][1]+=1 #class -

        #A3
        if (float(dataset.iloc[i][2]) <=1): 
            a3[0]+=1 # total sample A3<=1
            if (float(dataset.iloc[i][2]) <=1) and (dataset.iloc[i][15] == '+'):
                a3CI[0][0]+=1 #class +
            else:
                a3CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][2]) >1 and float(dataset.iloc[i][2])<=3): 
            a3[1]+=1 # total sample >1 A3<=3
            if (float(dataset.iloc[i][2]) >1 and float(dataset.iloc[i][2])<=3) and (dataset.iloc[i][15] == '+'):
                a3CI[1][0]+=1 #class +
            else:
                a3CI[1][1]+=1 #class -
        elif(float(dataset.iloc[i][2]) > 3 and float(dataset.iloc[i][2])<=8): 
            a3[2]+=1 # total sample 3 > A3 <=8
            if (float(dataset.iloc[i][2]) > 3 and float(dataset.iloc[i][2])<=8) and (dataset.iloc[i][15] == '+'):
                a3CI[2][0]+=1 #class +
            else:
                a3CI[2][1]+=1 #class -
        elif(float(dataset.iloc[i][2]) > 8): 
            a3[3]+=1 # total sample A3>8
            if (float(dataset.iloc[i][2]) > 8) and (dataset.iloc[i][15] == '+'):
                a3CI[3][0]+=1 #class +
            else:
                a3CI[3][1]+=1 #class -
        
            
        #A4
        if (dataset.iloc[i][3] == 'u'): 
            a4[0]+=1 # total sample A4 = u
            if (dataset.iloc[i][3] == 'u') and (dataset.iloc[i][15] == '+'):
                a4CI[0][0]+=1 #count A4 = u and class +
            else:
                a4CI[0][1]+=1 #class -
        elif(dataset.iloc[i][3] == 'y'): 
            a4[1]+=1 # total sample A4 = y
            if (dataset.iloc[i][3] == 'y') and (dataset.iloc[i][15] == '+'):
                a4CI[1][0]+=1 #count A4 = y and class +
            else:
                a4CI[1][1]+=1 #class -
        elif(dataset.iloc[i][3] == 'l'): 
            a4[2]+=1 # total sample A4 = l
            if (dataset.iloc[i][3] == 'l') and (dataset.iloc[i][15] == '+'):
                a4CI[2][0]+=1 #count A4 = l and class +
            else:
                a4CI[2][1]+=1 #class -
        elif(dataset.iloc[i][3] == 't'): 
            a4[3]+=1 # total sample A4 = t
            if (dataset.iloc[i][3] == 't') and (dataset.iloc[i][15] == '+'):
                a4CI[3][0]+=1 #count A4 = t and class +
            else:
                a4CI[3][1]+=1 #class -

        #A5
        if (dataset.iloc[i][4] == 'g'): 
            a5[0]+=1 # total sample A5 = g
            if (dataset.iloc[i][4] == 'g') and (dataset.iloc[i][15] == '+'):
                a5CI[0][0]+=1 #class +
            else:
                a5CI[0][1]+=1 #class -
        elif(dataset.iloc[i][4] == 'p'): 
            a5[1]+=1 # total sample A5 = p
            if (dataset.iloc[i][4] == 'p') and (dataset.iloc[i][15] == '+'):
                a5CI[1][0]+=1 #class +
            else:
                a5CI[1][1]+=1 #class -
        elif(dataset.iloc[i][4] == 'gg'): 
            a5[2]+=1 # total sample A5 = gg
            if (dataset.iloc[i][4] == 'gg') and (dataset.iloc[i][15] == '+'):
                a5CI[2][0]+=1 #class +
            else:
                a5CI[2][1]+=1 #class -

        #A6
        if (dataset.iloc[i][5] == 'c'): 
            a6[0]+=1 # total sample A6 = c
            if (dataset.iloc[i][5] == 'c') and (dataset.iloc[i][15] == '+'):
                a6CI[0][0]+=1 #class +
            else:
                a6CI[0][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'd'): 
            a6[1]+=1 # total sample A6 = d
            if (dataset.iloc[i][5] == 'd') and (dataset.iloc[i][15] == '+'):
                a6CI[1][0]+=1 #class +
            else:
                a6CI[1][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'cc'): 
            a6[2]+=1 # total sample A6 = cc
            if (dataset.iloc[i][5] == 'cc') and (dataset.iloc[i][15] == '+'):
                a6CI[2][0]+=1 #class +
            else:
                a6CI[2][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'i'): 
            a6[3]+=1 # total sample A6 = i
            if (dataset.iloc[i][5] == 'i') and (dataset.iloc[i][15] == '+'):
                a6CI[3][0]+=1 #class +
            else:
                a6CI[3][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'j'): 
            a6[4]+=1 # total sample A6 = j
            if (dataset.iloc[i][5] == 'j') and (dataset.iloc[i][15] == '+'):
                a6CI[4][0]+=1 #class +
            else:
                a6CI[4][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'k'): 
            a6[5]+=1 # total sample A6 = k
            if (dataset.iloc[i][5] == 'k') and (dataset.iloc[i][15] == '+'):
                a6CI[5][0]+=1 #class +
            else:
                a6CI[5][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'm'): 
            a6[6]+=1 # total sample A6 = m
            if (dataset.iloc[i][5] == 'm') and (dataset.iloc[i][15] == '+'):
                a6CI[6][0]+=1 #class +
            else:
                a6CI[6][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'r'): 
            a6[7]+=1 # total sample A6 = r
            if (dataset.iloc[i][5] == 'r') and (dataset.iloc[i][15] == '+'):
                a6CI[7][0]+=1 #class +
            else:
                a6CI[7][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'q'): 
            a6[8]+=1 # total sample A6 = q
            if (dataset.iloc[i][5] == 'q') and (dataset.iloc[i][15] == '+'):
                a6CI[8][0]+=1 #class +
            else:
                a6CI[8][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'w'): 
            a6[9]+=1 # total sample A6 = w
            if (dataset.iloc[i][5] == 'w') and (dataset.iloc[i][15] == '+'):
                a6CI[9][0]+=1 #class +
            else:
                a6CI[9][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'x'): 
            a6[10]+=1 # total sample A6 = x
            if (dataset.iloc[i][5] == 'x') and (dataset.iloc[i][15] == '+'):
                a6CI[10][0]+=1 #class +
            else:
                a6CI[10][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'e'): 
            a6[11]+=1 # total sample A6 = e
            if (dataset.iloc[i][5] == 'e') and (dataset.iloc[i][15] == '+'):
                a6CI[11][0]+=1 #class +
            else:
                a6CI[11][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'aa'): 
            a6[12]+=1 # total sample A6 = aa
            if (dataset.iloc[i][5] == 'aa') and (dataset.iloc[i][15] == '+'):
                a6CI[12][0]+=1 #class +
            else:
                a6CI[12][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'ff'): 
            a6[13]+=1 # total sample A6 = ff
            if (dataset.iloc[i][5] == 'ff') and (dataset.iloc[i][15] == '+'):
                a6CI[13][0]+=1 #class +
            else:
                a6CI[13][1]+=1 #class -

        #A7
        if (dataset.iloc[i][6] == 'v'): 
            a7[0]+=1 # total sample A6 = v
            if (dataset.iloc[i][6] == 'v') and (dataset.iloc[i][15] == '+'):
                a7CI[0][0]+=1 #class +
            else:
                a7CI[0][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'h'): 
            a7[1]+=1 # total sample A6 = h
            if (dataset.iloc[i][6] == 'h') and (dataset.iloc[i][15] == '+'):
                a7CI[1][0]+=1 #class +
            else:
                a7CI[1][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'bb'): 
            a7[2]+=1 # total sample A6 = bb
            if (dataset.iloc[i][6] == 'bb') and (dataset.iloc[i][15] == '+'):
                a7CI[2][0]+=1 #class +
            else:
                a7CI[2][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'j'): 
            a7[3]+=1 # total sample A6 = j
            if (dataset.iloc[i][6] == 'j') and (dataset.iloc[i][15] == '+'):
                a7CI[3][0]+=1 #class +
            else:
                a7CI[3][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'n'): 
            a7[4]+=1 # total sample A6 = n
            if (dataset.iloc[i][6] == 'n') and (dataset.iloc[i][15] == '+'):
                a7CI[4][0]+=1 #class +
            else:
                a7CI[4][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'z'): 
            a7[5]+=1 # total sample A6 = z
            if (dataset.iloc[i][6] == 'z') and (dataset.iloc[i][15] == '+'):
                a7CI[5][0]+=1 #class +
            else:
                a7CI[5][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'dd'): 
            a7[6]+=1 # total sample A6 = dd
            if (dataset.iloc[i][6] == 'dd') and (dataset.iloc[i][15] == '+'):
                a7CI[6][0]+=1 #class +
            else:
                a7CI[6][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'ff'): 
            a7[7]+=1 # total sample A6 = ff
            if (dataset.iloc[i][6] == 'ff') and (dataset.iloc[i][15] == '+'):
                a7CI[7][0]+=1 #class +
            else:
                a7CI[7][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'o'): 
            a7[8]+=1 # total sample A6 = o
            if (dataset.iloc[i][6] == 'o') and (dataset.iloc[i][15] == '+'):
                a7CI[8][0]+=1 #class +
            else:
                a7CI[8][1]+=1 #class -
        
        #A8
        if (float(dataset.iloc[i][7]) <= 0.2): 
            a8[0]+=1 # total sample A8<=0.2
            if (float(dataset.iloc[i][7]) <= 0.2) and (dataset.iloc[i][15] == '+'):
                a8CI[0][0]+=1 #class +
            else:
                a8CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][7]) >0.2 and float(dataset.iloc[i][7])<=1): 
            a8[1]+=1 # total sample 0.2 < A8 <= 1
            if (float(dataset.iloc[i][7]) >0.2 and float(dataset.iloc[i][7])<=1) and (dataset.iloc[i][15] == '+'):
                a8CI[1][0]+=1 #class +
            else:
                a8CI[1][1]+=1 #class -
        elif(float(dataset.iloc[i][7]) >1 and float(dataset.iloc[i][7])<=3): 
            a8[2]+=1 # total sample 1 < A8 <= 3
            if (float(dataset.iloc[i][7]) >1 and float(dataset.iloc[i][7])<=3) and (dataset.iloc[i][15] == '+'):
                a8CI[2][0]+=1 #class +
            else:
                a8CI[2][1]+=1 #class -
        elif(float(dataset.iloc[i][7]) > 3): 
            a8[3]+=1 # total sample  A8 >3
            if (float(dataset.iloc[i][7]) > 3) and (dataset.iloc[i][15] == '+'):
                a8CI[3][0]+=1 #class +
            else:
                a8CI[3][1]+=1 #class -

        #A9
        #upper level

        #A10
        if (dataset.iloc[i][9] == 't'): 
            a10[0]+=1 # total sample A10 = t
            if (dataset.iloc[i][9] == 't') and (dataset.iloc[i][15] == '+'):
                a10CI[0][0]+=1 #class +
            else:
                a10CI[0][1]+=1 #class -
        elif (dataset.iloc[i][9] == 'f'): 
            a10[1]+=1 # total sample A10 = f
            if (dataset.iloc[i][9] == 'f') and (dataset.iloc[i][15] == '+'):
                a10CI[1][0]+=1 #class +
            else:
                a10CI[1][1]+=1 #class -

        #A11
        if (float(dataset.iloc[i][10]) <= 3): 
            a11[0]+=1 # total sample A11<=3
            if (float(dataset.iloc[i][10]) <= 3) and (dataset.iloc[i][15] == '+'):
                a11CI[0][0]+=1 #class +
            else:
                a11CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][10]) >3): 
            a11[1]+=1 # total sample A11>3
            if (float(dataset.iloc[i][10]) >3) and (dataset.iloc[i][15] == '+'):
                a11CI[1][0]+=1 #class +
            else:
                a11CI[1][1]+=1 #class -
        

        #A12
        if (dataset.iloc[i][11] == 't'): 
            a12[0]+=1 # total sample A12 = t
            if (dataset.iloc[i][11] == 't') and (dataset.iloc[i][15] == '+'):
                a12CI[0][0]+=1 #class +
            else:
                a12CI[0][1]+=1 #class -
        elif (dataset.iloc[i][11] == 'f'): 
            a12[1]+=1 # total sample A12 = t
            if (dataset.iloc[i][11] == 'f') and (dataset.iloc[i][15] == '+'):
                a12CI[1][0]+=1 #class +
            else:
                a12CI[1][1]+=1 #class -

        #A13
        if (dataset.iloc[i][12] == 'g'): 
            a13[0]+=1 # total sample A13 = g
            if (dataset.iloc[i][12] == 'g') and (dataset.iloc[i][15] == '+'):
                a13CI[0][0]+=1 #class +
            else:
                a13CI[0][1]+=1 #class -
        elif (dataset.iloc[i][12] == 'p'): 
            a13[1]+=1 # total sample A13 = p
            if (dataset.iloc[i][12] == 'p') and (dataset.iloc[i][15] == '+'):
                a13CI[1][0]+=1 #class +
            else:
                a13CI[1][1]+=1 #class -
        elif (dataset.iloc[i][12] == 's'): 
            a13[2]+=1 # total sample A13 = s
            if (dataset.iloc[i][12] == 's') and (dataset.iloc[i][15] == '+'):
                a13CI[2][0]+=1 #class +
            else:
                a13CI[2][1]+=1 #class -

        #A14
        #This level

        #A15
        if (float(dataset.iloc[i][14]) <= 5): 
            a15[0]+=1 # total sample A15<=5
            if (float(dataset.iloc[i][14]) <= 5) and (dataset.iloc[i][15] == '+'):
                a15CI[0][0]+=1 #class +
            else:
                a15CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][14]) > 5 and float(dataset.iloc[i][14]) <=395): 
            a15[1]+=1 # total sample 5<A15<=395
            if (float(dataset.iloc[i][14]) > 5 and float(dataset.iloc[i][14]) <=395) and (dataset.iloc[i][15] == '+'):
                a15CI[1][0]+=1 #class +
            else:
                a15CI[1][1]+=1 #class -
        elif (float(dataset.iloc[i][14]) > 395): 
            a15[2]+=1 # total sample A15 > 395
            if (float(dataset.iloc[i][14]) >395) and (dataset.iloc[i][15] == '+'):
                a15CI[2][0]+=1 #class +
            else:
                a15CI[2][1]+=1 #class -
        

        #A16
        if (dataset.iloc[i][15] == '+'): 
            a16[0]+=1 # total sample A16 = +
        elif (dataset.iloc[i][15] == '-'): 
            a16[1]+=1 # total sample A16 = -



    # calculate information gain of dataset and attb
    # base on class
    # calculate Info(D)
    InD=entropy(a16[1],a16[0])

    # calculate each attribute's Info
    # calculate entropy all catagaries of A1
    a1CI[0][2] = entropy(a1CI[0][0],a1CI[0][1])
    a1CI[1][2] = entropy(a1CI[1][0],a1CI[1][1])

    # calculate entropy all catagaries of A2
    a2CI[0][2] = entropy(a2CI[0][0],a2CI[0][1])
    a2CI[1][2] = entropy(a2CI[1][0],a2CI[1][1])
    a2CI[2][2] = entropy(a2CI[2][0],a2CI[2][1])
    a2CI[3][2] = entropy(a2CI[3][0],a2CI[3][1])

    # calculate entropy all catagaries of A3
    a3CI[0][2] = entropy(a3CI[0][0],a3CI[0][1])
    a3CI[1][2] = entropy(a3CI[1][0],a3CI[1][1])
    a3CI[2][2] = entropy(a3CI[2][0],a3CI[2][1])
    a3CI[3][2] = entropy(a3CI[3][0],a3CI[3][1])

    # calculate entropy all catagaries of A4
    a4CI[0][2] = entropy(a4CI[0][0],a4CI[0][1])
    a4CI[1][2] = entropy(a4CI[1][0],a4CI[1][1])
    a4CI[2][2] = entropy(a4CI[2][0],a4CI[2][1])
    a4CI[3][2] = entropy(a4CI[3][0],a4CI[3][1])

    # calculate entropy all catagaries of A5
    a5CI[0][2] = entropy(a5CI[0][0],a5CI[0][1])
    a5CI[1][2] = entropy(a5CI[1][0],a5CI[1][1])
    a5CI[2][2] = entropy(a5CI[2][0],a5CI[2][1])

    # calculate entropy all catagaries of A6
    a6CI[0][2] = entropy(a6CI[0][0],a6CI[0][1])
    a6CI[1][2] = entropy(a6CI[1][0],a6CI[1][1])
    a6CI[2][2] = entropy(a6CI[2][0],a6CI[2][1])
    a6CI[3][2] = entropy(a6CI[3][0],a6CI[3][1])
    a6CI[4][2] = entropy(a6CI[4][0],a6CI[4][1])
    a6CI[5][2] = entropy(a6CI[5][0],a6CI[5][1])
    a6CI[6][2] = entropy(a6CI[6][0],a6CI[6][1])
    a6CI[7][2] = entropy(a6CI[7][0],a6CI[7][1])
    a6CI[8][2] = entropy(a6CI[8][0],a6CI[8][1])
    a6CI[9][2] = entropy(a6CI[9][0],a6CI[9][1])
    a6CI[10][2] = entropy(a6CI[10][0],a6CI[10][1])
    a6CI[11][2] = entropy(a6CI[11][0],a6CI[11][1])
    a6CI[12][2] = entropy(a6CI[12][0],a6CI[12][1])
    a6CI[13][2] = entropy(a6CI[13][0],a6CI[13][1])

    # calculate entropy all catagaries of A7
    a7CI[0][2] = entropy(a7CI[0][0],a7CI[0][1])
    a7CI[1][2] = entropy(a7CI[1][0],a7CI[1][1])
    a7CI[2][2] = entropy(a7CI[2][0],a7CI[2][1])
    a7CI[3][2] = entropy(a7CI[3][0],a7CI[3][1])
    a7CI[4][2] = entropy(a7CI[4][0],a7CI[4][1])
    a7CI[5][2] = entropy(a7CI[5][0],a7CI[5][1])
    a7CI[6][2] = entropy(a7CI[6][0],a7CI[6][1])
    a7CI[7][2] = entropy(a7CI[7][0],a7CI[7][1])
    a7CI[8][2] = entropy(a7CI[8][0],a7CI[8][1])

    # calculate entropy all catagaries of A8
    a8CI[0][2] = entropy(a8CI[0][0],a8CI[0][1])
    a8CI[1][2] = entropy(a8CI[1][0],a8CI[1][1])
    a8CI[2][2] = entropy(a8CI[2][0],a8CI[2][1])
    a8CI[3][2] = entropy(a8CI[3][0],a8CI[3][1])

    # calculate entropy all catagaries of A9
    # a9CI[0][2] = entropy(a9CI[0][0],a9CI[0][1])
    # a9CI[1][2] = entropy(a9CI[1][0],a9CI[1][1])

    # calculate entropy all catagaries of A10
    a10CI[0][2] = entropy(a10CI[0][0],a10CI[0][1])
    a10CI[1][2] = entropy(a10CI[1][0],a10CI[1][1])

    # calculate entropy all catagaries of A11
    a11CI[0][2] = entropy(a11CI[0][0],a11CI[0][1])
    a11CI[1][2] = entropy(a11CI[1][0],a11CI[1][1])

    # calculate entropy all catagaries of A12
    a12CI[0][2] = entropy(a12CI[0][0],a12CI[0][1])
    a12CI[1][2] = entropy(a12CI[1][0],a12CI[1][1])

    # calculate entropy all catagaries of A13
    a13CI[0][2] = entropy(a13CI[0][0],a13CI[0][1])
    a13CI[1][2] = entropy(a13CI[1][0],a13CI[1][1])
    a13CI[2][2] = entropy(a13CI[2][0],a13CI[2][1])

    # calculate entropy all catagaries of A14
    # a14CI[0][2] = entropy(a14CI[0][0],a14CI[0][1])
    # a14CI[1][2] = entropy(a14CI[1][0],a14CI[1][1])
    # a14CI[2][2] = entropy(a14CI[2][0],a14CI[2][1])
    # a14CI[3][2] = entropy(a14CI[3][0],a14CI[3][1])
    # a14CI[4][2] = entropy(a14CI[4][0],a14CI[4][1])
    # a14CI[5][2] = entropy(a14CI[5][0],a14CI[5][1])
    # a14CI[6][2] = entropy(a14CI[6][0],a14CI[6][1])
    # a14CI[7][2] = entropy(a14CI[7][0],a14CI[7][1])
    # a14CI[8][2] = entropy(a14CI[8][0],a14CI[8][1])
    # a14CI[9][2] = entropy(a14CI[9][0],a14CI[9][1])
    # a14CI[10][2] = entropy(a14CI[10][0],a14CI[10][1])
    # a14CI[11][2] = entropy(a14CI[11][0],a14CI[11][1])

    # calculate entropy all catagaries of A15
    a15CI[0][2] = entropy(a15CI[0][0],a15CI[0][1])
    a15CI[1][2] = entropy(a15CI[1][0],a15CI[1][1])
    a15CI[2][2] = entropy(a15CI[2][0],a15CI[2][1])



    # calculate Info 
    Info_A1 = inforD(a1,[a1CI[0][2],a1CI[1][2]])
    Info_A2 = inforD(a2,[a2CI[0][2],a2CI[1][2],a2CI[2][2],a2CI[3][2]]) 
    Info_A3 = inforD(a3,[a3CI[0][2],a3CI[1][2],a3CI[2][2],a3CI[3][2]]) 
    Info_A4 = inforD(a4,[a4CI[0][2],a4CI[1][2],a4CI[2][2],a4CI[3][2]])
    Info_A5 = inforD(a5,[a5CI[0][2],a5CI[1][2],a5CI[2][2]])
    Info_A6 = inforD(a6,[a6CI[0][2],a6CI[1][2],a6CI[2][2],a6CI[3][2],a6CI[4][2],a6CI[5][2],a6CI[6][2],a6CI[7][2],a6CI[8][2],a6CI[9][2],a6CI[10][2],a6CI[11][2],a6CI[12][2],a6CI[13][2]])
    Info_A7 = inforD(a7,[a7CI[0][2],a7CI[1][2],a7CI[2][2],a7CI[3][2],a7CI[4][2],a7CI[5][2],a7CI[6][2],a7CI[7][2],a7CI[8][2]])
    Info_A8 = inforD(a8,[a8CI[0][2],a8CI[1][2],a8CI[2][2],a8CI[3][2]]) 
    # Info_A9 = inforD(a9,[a9CI[0][2],a9CI[1][2]])
    Info_A10 = inforD(a10,[a10CI[0][2],a10CI[1][2]])
    Info_A11 = inforD(a11,[a11CI[0][2],a11CI[1][2]]) 
    Info_A12 = inforD(a12,[a12CI[0][2],a12CI[1][2]])
    Info_A13 = inforD(a13,[a13CI[0][2],a13CI[1][2],a13CI[2][2]])
    # Info_A14 = inforD(a14,[a14CI[0][2],a14CI[1][2],a14CI[2][2],a14CI[3][2],a14CI[4][2],a14CI[5][2],a14CI[6][2],a14CI[7][2],a14CI[8][2],a14CI[9][2],a14CI[10][2],a14CI[11][2]])
    Info_A15 = inforD(a15,[a15CI[0][2],a15CI[1][2],a15CI[2][2]]) 

    # แสดงผลการทำงานรอบแรก
    print("A1 count is", a1)
    print("A2 count is",a2)
    print("A3 count is",a3)
    print("A4 count is",a4)
    print("A5 count is", a5)
    print("A6 count is",a6)
    print("A7 count is", a7)
    print("A8 count is", a8)
    # print("A9 count is", a9)
    print("A10 count is", a10)
    print("A11 count is", a11)
    print("A12 count is", a12)
    print("A13 count is", a13)
    # print("A14 count is", a14)
    print("A15 count is", a15)
    print("A16 count is", a16)
    """

    """
    print("\n***Gain results of Lv.3 Left 4 dataset***")
    print("InD is %5.3f"% InD)
    gainA1=InD-Info_A1
    print("Gain (A1) is %5.3f"% gainA1)
    gainA2=InD-Info_A2
    print("Gain (A2) is %5.3f"% gainA2)
    gainA3=InD-Info_A3
    print("Gain (A3) is %5.3f"% gainA3)
    gainA4=InD-Info_A4
    print("Gain (A4) is %5.3f"% gainA4)
    gainA5=InD-Info_A5
    print("Gain (A5) is %5.3f"% gainA5)
    gainA6=InD-Info_A6
    print("Gain (A6) is %5.3f"% gainA6)
    gainA7=InD-Info_A7
    print("Gain (A7) is %5.3f"% gainA7)
    gainA8=InD-Info_A8
    print("Gain (A8) is %5.3f"% gainA8)
    # gainA9=InD-Info_A9
    # print("Gain (A9) is %5.3f"% gainA9)
    gainA10=InD-Info_A10
    print("Gain (A10) is %5.3f"% gainA10)
    gainA11=InD-Info_A11
    print("Gain (A11) is %5.3f"% gainA11)
    gainA12=InD-Info_A12
    print("Gain (A12) is %5.3f"% gainA12)
    gainA13=InD-Info_A13
    print("Gain (A13) is %5.3f"% gainA13)
    # gainA14=InD-Info_A14
    # print("Gain (A14) is %5.3f"% gainA14)
    gainA15=InD-Info_A15
    print("Gain (A15) is %5.3f"% gainA15)

    Result_All=[gainA1,gainA2,gainA3,gainA4,gainA5,gainA6,gainA7,gainA8,gainA10,gainA11,gainA12,gainA13,gainA15]
    max_gain=max(Result_All)    #find max gain
    pos=np.argmax(Result_All)   #position of max gain
    print("max gain of attb is %5.3f" % max_gain,"attribute is",pos)
    
    X4L21=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age <=30
    X4L22=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L23=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L24=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L25=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L26=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L27=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L28=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L29=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L210=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L211=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L212=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L213=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L214=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40


    for i in range(len(dataset)):
        if (dataset.iloc[i][5] == 'c'): 
            X4L21.append(dataset.iloc[i])
            
        elif(dataset.iloc[i][5] == 'd'): 
            X4L22.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'cc'): 
            X4L23.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'i'): 
            X4L24.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'j'): 
            X4L25.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'k'): 
            X4L26.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'm'): 
            X4L27.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'r'): 
            X4L28.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'q'): 
            X4L29.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'w'): 
            X4L210.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'x'): 
            X4L211.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'e'): 
            X4L212.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'aa'): 
            X4L213.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'ff'): 
            X4L214.append(dataset.iloc[i])
  
    

    crx4L21 = pd.DataFrame(X4L21)
    crx4L22 = pd.DataFrame(X4L22)
    crx4L23 = pd.DataFrame(X4L23)
    crx4L24 = pd.DataFrame(X4L24)
    crx4L25 = pd.DataFrame(X4L25)
    crx4L26 = pd.DataFrame(X4L26)
    crx4L27 = pd.DataFrame(X4L27)
    crx4L28 = pd.DataFrame(X4L28)
    crx4L29 = pd.DataFrame(X4L29)
    crx4L210 = pd.DataFrame(X4L210)
    crx4L211 = pd.DataFrame(X4L211)
    crx4L212 = pd.DataFrame(X4L212)
    crx4L213 = pd.DataFrame(X4L213)
    crx4L214 = pd.DataFrame(X4L214)


    crx4L21.to_csv('data/lv4/crx4L41.csv', index=False, header=False)
    crx4L22.to_csv('data/lv4/crx4L42.csv', index=False, header=False)
    crx4L23.to_csv('data/lv4/crx4L43.csv', index=False, header=False)
    crx4L24.to_csv('data/lv4/crx4L44.csv', index=False, header=False)
    crx4L25.to_csv('data/lv4/crx4L45.csv', index=False, header=False)
    crx4L26.to_csv('data/lv4/crx4L46.csv', index=False, header=False)
    crx4L27.to_csv('data/lv4/crx4L47.csv', index=False, header=False)
    crx4L28.to_csv('data/lv4/crx4L48.csv', index=False, header=False)
    crx4L29.to_csv('data/lv4/crx4L49.csv', index=False, header=False)
    crx4L210.to_csv('data/lv4/crx4L410.csv', index=False, header=False)
    crx4L211.to_csv('data/lv4/crx4L411.csv', index=False, header=False)
    crx4L212.to_csv('data/lv4/crx4L412.csv', index=False, header=False)
    crx4L213.to_csv('data/lv4/crx4L413.csv', index=False, header=False)
    crx4L214.to_csv('data/lv4/crx4L414.csv', index=False, header=False)



def findmaxgainLv3L5(dataset):  
    M=3 #row

    a1=np.zeros(2)
    a1CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of A1)

    a2=np.zeros(4) 
    a2CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A2)

    a3=np.zeros(4) #wait for generate range
    a3CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of age)

    a4=np.zeros(4)
    a4CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of age)

    a5=np.zeros(3)
    a5CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of age)

    a6=np.zeros(14)
    a6CI=[[0 for i in range(M)] for j in range(14)] # zero matrix 14 rows 3 columns (class and info gain of age)

    a7=np.zeros(9)
    a7CI=[[0 for i in range(M)] for j in range(9)] # zero matrix 9 rows 3 columns (class and info gain of age)

    a8=np.zeros(4)          # zero array for count sample in A8 
    a8CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A8)

    a10=np.zeros(2)
    a10CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of age)

    a11=np.zeros(2) #wait to generate range
    a11CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of age)

    a12=np.zeros(2)
    a12CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of age)

    a13=np.zeros(3)
    a13CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of age)


    a15=np.zeros(3) #wait to generate change
    a15CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of age)

    a16=np.zeros(2) 

    #วน loop เพื่อนับข้อมูล แยกตามรายละเอียด attb และ class
    for i in range(0,len(dataset)):
        #A1
        if (dataset.iloc[i][0] == 'b'):  #A1 = 'b'   
            a1[0]+=1 # total sample A1 = 'b'
            if (dataset.iloc[i][0] == 'b') and (dataset.iloc[i][15] == '+'):
                a1CI[0][0]+=1 #class +
            else:
                a1CI[0][1]+=1 #class -
        elif(dataset.iloc[i][0] == 'a'):    #A1 = 'a'
            a1[1]+=1 # total sample A1 = 'a'
            if (dataset.iloc[i][0] == 'a') and (dataset.iloc[i][15] == '+'):
                a1CI[1][0]+=1 #class +
            else:
                a1CI[1][1]+=1 #class -

        #A2
        if (float(dataset.iloc[i][1]) <= 25):   
            a2[0]+=1 # total sample A2 <=25
            if (float(dataset.iloc[i][1]) <= 25) and (dataset.iloc[i][15] == '+'):
                a2CI[0][0]+=1 #A2 <= 25 and class +
            else:
                a2CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][1]) >25 and float(dataset.iloc[i][1])<=30): 
            a2[1]+=1 # total sample 25 < A2 <= 30 
            if (float(dataset.iloc[i][1]) >25 and float(dataset.iloc[i][1])<=30) and (dataset.iloc[i][15] == '+'):
                a2CI[1][0]+=1 #25 < A2 <= 30  and class +
            else:
                a2CI[1][1]+=1 #25 < A2 <= 30 and class -
        elif(float(dataset.iloc[i][1]) > 30 and float(dataset.iloc[i][1])<=40): 
            a2[2]+=1 # total sample 30 < A2 <= 40
            if (float(dataset.iloc[i][1]) > 30 and float(dataset.iloc[i][1])<=40) and (dataset.iloc[i][15] == '+'):
                a2CI[2][0]+=1 #30 < A2 <= 40 and class +
            else:
                a2CI[2][1]+=1 #class -
        elif(float(dataset.iloc[i][1]) > 40): 
            a2[3]+=1 # total sample A2>40
            if (float(dataset.iloc[i][1]) > 40) and (dataset.iloc[i][15] == '+'):
                a2CI[3][0]+=1 #A2>40 and class +
            else:
                a2CI[3][1]+=1 #class -

        #A3
        if (float(dataset.iloc[i][2]) <=1): 
            a3[0]+=1 # total sample A3<=1
            if (float(dataset.iloc[i][2]) <=1) and (dataset.iloc[i][15] == '+'):
                a3CI[0][0]+=1 #class +
            else:
                a3CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][2]) >1 and float(dataset.iloc[i][2])<=3): 
            a3[1]+=1 # total sample >1 A3<=3
            if (float(dataset.iloc[i][2]) >1 and float(dataset.iloc[i][2])<=3) and (dataset.iloc[i][15] == '+'):
                a3CI[1][0]+=1 #class +
            else:
                a3CI[1][1]+=1 #class -
        elif(float(dataset.iloc[i][2]) > 3 and float(dataset.iloc[i][2])<=8): 
            a3[2]+=1 # total sample 3 > A3 <=8
            if (float(dataset.iloc[i][2]) > 3 and float(dataset.iloc[i][2])<=8) and (dataset.iloc[i][15] == '+'):
                a3CI[2][0]+=1 #class +
            else:
                a3CI[2][1]+=1 #class -
        elif(float(dataset.iloc[i][2]) > 8): 
            a3[3]+=1 # total sample A3>8
            if (float(dataset.iloc[i][2]) > 8) and (dataset.iloc[i][15] == '+'):
                a3CI[3][0]+=1 #class +
            else:
                a3CI[3][1]+=1 #class -
        
            
        #A4
        if (dataset.iloc[i][3] == 'u'): 
            a4[0]+=1 # total sample A4 = u
            if (dataset.iloc[i][3] == 'u') and (dataset.iloc[i][15] == '+'):
                a4CI[0][0]+=1 #count A4 = u and class +
            else:
                a4CI[0][1]+=1 #class -
        elif(dataset.iloc[i][3] == 'y'): 
            a4[1]+=1 # total sample A4 = y
            if (dataset.iloc[i][3] == 'y') and (dataset.iloc[i][15] == '+'):
                a4CI[1][0]+=1 #count A4 = y and class +
            else:
                a4CI[1][1]+=1 #class -
        elif(dataset.iloc[i][3] == 'l'): 
            a4[2]+=1 # total sample A4 = l
            if (dataset.iloc[i][3] == 'l') and (dataset.iloc[i][15] == '+'):
                a4CI[2][0]+=1 #count A4 = l and class +
            else:
                a4CI[2][1]+=1 #class -
        elif(dataset.iloc[i][3] == 't'): 
            a4[3]+=1 # total sample A4 = t
            if (dataset.iloc[i][3] == 't') and (dataset.iloc[i][15] == '+'):
                a4CI[3][0]+=1 #count A4 = t and class +
            else:
                a4CI[3][1]+=1 #class -

        #A5
        if (dataset.iloc[i][4] == 'g'): 
            a5[0]+=1 # total sample A5 = g
            if (dataset.iloc[i][4] == 'g') and (dataset.iloc[i][15] == '+'):
                a5CI[0][0]+=1 #class +
            else:
                a5CI[0][1]+=1 #class -
        elif(dataset.iloc[i][4] == 'p'): 
            a5[1]+=1 # total sample A5 = p
            if (dataset.iloc[i][4] == 'p') and (dataset.iloc[i][15] == '+'):
                a5CI[1][0]+=1 #class +
            else:
                a5CI[1][1]+=1 #class -
        elif(dataset.iloc[i][4] == 'gg'): 
            a5[2]+=1 # total sample A5 = gg
            if (dataset.iloc[i][4] == 'gg') and (dataset.iloc[i][15] == '+'):
                a5CI[2][0]+=1 #class +
            else:
                a5CI[2][1]+=1 #class -

        #A6
        if (dataset.iloc[i][5] == 'c'): 
            a6[0]+=1 # total sample A6 = c
            if (dataset.iloc[i][5] == 'c') and (dataset.iloc[i][15] == '+'):
                a6CI[0][0]+=1 #class +
            else:
                a6CI[0][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'd'): 
            a6[1]+=1 # total sample A6 = d
            if (dataset.iloc[i][5] == 'd') and (dataset.iloc[i][15] == '+'):
                a6CI[1][0]+=1 #class +
            else:
                a6CI[1][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'cc'): 
            a6[2]+=1 # total sample A6 = cc
            if (dataset.iloc[i][5] == 'cc') and (dataset.iloc[i][15] == '+'):
                a6CI[2][0]+=1 #class +
            else:
                a6CI[2][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'i'): 
            a6[3]+=1 # total sample A6 = i
            if (dataset.iloc[i][5] == 'i') and (dataset.iloc[i][15] == '+'):
                a6CI[3][0]+=1 #class +
            else:
                a6CI[3][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'j'): 
            a6[4]+=1 # total sample A6 = j
            if (dataset.iloc[i][5] == 'j') and (dataset.iloc[i][15] == '+'):
                a6CI[4][0]+=1 #class +
            else:
                a6CI[4][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'k'): 
            a6[5]+=1 # total sample A6 = k
            if (dataset.iloc[i][5] == 'k') and (dataset.iloc[i][15] == '+'):
                a6CI[5][0]+=1 #class +
            else:
                a6CI[5][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'm'): 
            a6[6]+=1 # total sample A6 = m
            if (dataset.iloc[i][5] == 'm') and (dataset.iloc[i][15] == '+'):
                a6CI[6][0]+=1 #class +
            else:
                a6CI[6][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'r'): 
            a6[7]+=1 # total sample A6 = r
            if (dataset.iloc[i][5] == 'r') and (dataset.iloc[i][15] == '+'):
                a6CI[7][0]+=1 #class +
            else:
                a6CI[7][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'q'): 
            a6[8]+=1 # total sample A6 = q
            if (dataset.iloc[i][5] == 'q') and (dataset.iloc[i][15] == '+'):
                a6CI[8][0]+=1 #class +
            else:
                a6CI[8][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'w'): 
            a6[9]+=1 # total sample A6 = w
            if (dataset.iloc[i][5] == 'w') and (dataset.iloc[i][15] == '+'):
                a6CI[9][0]+=1 #class +
            else:
                a6CI[9][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'x'): 
            a6[10]+=1 # total sample A6 = x
            if (dataset.iloc[i][5] == 'x') and (dataset.iloc[i][15] == '+'):
                a6CI[10][0]+=1 #class +
            else:
                a6CI[10][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'e'): 
            a6[11]+=1 # total sample A6 = e
            if (dataset.iloc[i][5] == 'e') and (dataset.iloc[i][15] == '+'):
                a6CI[11][0]+=1 #class +
            else:
                a6CI[11][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'aa'): 
            a6[12]+=1 # total sample A6 = aa
            if (dataset.iloc[i][5] == 'aa') and (dataset.iloc[i][15] == '+'):
                a6CI[12][0]+=1 #class +
            else:
                a6CI[12][1]+=1 #class -
        elif(dataset.iloc[i][5] == 'ff'): 
            a6[13]+=1 # total sample A6 = ff
            if (dataset.iloc[i][5] == 'ff') and (dataset.iloc[i][15] == '+'):
                a6CI[13][0]+=1 #class +
            else:
                a6CI[13][1]+=1 #class -

        #A7
        if (dataset.iloc[i][6] == 'v'): 
            a7[0]+=1 # total sample A6 = v
            if (dataset.iloc[i][6] == 'v') and (dataset.iloc[i][15] == '+'):
                a7CI[0][0]+=1 #class +
            else:
                a7CI[0][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'h'): 
            a7[1]+=1 # total sample A6 = h
            if (dataset.iloc[i][6] == 'h') and (dataset.iloc[i][15] == '+'):
                a7CI[1][0]+=1 #class +
            else:
                a7CI[1][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'bb'): 
            a7[2]+=1 # total sample A6 = bb
            if (dataset.iloc[i][6] == 'bb') and (dataset.iloc[i][15] == '+'):
                a7CI[2][0]+=1 #class +
            else:
                a7CI[2][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'j'): 
            a7[3]+=1 # total sample A6 = j
            if (dataset.iloc[i][6] == 'j') and (dataset.iloc[i][15] == '+'):
                a7CI[3][0]+=1 #class +
            else:
                a7CI[3][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'n'): 
            a7[4]+=1 # total sample A6 = n
            if (dataset.iloc[i][6] == 'n') and (dataset.iloc[i][15] == '+'):
                a7CI[4][0]+=1 #class +
            else:
                a7CI[4][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'z'): 
            a7[5]+=1 # total sample A6 = z
            if (dataset.iloc[i][6] == 'z') and (dataset.iloc[i][15] == '+'):
                a7CI[5][0]+=1 #class +
            else:
                a7CI[5][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'dd'): 
            a7[6]+=1 # total sample A6 = dd
            if (dataset.iloc[i][6] == 'dd') and (dataset.iloc[i][15] == '+'):
                a7CI[6][0]+=1 #class +
            else:
                a7CI[6][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'ff'): 
            a7[7]+=1 # total sample A6 = ff
            if (dataset.iloc[i][6] == 'ff') and (dataset.iloc[i][15] == '+'):
                a7CI[7][0]+=1 #class +
            else:
                a7CI[7][1]+=1 #class -
        elif (dataset.iloc[i][6] == 'o'): 
            a7[8]+=1 # total sample A6 = o
            if (dataset.iloc[i][6] == 'o') and (dataset.iloc[i][15] == '+'):
                a7CI[8][0]+=1 #class +
            else:
                a7CI[8][1]+=1 #class -
        
        #A8
        if (float(dataset.iloc[i][7]) <= 0.2): 
            a8[0]+=1 # total sample A8<=0.2
            if (float(dataset.iloc[i][7]) <= 0.2) and (dataset.iloc[i][15] == '+'):
                a8CI[0][0]+=1 #class +
            else:
                a8CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][7]) >0.2 and float(dataset.iloc[i][7])<=1): 
            a8[1]+=1 # total sample 0.2 < A8 <= 1
            if (float(dataset.iloc[i][7]) >0.2 and float(dataset.iloc[i][7])<=1) and (dataset.iloc[i][15] == '+'):
                a8CI[1][0]+=1 #class +
            else:
                a8CI[1][1]+=1 #class -
        elif(float(dataset.iloc[i][7]) >1 and float(dataset.iloc[i][7])<=3): 
            a8[2]+=1 # total sample 1 < A8 <= 3
            if (float(dataset.iloc[i][7]) >1 and float(dataset.iloc[i][7])<=3) and (dataset.iloc[i][15] == '+'):
                a8CI[2][0]+=1 #class +
            else:
                a8CI[2][1]+=1 #class -
        elif(float(dataset.iloc[i][7]) > 3): 
            a8[3]+=1 # total sample  A8 >3
            if (float(dataset.iloc[i][7]) > 3) and (dataset.iloc[i][15] == '+'):
                a8CI[3][0]+=1 #class +
            else:
                a8CI[3][1]+=1 #class -

        #A9
        #upper level

        #A10
        if (dataset.iloc[i][9] == 't'): 
            a10[0]+=1 # total sample A10 = t
            if (dataset.iloc[i][9] == 't') and (dataset.iloc[i][15] == '+'):
                a10CI[0][0]+=1 #class +
            else:
                a10CI[0][1]+=1 #class -
        elif (dataset.iloc[i][9] == 'f'): 
            a10[1]+=1 # total sample A10 = f
            if (dataset.iloc[i][9] == 'f') and (dataset.iloc[i][15] == '+'):
                a10CI[1][0]+=1 #class +
            else:
                a10CI[1][1]+=1 #class -

        #A11
        if (float(dataset.iloc[i][10]) <= 3): 
            a11[0]+=1 # total sample A11<=3
            if (float(dataset.iloc[i][10]) <= 3) and (dataset.iloc[i][15] == '+'):
                a11CI[0][0]+=1 #class +
            else:
                a11CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][10]) >3): 
            a11[1]+=1 # total sample A11>3
            if (float(dataset.iloc[i][10]) >3) and (dataset.iloc[i][15] == '+'):
                a11CI[1][0]+=1 #class +
            else:
                a11CI[1][1]+=1 #class -
        

        #A12
        if (dataset.iloc[i][11] == 't'): 
            a12[0]+=1 # total sample A12 = t
            if (dataset.iloc[i][11] == 't') and (dataset.iloc[i][15] == '+'):
                a12CI[0][0]+=1 #class +
            else:
                a12CI[0][1]+=1 #class -
        elif (dataset.iloc[i][11] == 'f'): 
            a12[1]+=1 # total sample A12 = t
            if (dataset.iloc[i][11] == 'f') and (dataset.iloc[i][15] == '+'):
                a12CI[1][0]+=1 #class +
            else:
                a12CI[1][1]+=1 #class -

        #A13
        if (dataset.iloc[i][12] == 'g'): 
            a13[0]+=1 # total sample A13 = g
            if (dataset.iloc[i][12] == 'g') and (dataset.iloc[i][15] == '+'):
                a13CI[0][0]+=1 #class +
            else:
                a13CI[0][1]+=1 #class -
        elif (dataset.iloc[i][12] == 'p'): 
            a13[1]+=1 # total sample A13 = p
            if (dataset.iloc[i][12] == 'p') and (dataset.iloc[i][15] == '+'):
                a13CI[1][0]+=1 #class +
            else:
                a13CI[1][1]+=1 #class -
        elif (dataset.iloc[i][12] == 's'): 
            a13[2]+=1 # total sample A13 = s
            if (dataset.iloc[i][12] == 's') and (dataset.iloc[i][15] == '+'):
                a13CI[2][0]+=1 #class +
            else:
                a13CI[2][1]+=1 #class -

        #A14
        #This level

        #A15
        if (float(dataset.iloc[i][14]) <= 5): 
            a15[0]+=1 # total sample A15<=5
            if (float(dataset.iloc[i][14]) <= 5) and (dataset.iloc[i][15] == '+'):
                a15CI[0][0]+=1 #class +
            else:
                a15CI[0][1]+=1 #class -
        elif(float(dataset.iloc[i][14]) > 5 and float(dataset.iloc[i][14]) <=395): 
            a15[1]+=1 # total sample 5<A15<=395
            if (float(dataset.iloc[i][14]) > 5 and float(dataset.iloc[i][14]) <=395) and (dataset.iloc[i][15] == '+'):
                a15CI[1][0]+=1 #class +
            else:
                a15CI[1][1]+=1 #class -
        elif (float(dataset.iloc[i][14]) > 395): 
            a15[2]+=1 # total sample A15 > 395
            if (float(dataset.iloc[i][14]) >395) and (dataset.iloc[i][15] == '+'):
                a15CI[2][0]+=1 #class +
            else:
                a15CI[2][1]+=1 #class -
        

        #A16
        if (dataset.iloc[i][15] == '+'): 
            a16[0]+=1 # total sample A16 = +
        elif (dataset.iloc[i][15] == '-'): 
            a16[1]+=1 # total sample A16 = -



    # calculate information gain of dataset and attb
    # base on class
    # calculate Info(D)
    InD=entropy(a16[1],a16[0])

    # calculate each attribute's Info
    # calculate entropy all catagaries of A1
    a1CI[0][2] = entropy(a1CI[0][0],a1CI[0][1])
    a1CI[1][2] = entropy(a1CI[1][0],a1CI[1][1])

    # calculate entropy all catagaries of A2
    a2CI[0][2] = entropy(a2CI[0][0],a2CI[0][1])
    a2CI[1][2] = entropy(a2CI[1][0],a2CI[1][1])
    a2CI[2][2] = entropy(a2CI[2][0],a2CI[2][1])
    a2CI[3][2] = entropy(a2CI[3][0],a2CI[3][1])

    # calculate entropy all catagaries of A3
    a3CI[0][2] = entropy(a3CI[0][0],a3CI[0][1])
    a3CI[1][2] = entropy(a3CI[1][0],a3CI[1][1])
    a3CI[2][2] = entropy(a3CI[2][0],a3CI[2][1])
    a3CI[3][2] = entropy(a3CI[3][0],a3CI[3][1])

    # calculate entropy all catagaries of A4
    a4CI[0][2] = entropy(a4CI[0][0],a4CI[0][1])
    a4CI[1][2] = entropy(a4CI[1][0],a4CI[1][1])
    a4CI[2][2] = entropy(a4CI[2][0],a4CI[2][1])
    a4CI[3][2] = entropy(a4CI[3][0],a4CI[3][1])

    # calculate entropy all catagaries of A5
    a5CI[0][2] = entropy(a5CI[0][0],a5CI[0][1])
    a5CI[1][2] = entropy(a5CI[1][0],a5CI[1][1])
    a5CI[2][2] = entropy(a5CI[2][0],a5CI[2][1])

    # calculate entropy all catagaries of A6
    a6CI[0][2] = entropy(a6CI[0][0],a6CI[0][1])
    a6CI[1][2] = entropy(a6CI[1][0],a6CI[1][1])
    a6CI[2][2] = entropy(a6CI[2][0],a6CI[2][1])
    a6CI[3][2] = entropy(a6CI[3][0],a6CI[3][1])
    a6CI[4][2] = entropy(a6CI[4][0],a6CI[4][1])
    a6CI[5][2] = entropy(a6CI[5][0],a6CI[5][1])
    a6CI[6][2] = entropy(a6CI[6][0],a6CI[6][1])
    a6CI[7][2] = entropy(a6CI[7][0],a6CI[7][1])
    a6CI[8][2] = entropy(a6CI[8][0],a6CI[8][1])
    a6CI[9][2] = entropy(a6CI[9][0],a6CI[9][1])
    a6CI[10][2] = entropy(a6CI[10][0],a6CI[10][1])
    a6CI[11][2] = entropy(a6CI[11][0],a6CI[11][1])
    a6CI[12][2] = entropy(a6CI[12][0],a6CI[12][1])
    a6CI[13][2] = entropy(a6CI[13][0],a6CI[13][1])

    # calculate entropy all catagaries of A7
    a7CI[0][2] = entropy(a7CI[0][0],a7CI[0][1])
    a7CI[1][2] = entropy(a7CI[1][0],a7CI[1][1])
    a7CI[2][2] = entropy(a7CI[2][0],a7CI[2][1])
    a7CI[3][2] = entropy(a7CI[3][0],a7CI[3][1])
    a7CI[4][2] = entropy(a7CI[4][0],a7CI[4][1])
    a7CI[5][2] = entropy(a7CI[5][0],a7CI[5][1])
    a7CI[6][2] = entropy(a7CI[6][0],a7CI[6][1])
    a7CI[7][2] = entropy(a7CI[7][0],a7CI[7][1])
    a7CI[8][2] = entropy(a7CI[8][0],a7CI[8][1])

    # calculate entropy all catagaries of A8
    a8CI[0][2] = entropy(a8CI[0][0],a8CI[0][1])
    a8CI[1][2] = entropy(a8CI[1][0],a8CI[1][1])
    a8CI[2][2] = entropy(a8CI[2][0],a8CI[2][1])
    a8CI[3][2] = entropy(a8CI[3][0],a8CI[3][1])

    # calculate entropy all catagaries of A9
    # a9CI[0][2] = entropy(a9CI[0][0],a9CI[0][1])
    # a9CI[1][2] = entropy(a9CI[1][0],a9CI[1][1])

    # calculate entropy all catagaries of A10
    a10CI[0][2] = entropy(a10CI[0][0],a10CI[0][1])
    a10CI[1][2] = entropy(a10CI[1][0],a10CI[1][1])

    # calculate entropy all catagaries of A11
    a11CI[0][2] = entropy(a11CI[0][0],a11CI[0][1])
    a11CI[1][2] = entropy(a11CI[1][0],a11CI[1][1])

    # calculate entropy all catagaries of A12
    a12CI[0][2] = entropy(a12CI[0][0],a12CI[0][1])
    a12CI[1][2] = entropy(a12CI[1][0],a12CI[1][1])

    # calculate entropy all catagaries of A13
    a13CI[0][2] = entropy(a13CI[0][0],a13CI[0][1])
    a13CI[1][2] = entropy(a13CI[1][0],a13CI[1][1])
    a13CI[2][2] = entropy(a13CI[2][0],a13CI[2][1])

    # calculate entropy all catagaries of A14
    # a14CI[0][2] = entropy(a14CI[0][0],a14CI[0][1])
    # a14CI[1][2] = entropy(a14CI[1][0],a14CI[1][1])
    # a14CI[2][2] = entropy(a14CI[2][0],a14CI[2][1])
    # a14CI[3][2] = entropy(a14CI[3][0],a14CI[3][1])
    # a14CI[4][2] = entropy(a14CI[4][0],a14CI[4][1])
    # a14CI[5][2] = entropy(a14CI[5][0],a14CI[5][1])
    # a14CI[6][2] = entropy(a14CI[6][0],a14CI[6][1])
    # a14CI[7][2] = entropy(a14CI[7][0],a14CI[7][1])
    # a14CI[8][2] = entropy(a14CI[8][0],a14CI[8][1])
    # a14CI[9][2] = entropy(a14CI[9][0],a14CI[9][1])
    # a14CI[10][2] = entropy(a14CI[10][0],a14CI[10][1])
    # a14CI[11][2] = entropy(a14CI[11][0],a14CI[11][1])

    # calculate entropy all catagaries of A15
    a15CI[0][2] = entropy(a15CI[0][0],a15CI[0][1])
    a15CI[1][2] = entropy(a15CI[1][0],a15CI[1][1])
    a15CI[2][2] = entropy(a15CI[2][0],a15CI[2][1])



    # calculate Info 
    Info_A1 = inforD(a1,[a1CI[0][2],a1CI[1][2]])
    Info_A2 = inforD(a2,[a2CI[0][2],a2CI[1][2],a2CI[2][2],a2CI[3][2]]) 
    Info_A3 = inforD(a3,[a3CI[0][2],a3CI[1][2],a3CI[2][2],a3CI[3][2]]) 
    Info_A4 = inforD(a4,[a4CI[0][2],a4CI[1][2],a4CI[2][2],a4CI[3][2]])
    Info_A5 = inforD(a5,[a5CI[0][2],a5CI[1][2],a5CI[2][2]])
    Info_A6 = inforD(a6,[a6CI[0][2],a6CI[1][2],a6CI[2][2],a6CI[3][2],a6CI[4][2],a6CI[5][2],a6CI[6][2],a6CI[7][2],a6CI[8][2],a6CI[9][2],a6CI[10][2],a6CI[11][2],a6CI[12][2],a6CI[13][2]])
    Info_A7 = inforD(a7,[a7CI[0][2],a7CI[1][2],a7CI[2][2],a7CI[3][2],a7CI[4][2],a7CI[5][2],a7CI[6][2],a7CI[7][2],a7CI[8][2]])
    Info_A8 = inforD(a8,[a8CI[0][2],a8CI[1][2],a8CI[2][2],a8CI[3][2]]) 
    # Info_A9 = inforD(a9,[a9CI[0][2],a9CI[1][2]])
    Info_A10 = inforD(a10,[a10CI[0][2],a10CI[1][2]])
    Info_A11 = inforD(a11,[a11CI[0][2],a11CI[1][2]]) 
    Info_A12 = inforD(a12,[a12CI[0][2],a12CI[1][2]])
    Info_A13 = inforD(a13,[a13CI[0][2],a13CI[1][2],a13CI[2][2]])
    # Info_A14 = inforD(a14,[a14CI[0][2],a14CI[1][2],a14CI[2][2],a14CI[3][2],a14CI[4][2],a14CI[5][2],a14CI[6][2],a14CI[7][2],a14CI[8][2],a14CI[9][2],a14CI[10][2],a14CI[11][2]])
    Info_A15 = inforD(a15,[a15CI[0][2],a15CI[1][2],a15CI[2][2]]) 

    # แสดงผลการทำงานรอบแรก
    print("A1 count is", a1)
    print("A2 count is",a2)
    print("A3 count is",a3)
    print("A4 count is",a4)
    print("A5 count is", a5)
    print("A6 count is",a6)
    print("A7 count is", a7)
    print("A8 count is", a8)
    # print("A9 count is", a9)
    print("A10 count is", a10)
    print("A11 count is", a11)
    print("A12 count is", a12)
    print("A13 count is", a13)
    # print("A14 count is", a14)
    print("A15 count is", a15)
    print("A16 count is", a16)
    """

    """
    print("\n***Gain results of Lv.3 Left 5 dataset***")
    print("InD is %5.3f"% InD)
    gainA1=InD-Info_A1
    print("Gain (A1) is %5.3f"% gainA1)
    gainA2=InD-Info_A2
    print("Gain (A2) is %5.3f"% gainA2)
    gainA3=InD-Info_A3
    print("Gain (A3) is %5.3f"% gainA3)
    gainA4=InD-Info_A4
    print("Gain (A4) is %5.3f"% gainA4)
    gainA5=InD-Info_A5
    print("Gain (A5) is %5.3f"% gainA5)
    gainA6=InD-Info_A6
    print("Gain (A6) is %5.3f"% gainA6)
    gainA7=InD-Info_A7
    print("Gain (A7) is %5.3f"% gainA7)
    gainA8=InD-Info_A8
    print("Gain (A8) is %5.3f"% gainA8)
    # gainA9=InD-Info_A9
    # print("Gain (A9) is %5.3f"% gainA9)
    gainA10=InD-Info_A10
    print("Gain (A10) is %5.3f"% gainA10)
    gainA11=InD-Info_A11
    print("Gain (A11) is %5.3f"% gainA11)
    gainA12=InD-Info_A12
    print("Gain (A12) is %5.3f"% gainA12)
    gainA13=InD-Info_A13
    print("Gain (A13) is %5.3f"% gainA13)
    # gainA14=InD-Info_A14
    # print("Gain (A14) is %5.3f"% gainA14)
    gainA15=InD-Info_A15
    print("Gain (A15) is %5.3f"% gainA15)

    Result_All=[gainA1,gainA2,gainA3,gainA4,gainA5,gainA6,gainA7,gainA8,gainA10,gainA11,gainA12,gainA13,gainA15]
    max_gain=max(Result_All)    #find max gain
    pos=np.argmax(Result_All)   #position of max gain
    print("max gain of attb is %5.3f" % max_gain,"attribute is",pos)
    
    X4L21=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age <=30
    X4L22=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L23=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L24=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L25=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L26=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L27=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L28=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L29=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L210=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L211=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L212=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L213=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
    X4L214=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40


    for i in range(len(dataset)):
        if (dataset.iloc[i][5] == 'c'): 
            X4L21.append(dataset.iloc[i])
            
        elif(dataset.iloc[i][5] == 'd'): 
            X4L22.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'cc'): 
            X4L23.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'i'): 
            X4L24.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'j'): 
            X4L25.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'k'): 
            X4L26.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'm'): 
            X4L27.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'r'): 
            X4L28.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'q'): 
            X4L29.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'w'): 
            X4L210.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'x'): 
            X4L211.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'e'): 
            X4L212.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'aa'): 
            X4L213.append(dataset.iloc[i])
        elif(dataset.iloc[i][5] == 'ff'): 
            X4L214.append(dataset.iloc[i])
  
    

    crx4L21 = pd.DataFrame(X4L21)
    crx4L22 = pd.DataFrame(X4L22)
    crx4L23 = pd.DataFrame(X4L23)
    crx4L24 = pd.DataFrame(X4L24)
    crx4L25 = pd.DataFrame(X4L25)
    crx4L26 = pd.DataFrame(X4L26)
    crx4L27 = pd.DataFrame(X4L27)
    crx4L28 = pd.DataFrame(X4L28)
    crx4L29 = pd.DataFrame(X4L29)
    crx4L210 = pd.DataFrame(X4L210)
    crx4L211 = pd.DataFrame(X4L211)
    crx4L212 = pd.DataFrame(X4L212)
    crx4L213 = pd.DataFrame(X4L213)
    crx4L214 = pd.DataFrame(X4L214)


    crx4L21.to_csv('data/lv4/crx4L51.csv', index=False, header=False)
    crx4L22.to_csv('data/lv4/crx4L52.csv', index=False, header=False)
    crx4L23.to_csv('data/lv4/crx4L53.csv', index=False, header=False)
    crx4L24.to_csv('data/lv4/crx4L54.csv', index=False, header=False)
    crx4L25.to_csv('data/lv4/crx4L55.csv', index=False, header=False)
    crx4L26.to_csv('data/lv4/crx4L56.csv', index=False, header=False)
    crx4L27.to_csv('data/lv4/crx4L57.csv', index=False, header=False)
    crx4L28.to_csv('data/lv4/crx4L58.csv', index=False, header=False)
    crx4L29.to_csv('data/lv4/crx4L59.csv', index=False, header=False)
    crx4L210.to_csv('data/lv4/crx4L510.csv', index=False, header=False)
    crx4L211.to_csv('data/lv4/crx4L511.csv', index=False, header=False)
    crx4L212.to_csv('data/lv4/crx4L512.csv', index=False, header=False)
    crx4L213.to_csv('data/lv4/crx4L513.csv', index=False, header=False)
    crx4L214.to_csv('data/lv4/crx4L514.csv', index=False, header=False)