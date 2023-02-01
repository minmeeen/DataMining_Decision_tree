import numpy as np
from Dtreefunc import *
from Preprocessing import *
import pandas as pd

def findmaxgainLv2L(dataset):  
    M=3 #row

    a1=np.zeros(2)
    a1CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of A1)

    a2=np.zeros(4) 
    a2CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A2)

    a3=np.zeros(4) 
    a3CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A3)

    a4=np.zeros(4)
    a4CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A4)

    a5=np.zeros(3)
    a5CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of A5)

    a6=np.zeros(14)
    a6CI=[[0 for i in range(M)] for j in range(14)] # zero matrix 14 rows 3 columns (class and info gain of A6)

    a7=np.zeros(9)
    a7CI=[[0 for i in range(M)] for j in range(9)] # zero matrix 9 rows 3 columns (class and info gain of A7)

    a8=np.zeros(4) 
    a8CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A8)

    a10=np.zeros(2)
    a10CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of A10)

    a11=np.zeros(2) 
    a11CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of A11)

    a12=np.zeros(2)
    a12CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of A12)

    a13=np.zeros(3)
    a13CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of A13)

    a14=np.zeros(12) 
    a14CI=[[0 for i in range(M)] for j in range(12)] # zero matrix 11 rows 3 columns (class and info gain of A14)

    a15=np.zeros(3) 
    a15CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of A15)

    a16=np.zeros(2)


    for i in range(0,len(dataset)):
        #A1
        if (dataset.iloc[i][0] == 'b'):  #A1 = 'b'   
            a1[0]+=1 # total sample A1 = 'b'
            if (dataset.iloc[i][0] == 'b') and (dataset.iloc[i][15] == '+'):
                a1CI[0][0]+=1 #count A1 = 'b' and class +
            else:
                a1CI[0][1]+=1 #count A1 = 'b' and class -
        elif(dataset.iloc[i][0] == 'a'):    #A1 = 'a'
            a1[1]+=1 # total sample A1 = 'a'
            if (dataset.iloc[i][0] == 'a') and (dataset.iloc[i][15] == '+'):
                a1CI[1][0]+=1 #count A1 = 'a' and class +
            else:
                a1CI[1][1]+=1 #count A1 = 'a' and class -

        #A2
        if (float(dataset.iloc[i][1]) <= 25):   #A2 <=25
            a2[0]+=1 # total sample A2 <=25
            if (float(dataset.iloc[i][1]) <= 25) and (dataset.iloc[i][15] == '+'):
                a2CI[0][0]+=1 #count A2 <= 25 and class +
            else:
                a2CI[0][1]+=1 #count A2 <= 25 class -
        elif(float(dataset.iloc[i][1]) >25 and float(dataset.iloc[i][1])<=30): #25 < A2 <=30
            a2[1]+=1 # total sample 25 < A2 <= 30 
            if (float(dataset.iloc[i][1]) >25 and float(dataset.iloc[i][1])<=30) and (dataset.iloc[i][15] == '+'):
                a2CI[1][0]+=1 #count 25 < A2 <= 30  and class +
            else:
                a2CI[1][1]+=1 #count 25 < A2 <= 30 and class -
        elif(float(dataset.iloc[i][1]) > 30 and float(dataset.iloc[i][1])<=40): #30 < A2 <=40
            a2[2]+=1 # total sample 30 < A2 <= 40
            if (float(dataset.iloc[i][1]) > 30 and float(dataset.iloc[i][1])<=40) and (dataset.iloc[i][15] == '+'):
                a2CI[2][0]+=1 # count 30 < A2 <= 40 and class +
            else:
                a2CI[2][1]+=1 #count 30 < A2 <=40 and class -
        elif(float(dataset.iloc[i][1]) > 40):   #A2 > 40 
            a2[3]+=1 # total sample A2>40
            if (float(dataset.iloc[i][1]) > 40) and (dataset.iloc[i][15] == '+'):
                a2CI[3][0]+=1 #count A2>40 and class +
            else:
                a2CI[3][1]+=1 #count A2>40 and class -

        #A3
        if (float(dataset.iloc[i][2]) <=1): #A3 <= 1
            a3[0]+=1 # total sample A3<=1
            if (float(dataset.iloc[i][2]) <=1) and (dataset.iloc[i][15] == '+'):
                a3CI[0][0]+=1 #count A3 <= 1 and class +
            else:
                a3CI[0][1]+=1 #count A3 <= 1 and class -
        elif(float(dataset.iloc[i][2]) >1 and float(dataset.iloc[i][2])<=3): #1 < A3 <=3
            a3[1]+=1 # total sample 1< A3 <=3
            if (float(dataset.iloc[i][2]) >1 and float(dataset.iloc[i][2])<=3) and (dataset.iloc[i][15] == '+'):
                a3CI[1][0]+=1 #count 1 < A3 <=3 and class +
            else:
                a3CI[1][1]+=1 #count 1 < A3 <=3 and class -
        elif(float(dataset.iloc[i][2]) > 3 and float(dataset.iloc[i][2])<=8): #3 < A3 <=8
            a3[2]+=1 # total sample 3 < A3 <=8
            if (float(dataset.iloc[i][2]) > 3 and float(dataset.iloc[i][2])<=8) and (dataset.iloc[i][15] == '+'):
                a3CI[2][0]+=1 #count 3 < A3 <=8 and class +
            else:
                a3CI[2][1]+=1 #count 3 < A3 <=8 and class -
        elif(float(dataset.iloc[i][2]) > 8): #A3>8
            a3[3]+=1 # total sample A3>8
            if (float(dataset.iloc[i][2]) > 8) and (dataset.iloc[i][15] == '+'):
                a3CI[3][0]+=1 #count A3>8 and class +
            else:
                a3CI[3][1]+=1 #count A3>8 and class -
        
            
        #A4
        if (dataset.iloc[i][3] == 'u'):     #A4 = u
            a4[0]+=1 # total sample A4 = u
            if (dataset.iloc[i][3] == 'u') and (dataset.iloc[i][15] == '+'):
                a4CI[0][0]+=1 #count A4 = u and class +
            else:
                a4CI[0][1]+=1 #count A4 = u and class -
        elif(dataset.iloc[i][3] == 'y'):    #A4 = y
            a4[1]+=1 # total sample A4 = y
            if (dataset.iloc[i][3] == 'y') and (dataset.iloc[i][15] == '+'):
                a4CI[1][0]+=1 #count A4 = y and class +
            else:
                a4CI[1][1]+=1 #count A4 = y and class -
        elif(dataset.iloc[i][3] == 'l'):    #A4 = l
            a4[2]+=1 # total sample A4 = l
            if (dataset.iloc[i][3] == 'l') and (dataset.iloc[i][15] == '+'):
                a4CI[2][0]+=1 #count A4 = l and class +
            else:
                a4CI[2][1]+=1 #count A4 = l and class -
        elif(dataset.iloc[i][3] == 't'):    #A4 = t
            a4[3]+=1 # total sample A4 = t
            if (dataset.iloc[i][3] == 't') and (dataset.iloc[i][15] == '+'):
                a4CI[3][0]+=1 #count A4 = t and class +
            else:
                a4CI[3][1]+=1 #count A4 = t and class -

        #A5
        if (dataset.iloc[i][4] == 'g'):     #A5 = g
            a5[0]+=1 # total sample A5 = g
            if (dataset.iloc[i][4] == 'g') and (dataset.iloc[i][15] == '+'):
                a5CI[0][0]+=1 #count A5 = g and class +
            else:
                a5CI[0][1]+=1 #count A5 = g and class -
        elif(dataset.iloc[i][4] == 'p'):    #A5 = p
            a5[1]+=1 # total sample A5 = p
            if (dataset.iloc[i][4] == 'p') and (dataset.iloc[i][15] == '+'):
                a5CI[1][0]+=1 #count A5 = p and class +
            else:
                a5CI[1][1]+=1 #count A5 = p and class -
        elif(dataset.iloc[i][4] == 'gg'):   #A5 = gg
            a5[2]+=1 # total sample A5 = gg
            if (dataset.iloc[i][4] == 'gg') and (dataset.iloc[i][15] == '+'):
                a5CI[2][0]+=1 #count A5 = gg and class +
            else:
                a5CI[2][1]+=1 #A5 = gg and class -

        #A6
        if (dataset.iloc[i][5] == 'c'):     #A6 = c
            a6[0]+=1 # total sample A6 = c
            if (dataset.iloc[i][5] == 'c') and (dataset.iloc[i][15] == '+'):
                a6CI[0][0]+=1 #count A6 = c and class +
            else:
                a6CI[0][1]+=1 #count A6 = c and class -
        elif(dataset.iloc[i][5] == 'd'):    #A6 = d
            a6[1]+=1 # total sample A6 = d
            if (dataset.iloc[i][5] == 'd') and (dataset.iloc[i][15] == '+'):
                a6CI[1][0]+=1 #count A6 = d and class +
            else:
                a6CI[1][1]+=1 #count A6 = d and class -
        elif(dataset.iloc[i][5] == 'cc'):   #A6 = cc
            a6[2]+=1 # total sample A6 = cc
            if (dataset.iloc[i][5] == 'cc') and (dataset.iloc[i][15] == '+'):
                a6CI[2][0]+=1 #count A6 = cc and class +
            else:
                a6CI[2][1]+=1 #count A6 = cc and class -
        elif(dataset.iloc[i][5] == 'i'):    #A6 = i
            a6[3]+=1 # total sample A6 = i
            if (dataset.iloc[i][5] == 'i') and (dataset.iloc[i][15] == '+'):
                a6CI[3][0]+=1 #count A6 = i and class +
            else:
                a6CI[3][1]+=1 #count A6 = i and class -
        elif(dataset.iloc[i][5] == 'j'):    #A6 = j
            a6[4]+=1 # total sample A6 = j
            if (dataset.iloc[i][5] == 'j') and (dataset.iloc[i][15] == '+'):
                a6CI[4][0]+=1 #count A6 = j and class +
            else:
                a6CI[4][1]+=1 #count A6 = j and class -
        elif(dataset.iloc[i][5] == 'k'):    #A6 = k
            a6[5]+=1 # total sample A6 = k
            if (dataset.iloc[i][5] == 'k') and (dataset.iloc[i][15] == '+'):
                a6CI[5][0]+=1 #count A6 = k and class +
            else:
                a6CI[5][1]+=1 #count A6 = k and class -
        elif(dataset.iloc[i][5] == 'm'):    #A6 = m
            a6[6]+=1 # total sample A6 = m
            if (dataset.iloc[i][5] == 'm') and (dataset.iloc[i][15] == '+'):
                a6CI[6][0]+=1 #count A6 = m and class +
            else:
                a6CI[6][1]+=1 #count A6 = m and class -
        elif(dataset.iloc[i][5] == 'r'):    #A6 = r
            a6[7]+=1 # total sample A6 = r
            if (dataset.iloc[i][5] == 'r') and (dataset.iloc[i][15] == '+'):
                a6CI[7][0]+=1 #count A6 = r and class +
            else:
                a6CI[7][1]+=1 #count A6 = r and class -
        elif(dataset.iloc[i][5] == 'q'):    # A6 = q
            a6[8]+=1 # total sample A6 = q
            if (dataset.iloc[i][5] == 'q') and (dataset.iloc[i][15] == '+'):
                a6CI[8][0]+=1 #count A6 = q and class +
            else:
                a6CI[8][1]+=1 #count A6 = q and class -
        elif(dataset.iloc[i][5] == 'w'):    #A6 = w
            a6[9]+=1 # total sample A6 = w
            if (dataset.iloc[i][5] == 'w') and (dataset.iloc[i][15] == '+'):
                a6CI[9][0]+=1 #count A6 = w and class +
            else:
                a6CI[9][1]+=1 #count A6 = w and class -
        elif(dataset.iloc[i][5] == 'x'):    # A6 = x
            a6[10]+=1 # total sample A6 = x
            if (dataset.iloc[i][5] == 'x') and (dataset.iloc[i][15] == '+'):
                a6CI[10][0]+=1 #count A6 = x and class +
            else:
                a6CI[10][1]+=1 #count A6 = x and class -
        elif(dataset.iloc[i][5] == 'e'):    #A6 = e
            a6[11]+=1 # total sample A6 = e
            if (dataset.iloc[i][5] == 'e') and (dataset.iloc[i][15] == '+'):
                a6CI[11][0]+=1 #count A6 = e and class +
            else:
                a6CI[11][1]+=1 #count A6 = e and class -
        elif(dataset.iloc[i][5] == 'aa'):   #A6 = aa
            a6[12]+=1 # total sample A6 = aa
            if (dataset.iloc[i][5] == 'aa') and (dataset.iloc[i][15] == '+'):
                a6CI[12][0]+=1 #count A6 = aa and class +
            else:
                a6CI[12][1]+=1 #count A6 = aa and class -
        elif(dataset.iloc[i][5] == 'ff'):   #A6 = ff
            a6[13]+=1 # total sample A6 = ff
            if (dataset.iloc[i][5] == 'ff') and (dataset.iloc[i][15] == '+'):
                a6CI[13][0]+=1 #count A6 = ff and class +
            else:
                a6CI[13][1]+=1 #count A6 = ff and class -

        #A7
        if (dataset.iloc[i][6] == 'v'):     #A7 = v
            a7[0]+=1 # total sample A7 = v
            if (dataset.iloc[i][6] == 'v') and (dataset.iloc[i][15] == '+'):
                a7CI[0][0]+=1 #count A7 = v and class +
            else:
                a7CI[0][1]+=1 #count A7 = v and class -
        elif (dataset.iloc[i][6] == 'h'):   #A7 = h
            a7[1]+=1 # total sample A7 = h
            if (dataset.iloc[i][6] == 'h') and (dataset.iloc[i][15] == '+'):
                a7CI[1][0]+=1 #count A7 = h and class +
            else:
                a7CI[1][1]+=1 #count A7 = h and class -
        elif (dataset.iloc[i][6] == 'bb'):  #A7 = bb
            a7[2]+=1 # total sample A7 = bb
            if (dataset.iloc[i][6] == 'bb') and (dataset.iloc[i][15] == '+'):
                a7CI[2][0]+=1 #count A7 = bb and class +
            else:
                a7CI[2][1]+=1 #count A7 = bb and class -
        elif (dataset.iloc[i][6] == 'j'):   #A7 = j
            a7[3]+=1 # total sample A7 = j
            if (dataset.iloc[i][6] == 'j') and (dataset.iloc[i][15] == '+'):
                a7CI[3][0]+=1 #count A7 = j and class +
            else:
                a7CI[3][1]+=1 #count A7 = j and class -
        elif (dataset.iloc[i][6] == 'n'):   #A7 = n
            a7[4]+=1 # total sample A7 = n
            if (dataset.iloc[i][6] == 'n') and (dataset.iloc[i][15] == '+'):
                a7CI[4][0]+=1 #count A7 = n and class +
            else:
                a7CI[4][1]+=1 #count A7 = n and class -
        elif (dataset.iloc[i][6] == 'z'):   #A7 = z
            a7[5]+=1 # total sample A7 = z
            if (dataset.iloc[i][6] == 'z') and (dataset.iloc[i][15] == '+'):
                a7CI[5][0]+=1 #count A7 = z and class +
            else:
                a7CI[5][1]+=1 #count A7 = z and class -
        elif (dataset.iloc[i][6] == 'dd'):  #A7 = dd
            a7[6]+=1 # total sample A7 = dd
            if (dataset.iloc[i][6] == 'dd') and (dataset.iloc[i][15] == '+'):
                a7CI[6][0]+=1 #count A7 = dd and class +
            else:
                a7CI[6][1]+=1 #count A7 = dd and class -
        elif (dataset.iloc[i][6] == 'ff'):  #A7 = ff
            a7[7]+=1 # total sample A7 = ff
            if (dataset.iloc[i][6] == 'ff') and (dataset.iloc[i][15] == '+'):
                a7CI[7][0]+=1 #count A7 = ff and class +
            else:
                a7CI[7][1]+=1 #count A7 = ff and class -
        elif (dataset.iloc[i][6] == 'o'):   #A7 = o
            a7[8]+=1 # total sample A7 = o
            if (dataset.iloc[i][6] == 'o') and (dataset.iloc[i][15] == '+'):
                a7CI[8][0]+=1 #count A7 = o and class +
            else:
                a7CI[8][1]+=1 #count A7 = o and class -
        
        #A8
        if (float(dataset.iloc[i][7]) <= 0.2):  #A8<=0.2
            a8[0]+=1 # total sample A8<=0.2
            if (float(dataset.iloc[i][7]) <= 0.2) and (dataset.iloc[i][15] == '+'):
                a8CI[0][0]+=1 #count A8<=0.2 and class +
            else:
                a8CI[0][1]+=1 #count A8<=0.2 and class -
        elif(float(dataset.iloc[i][7]) >0.2 and float(dataset.iloc[i][7])<=1):  # 0.2 < A8 <= 1
            a8[1]+=1 # total sample 0.2 < A8 <= 1
            if (float(dataset.iloc[i][7]) >0.2 and float(dataset.iloc[i][7])<=1) and (dataset.iloc[i][15] == '+'):
                a8CI[1][0]+=1 #count  0.2 < A8 <= 1 and class +
            else:
                a8CI[1][1]+=1 #count  0.2 < A8 <= 1 and class -
        elif(float(dataset.iloc[i][7]) >1 and float(dataset.iloc[i][7])<=3):    #1 < A8 <= 3
            a8[2]+=1 # total sample 1 < A8 <= 3
            if (float(dataset.iloc[i][7]) >1 and float(dataset.iloc[i][7])<=3) and (dataset.iloc[i][15] == '+'):
                a8CI[2][0]+=1 #count 1 < A8 <= 3 and class +
            else:
                a8CI[2][1]+=1 #count 1 < A8 <= 3 and class -
        elif(float(dataset.iloc[i][7]) > 3):    # A8 >3
            a8[3]+=1 # total sample  A8 >3
            if (float(dataset.iloc[i][7]) > 3) and (dataset.iloc[i][15] == '+'):
                a8CI[3][0]+=1 #count  A8 >3 and class +
            else:
                a8CI[3][1]+=1 #count  A8 >3 and class -

        #A9
        #this level

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
        if (dataset.iloc[i][13][1] == '0'): 
            if (dataset.iloc[i][13][2] == '0'): 
                a14[0]+=1 # total sample A14 = X00XX
                if (dataset.iloc[i][13][2] == '0' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[0][0]+=1 #class +
                else:
                    a14CI[0][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '1'): 
                a14[1]+=1 # total sample A14 = X01XX
                if (dataset.iloc[i][13][2] == '1' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[1][0]+=1 #class +
                else:
                    a14CI[1][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '2'): 
                a14[2]+=1 # total sample A14 = X02XX
                if (dataset.iloc[i][13][2] == '2' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[2][0]+=1 #class +
                else:
                    a14CI[2][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '3'): 
                a14[3]+=1 # total sample A14 = X03XX
                if (dataset.iloc[i][13][2] == '3' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[3][0]+=1 #class +
                else:
                    a14CI[3][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '4'): 
                a14[4]+=1 # total sample A14 = X04XX
                if (dataset.iloc[i][13][2] == '4' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[4][0]+=1 #class +
                else:
                    a14CI[4][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '5'): 
                a14[5]+=1 # total sample A14 = X05XX
                if (dataset.iloc[i][13][2] == '5' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[5][0]+=1 #class +
                else:
                    a14CI[5][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '6'): 
                a14[6]+=1 # total sample A14 = X06XX
                if (dataset.iloc[i][13][2] == '6' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[6][0]+=1 #class +
                else:
                    a14CI[6][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '7'): 
                a14[7]+=1 # total sample A14 = X07XX
                if (dataset.iloc[i][13][2] == '7' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[7][0]+=1 #class +
                else:
                    a14CI[7][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '8'): 
                a14[8]+=1 # total sample A14 = X08XX
                if (dataset.iloc[i][13][2] == '8' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[8][0]+=1 #class +
                else:
                    a14CI[8][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '9'): 
                a14[9]+=1 # total sample A14 = X09XX
                if (dataset.iloc[i][13][2] == '9' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[9][0]+=1 #class +
                else:
                    a14CI[9][1]+=1 #class -
        elif (dataset.iloc[i][13][1] == '1' ): 
            a14[10]+=1 # total sample A14 = X1XXX
            if (dataset.iloc[i][13][1] == '1') and (dataset.iloc[i][15] == '+'):
                a14CI[10][0]+=1 #class +
            else:
                a14CI[10][1]+=1 #class -
        elif (dataset.iloc[i][13][1] == '2' ): 
            a14[11]+=1 # total sample A14 = X2XXX
            if (dataset.iloc[i][13][1] == '2') and (dataset.iloc[i][15] == '+'):
                a14CI[11][0]+=1 #class +
            else:
                a14CI[11][1]+=1 #class -

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
    
    # not calculate A9

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
    a14CI[0][2] = entropy(a14CI[0][0],a14CI[0][1])
    a14CI[1][2] = entropy(a14CI[1][0],a14CI[1][1])
    a14CI[2][2] = entropy(a14CI[2][0],a14CI[2][1])
    a14CI[3][2] = entropy(a14CI[3][0],a14CI[3][1])
    a14CI[4][2] = entropy(a14CI[4][0],a14CI[4][1])
    a14CI[5][2] = entropy(a14CI[5][0],a14CI[5][1])
    a14CI[6][2] = entropy(a14CI[6][0],a14CI[6][1])
    a14CI[7][2] = entropy(a14CI[7][0],a14CI[7][1])
    a14CI[8][2] = entropy(a14CI[8][0],a14CI[8][1])
    a14CI[9][2] = entropy(a14CI[9][0],a14CI[9][1])
    a14CI[10][2] = entropy(a14CI[10][0],a14CI[10][1])
    a14CI[11][2] = entropy(a14CI[11][0],a14CI[11][1])

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
    Info_A6 = inforD(a6,[a6CI[0][2],a6CI[1][2],a6CI[2][2],a6CI[3][2],a6CI[4][2],a6CI[5][2],a6CI[6][2],a6CI[7][2],
                    a6CI[8][2],a6CI[9][2],a6CI[10][2],a6CI[11][2],a6CI[12][2],a6CI[13][2]])
    Info_A7 = inforD(a7,[a7CI[0][2],a7CI[1][2],a7CI[2][2],a7CI[3][2],a7CI[4][2],a7CI[5][2],a7CI[6][2],a7CI[7][2],a7CI[8][2]])
    Info_A8 = inforD(a8,[a8CI[0][2],a8CI[1][2],a8CI[2][2],a8CI[3][2]]) 
    #A9
    Info_A10 = inforD(a10,[a10CI[0][2],a10CI[1][2]])
    Info_A11 = inforD(a11,[a11CI[0][2],a11CI[1][2]]) 
    Info_A12 = inforD(a12,[a12CI[0][2],a12CI[1][2]])
    Info_A13 = inforD(a13,[a13CI[0][2],a13CI[1][2],a13CI[2][2]])
    Info_A14 = inforD(a14,[a14CI[0][2],a14CI[1][2],a14CI[2][2],a14CI[3][2],a14CI[4][2],a14CI[5][2],a14CI[6][2],a14CI[7][2],
                    a14CI[8][2],a14CI[9][2],a14CI[10][2],a14CI[11][2]])
    Info_A15 = inforD(a15,[a15CI[0][2],a15CI[1][2],a15CI[2][2]]) 



    # แสดงผลการทำงานLevel2 Left A9=t
    print("Level 2 Left Node A9 = t ")
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
    print("A14 count is", a14)
    print("A15 count is", a15)
    print("A16 count is", a16)
    print()

    print("A1 Info relate to class",a1CI)
    print("A2 Info relate to class",a2CI)
    print("A3 Info relate to class",a3CI)
    print("A4 Info relate to class",a4CI)
    print("A5 Info relate to class",a5CI)
    print("A6 Info relate to class",a6CI)
    print("A7 Info relate to class",a7CI)
    print("A8 Info relate to class",a8CI)
    # print("A9 Info relate to class",a9CI)
    print("A10 Info relate to class",a10CI)
    print("A11 Info relate to class",a11CI)
    print("A12 Info relate to class",a12CI)
    print("A13 Info relate to class",a13CI)
    print("A14 Info relate to class",a14CI)
    print("A15 Info relate to class",a15CI)

    print()
    print("Info(D) is %5.3f" % InD)
    print("Info(A1 = b)  is %5.3f" % a1CI[0][2])
    print("Info(A1 = a)  is %5.3f" % a1CI[1][2])

    print("Info(A2 <=25)  is %5.3f" % a2CI[0][2])
    print("Info(A2 >25 and <=30)   is %5.3f" % a2CI[1][2])
    print("Info(A2 >30 and <=40)   is %5.3f" % a2CI[2][2])
    print("Info(A2 >40)   is %5.3f" % a2CI[3][2])

    print("Info(A3 <= 1)   is %5.3f" % a3CI[0][2])
    print("Info(A3 >1 and <=3)   is %5.3f" % a3CI[1][2])
    print("Info(A3 >3 and <=8)   is %5.3f" % a3CI[2][2])
    print("Info(A3 >8)   is %5.3f" % a3CI[3][2])

    print("Info(A4 = u)  is %5.3f" % a4CI[0][2])
    print("Info(A4 = y)  is %5.3f" % a4CI[1][2])
    print("Info(A4 = l)  is %5.3f" % a4CI[2][2])
    print("Info(A4 = t)  is %5.3f" % a4CI[3][2])

    print("Info(A5 = g)  is %5.3f" % a5CI[0][2])
    print("Info(A5 = p)  is %5.3f" % a5CI[1][2])
    print("Info(A5 = gg)  is %5.3f" % a5CI[2][2])

    print("Info(A6 = c)  is %5.3f" % a6CI[0][2])
    print("Info(A6 = d) is %5.3f" % a6CI[1][2])
    print("Info(A6 = cc)  is %5.3f" % a6CI[2][2])
    print("Info(A6 = i)  is %5.3f" % a6CI[3][2])
    print("Info(A6 = j)  is %5.3f" % a6CI[4][2])
    print("Info(A6 = k)  is %5.3f" % a6CI[5][2])
    print("Info(A6 = m)  is %5.3f" % a6CI[6][2])
    print("Info(A6 = r)  is %5.3f" % a6CI[7][2])
    print("Info(A6 = q)  is %5.3f" % a6CI[8][2])
    print("Info(A6 = w)  is %5.3f" % a6CI[9][2])
    print("Info(A6 = x)  is %5.3f" % a6CI[10][2])
    print("Info(A6 = e)  is %5.3f" % a6CI[11][2])
    print("Info(A6 = aa)  is %5.3f" % a6CI[12][2])
    print("Info(A6 = ff)  is %5.3f" % a6CI[13][2])

    print("Info(A7 = v)  is %5.3f" % a7CI[0][2])
    print("Info(A7 = h)  is %5.3f" % a7CI[1][2])
    print("Info(A7 = bb)  is %5.3f" % a7CI[2][2])
    print("Info(A7 = j)  is %5.3f" % a7CI[3][2])
    print("Info(A7 = n)  is %5.3f" % a7CI[4][2])
    print("Info(A7 = z)  is %5.3f" % a7CI[5][2])
    print("Info(A7 = dd)  is %5.3f" % a7CI[6][2])
    print("Info(A7 = ff)  is %5.3f" % a7CI[7][2])
    print("Info(A7 = o)  is %5.3f" % a7CI[8][2])


    print("Info(A8 <=2)  is %5.3f" % a8CI[0][2])  
    print("Info(A8 >0.2 and <=1)   is %5.3f" % a8CI[1][2])  
    print("Info(A8 >1 and <=3)  is %5.3f" % a8CI[2][2])  
    print("Info(A8 >3)   is %5.3f" % a8CI[3][2])  


    #A9

    print("Info(A10 = t)  is %5.3f" % a10CI[0][2])
    print("Info(A10 = f)  is %5.3f" % a10CI[1][2])


    print("Info(A11 = <=3)  is %5.3f" % a11CI[0][2])
    print("Info(A11 = >3)  is %5.3f" % a11CI[1][2])


    print("Info(A12 = t)  is %5.3f" % a12CI[0][2])
    print("Info(A12 = f)  is %5.3f" % a12CI[1][2])

    print("Info(A13 = g)  is %5.3f" % a13CI[0][2])
    print("Info(A13 = p)  is %5.3f" % a13CI[1][2])
    print("Info(A13 = s)  is %5.3f" % a13CI[2][2])


    print("Info(A14 = 000XX)  is %5.3f" % a14CI[0][2])
    print("Info(A14 = 001XX)  is %5.3f" % a14CI[1][2])
    print("Info(A14 = 002XX)  is %5.3f" % a14CI[2][2])
    print("Info(A14 = 003XX)  is %5.3f" % a14CI[3][2])
    print("Info(A14 = 004XX)  is %5.3f" % a14CI[4][2])
    print("Info(A14 = 005XX)  is %5.3f" % a14CI[5][2])
    print("Info(A14 = 006XX)  is %5.3f" % a14CI[6][2])
    print("Info(A14 = 007XX) is %5.3f" % a14CI[7][2])
    print("Info(A14 = 008XX)  is %5.3f" % a14CI[8][2])
    print("Info(A14 = 009XX)  is %5.3f" % a14CI[9][2])
    print("Info(A14 = 010XX)  is %5.3f" % a14CI[10][2])
    print("Info(A14 = 020XX)  is %5.3f" % a14CI[11][2])


    print("Info(A15 <=5)  is %5.3f" % a15CI[0][2])
    print("Info(A15 >5 and <=395)  is %5.3f" % a15CI[1][2])
    print("Info(A15 >395)  is %5.3f" % a15CI[2][2])

    print()
    print("Info A1 (D) is %5.3f" % Info_A1)
    print("Info A2 (D) is %5.3f" % Info_A2)
    print("Info A3 (D) is %5.3f" % Info_A3)
    print("Info A4 (D) is %5.3f" % Info_A4)
    print("Info A5 (D) is %5.3f" % Info_A5)
    print("Info A6 (D) is %5.3f" % Info_A6)
    print("Info A7 (D) is %5.3f" % Info_A7)
    print("Info A8 (D) is %5.3f" % Info_A8)
    # print("Info A9 (D) is %5.3f" % Info_A9)
    print("Info A10 (D) is %5.3f" % Info_A10)
    print("Info A11 (D) is %5.3f" % Info_A11)
    print("Info A12 (D) is %5.3f" % Info_A12)
    print("Info A13 (D) is %5.3f" % Info_A13)
    print("Info A14 (D) is %5.3f" % Info_A14)
    print("Info A15 (D) is %5.3f" % Info_A15)

    
    print("\n***Gain results of Lv.2 Left dataset***")
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
    gainA14=InD-Info_A14
    print("Gain (A14) is %5.3f"% gainA14)
    gainA15=InD-Info_A15
    print("Gain (A15) is %5.3f"% gainA15)


    Result_All=[gainA1,gainA2,gainA3,gainA4,gainA5,gainA6,gainA7,gainA8,gainA10,gainA11,gainA12,gainA13,gainA14,gainA15]
    max_gain=max(Result_All)
    pos=np.argmax(Result_All)
    print("max gain of attb is %5.3f" % max_gain,"position is",pos)


    X3L1=[]  #ข้อมูลสำหรับสร้าง level 3 ที่ A14 = 'X00XX'
    X3L2=[]  #ข้อมูลสำหรับสร้าง level 3 ที่ A14 = 'X01XX'
    X3L3=[]  #ข้อมูลสำหรับสร้าง level 3 ที่ A14 = 'X02XX'
    X3L4=[]  #ข้อมูลสำหรับสร้าง level 3 ที่ A14 = 'X03XX'
    X3L5=[]  #ข้อมูลสำหรับสร้าง level 3 ที่ A14 = 'X04XX'
    X3L6=[]  #ข้อมูลสำหรับสร้าง level 3 ที่ A14 = 'X05XX'
    X3L7=[]  #ข้อมูลสำหรับสร้าง level 3 ที่ A14 = 'X06XX'
    X3L8=[]  #ข้อมูลสำหรับสร้าง level 3 ที่ A14 = 'X07XX'
    X3L9=[]  #ข้อมูลสำหรับสร้าง level 3 ที่ A14 = 'X08XX'
    X3L10=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A14 = 'X09XX'
    X3L11=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A14 = 'X1XXX'
    X3L12=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A14 = 'X2XXX'


    for i in range(len(dataset)):
        if (dataset.iloc[i][13][1] == '0'):     #A14 = 'X0XXX'
            if (dataset.iloc[i][13][2] == '0'):     #A14 = 'X00XX'
                X3L1.append(dataset.iloc[i])        #เก็บinstanceลงใน list สำหรับ A14 = 'X00XX' เพื่อเขียนเป็น csv
            elif (dataset.iloc[i][13][2] == '1'):   #A14 = 'X01XX'
                X3L2.append(dataset.iloc[i])        #เก็บinstanceลงใน list สำหรับ A14 = 'X01XX' เพื่อเขียนเป็น csv
            elif (dataset.iloc[i][13][2] == '2'):   #A14 = 'X02XX'
                X3L3.append(dataset.iloc[i])        #เก็บinstanceลงใน list สำหรับ A14 = 'X02XX' เพื่อเขียนเป็น csv
            elif (dataset.iloc[i][13][2] == '3'):   #A14 = 'X03XX'
                X3L4.append(dataset.iloc[i])        #เก็บinstanceลงใน list สำหรับ A14 = 'X03XX' เพื่อเขียนเป็น csv
            elif (dataset.iloc[i][13][2] == '4'):   #A14 = 'X04XX'
                X3L5.append(dataset.iloc[i])        #เก็บinstanceลงใน list สำหรับ A14 = 'X04XX' เพื่อเขียนเป็น csv
            elif (dataset.iloc[i][13][2] == '5'):   #A14 = 'X05XX'
                X3L6.append(dataset.iloc[i])        #เก็บinstanceลงใน list สำหรับ A14 = 'X05XX' เพื่อเขียนเป็น csv
            elif (dataset.iloc[i][13][2] == '6'):   #A14 = 'X06XX'
                X3L7.append(dataset.iloc[i])        #เก็บinstanceลงใน list สำหรับ A14 = 'X06XX' เพื่อเขียนเป็น csv
            elif (dataset.iloc[i][13][2] == '7'):   #A14 = 'X07XX'
                X3L8.append(dataset.iloc[i])        #เก็บinstanceลงใน list สำหรับ A14 = 'X07XX' เพื่อเขียนเป็น csv
            elif (dataset.iloc[i][13][2] == '8'):   #A14 = 'X08XX'
                X3L9.append(dataset.iloc[i])        #เก็บinstanceลงใน list สำหรับ A14 = 'X08XX' เพื่อเขียนเป็น csv
            elif (dataset.iloc[i][13][2] == '9'):   #A14 = 'X09XX'
                X3L10.append(dataset.iloc[i])       #เก็บinstanceลงใน list สำหรับ A14 = 'X09XX' เพื่อเขียนเป็น csv
        elif (dataset.iloc[i][13][1] == '1' ):      #A14 = 'X1XXX'
            X3L11.append(dataset.iloc[i])           #เก็บinstanceลงใน list สำหรับ A14 = 'X1XXX' เพื่อเขียนเป็น csv
        elif (dataset.iloc[i][13][1] == '2' ):      #A14 = 'X2XXX'
            X3L12.append(dataset.iloc[i])           #เก็บinstanceลงใน list สำหรับ A14 = 'X2XXX' เพื่อเขียนเป็น csv


    crx3L1 = pd.DataFrame(X3L1)
    crx3L2 = pd.DataFrame(X3L2)
    crx3L3 = pd.DataFrame(X3L3)
    crx3L4 = pd.DataFrame(X3L4)
    crx3L5 = pd.DataFrame(X3L5)
    crx3L6 = pd.DataFrame(X3L6)
    crx3L7 = pd.DataFrame(X3L7)
    crx3L8 = pd.DataFrame(X3L8)
    crx3L9 = pd.DataFrame(X3L9)
    crx3L10 = pd.DataFrame(X3L10)
    crx3L11 = pd.DataFrame(X3L11)
    crx3L12 = pd.DataFrame(X3L12)

    
    #write csv
    crx3L1.to_csv('data/lv3/crx3L1.csv', index=False, header=False)
    crx3L2.to_csv('data/lv3/crx3L2.csv', index=False, header=False)
    crx3L3.to_csv('data/lv3/crx3L3.csv', index=False, header=False)
    crx3L4.to_csv('data/lv3/crx3L4.csv', index=False, header=False)
    crx3L5.to_csv('data/lv3/crx3L5.csv', index=False, header=False)
    crx3L6.to_csv('data/lv3/crx3L6.csv', index=False, header=False)
    crx3L7.to_csv('data/lv3/crx3L7.csv', index=False, header=False)
    crx3L8.to_csv('data/lv3/crx3L8.csv', index=False, header=False)
    crx3L9.to_csv('data/lv3/crx3L9.csv', index=False, header=False)
    crx3L10.to_csv('data/lv3/crx3L10.csv', index=False, header=False)
    crx3L11.to_csv('data/lv3/crx3L11.csv', index=False, header=False)
    crx3L12.to_csv('data/lv3/crx3L12.csv', index=False, header=False)



        
def findmaxgainLv2R(dataset):   

    M=3 #row

    a1=np.zeros(2)
    a1CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of A1)

    a2=np.zeros(4) 
    a2CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A2)

    a3=np.zeros(4) 
    a3CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A3)

    a4=np.zeros(4)
    a4CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A4)

    a5=np.zeros(3)
    a5CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of A5)

    a6=np.zeros(14)
    a6CI=[[0 for i in range(M)] for j in range(14)] # zero matrix 14 rows 3 columns (class and info gain of A6)

    a7=np.zeros(9)
    a7CI=[[0 for i in range(M)] for j in range(9)] # zero matrix 9 rows 3 columns (class and info gain of A7)

    a8=np.zeros(4)  
    a8CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 4 rows 3 columns (class and info gain of A8)

    a10=np.zeros(2)
    a10CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of A10)

    a11=np.zeros(2) 
    a11CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of A11)

    a12=np.zeros(2)
    a12CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 2 rows 3 columns (class and info gain of A12)

    a13=np.zeros(3)
    a13CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of A13)

    a14=np.zeros(12) 
    a14CI=[[0 for i in range(M)] for j in range(12)] # zero matrix 11 rows 3 columns (class and info gain of A14)

    a15=np.zeros(3) 
    a15CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of A15)

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
        #this level

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
        if (dataset.iloc[i][13][1] == '0'): 
            if (dataset.iloc[i][13][2] == '0'): 
                a14[0]+=1 # total sample A14 = X00XX
                if (dataset.iloc[i][13][2] == '0' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[0][0]+=1 #class +
                else:
                    a14CI[0][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '1'): 
                a14[1]+=1 # total sample A14 = X01XX
                if (dataset.iloc[i][13][2] == '1' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[1][0]+=1 #class +
                else:
                    a14CI[1][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '2'): 
                a14[2]+=1 # total sample A14 = X02XX
                if (dataset.iloc[i][13][2] == '2' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[2][0]+=1 #class +
                else:
                    a14CI[2][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '3'): 
                a14[3]+=1 # total sample A14 = X03XX
                if (dataset.iloc[i][13][2] == '3' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[3][0]+=1 #class +
                else:
                    a14CI[3][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '4'): 
                a14[4]+=1 # total sample A14 = X04XX
                if (dataset.iloc[i][13][2] == '4' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[4][0]+=1 #class +
                else:
                    a14CI[4][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '5'): 
                a14[5]+=1 # total sample A14 = X05XX
                if (dataset.iloc[i][13][2] == '5' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[5][0]+=1 #class +
                else:
                    a14CI[5][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '6'): 
                a14[6]+=1 # total sample A14 = X06XX
                if (dataset.iloc[i][13][2] == '6' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[6][0]+=1 #class +
                else:
                    a14CI[6][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '7'): 
                a14[7]+=1 # total sample A14 = X07XX
                if (dataset.iloc[i][13][2] == '7' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[7][0]+=1 #class +
                else:
                    a14CI[7][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '8'): 
                a14[8]+=1 # total sample A14 = X08XX
                if (dataset.iloc[i][13][2] == '8' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[8][0]+=1 #class +
                else:
                    a14CI[8][1]+=1 #class -
            elif (dataset.iloc[i][13][2] == '9'): 
                a14[9]+=1 # total sample A14 = X09XX
                if (dataset.iloc[i][13][2] == '9' ) and (dataset.iloc[i][15] == '+'):
                    a14CI[9][0]+=1 #class +
                else:
                    a14CI[9][1]+=1 #class -
        elif (dataset.iloc[i][13][1] == '1' ): 
            a14[10]+=1 # total sample A14 = X1XXX
            if (dataset.iloc[i][13][1] == '1') and (dataset.iloc[i][15] == '+'):
                a14CI[10][0]+=1 #class +
            else:
                a14CI[10][1]+=1 #class -
        elif (dataset.iloc[i][13][1] == '2' ): 
            a14[11]+=1 # total sample A14 = X2XXX
            if (dataset.iloc[i][13][1] == '2') and (dataset.iloc[i][15] == '+'):
                a14CI[11][0]+=1 #class +
            else:
                a14CI[11][1]+=1 #class -

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

    #No attribute A9

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
    a14CI[0][2] = entropy(a14CI[0][0],a14CI[0][1])
    a14CI[1][2] = entropy(a14CI[1][0],a14CI[1][1])
    a14CI[2][2] = entropy(a14CI[2][0],a14CI[2][1])
    a14CI[3][2] = entropy(a14CI[3][0],a14CI[3][1])
    a14CI[4][2] = entropy(a14CI[4][0],a14CI[4][1])
    a14CI[5][2] = entropy(a14CI[5][0],a14CI[5][1])
    a14CI[6][2] = entropy(a14CI[6][0],a14CI[6][1])
    a14CI[7][2] = entropy(a14CI[7][0],a14CI[7][1])
    a14CI[8][2] = entropy(a14CI[8][0],a14CI[8][1])
    a14CI[9][2] = entropy(a14CI[9][0],a14CI[9][1])
    a14CI[10][2] = entropy(a14CI[10][0],a14CI[10][1])
    a14CI[11][2] = entropy(a14CI[11][0],a14CI[11][1])

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
    # Info_A9 
    Info_A10 = inforD(a10,[a10CI[0][2],a10CI[1][2]])
    Info_A11 = inforD(a11,[a11CI[0][2],a11CI[1][2]]) 
    Info_A12 = inforD(a12,[a12CI[0][2],a12CI[1][2]])
    Info_A13 = inforD(a13,[a13CI[0][2],a13CI[1][2],a13CI[2][2]])
    Info_A14 = inforD(a14,[a14CI[0][2],a14CI[1][2],a14CI[2][2],a14CI[3][2],a14CI[4][2],a14CI[5][2],a14CI[6][2],a14CI[7][2],a14CI[8][2],a14CI[9][2],a14CI[10][2],a14CI[11][2]]) #waiting
    Info_A15 = inforD(a15,[a15CI[0][2],a15CI[1][2],a15CI[2][2]]) 



    # แสดงผลการทำงาน Lv1 Right
    """
    print("A1 count is", a1)
    print("A2 count is",a2)
    print("A3 count is",a3)
    print("A4 count is",a4)
    print("A5 count is", a5)
    print("A6 count is",a6)
    print("A7 count is", a7)
    print("A8 count is", a8)
    print("A10 count is", a10)
    print("A11 count is", a11)
    print("A12 count is", a12)
    print("A13 count is", a13)
    print("A14 count is", a14)
    print("A15 count is", a15)
    print("A16 count is", a16)
    print()

    print("A1 Info relate to class",a1CI)
    print("A2 Info relate to class",a2CI)
    print("A3 Info relate to class",a3CI)
    print("A4 Info relate to class",a4CI)
    print("A5 Info relate to class",a5CI)
    print("A6 Info relate to class",a6CI)
    print("A7 Info relate to class",a7CI)
    print("A8 Info relate to class",a8CI)
    print("A10 Info relate to class",a10CI)
    print("A11 Info relate to class",a11CI)
    print("A12 Info relate to class",a12CI)
    print("A13 Info relate to class",a13CI)
    print("A14 Info relate to class",a14CI)
    print("A15 Info relate to class",a15CI)

    print()

    print("Info(D) is %5.3f" % InD)
    print("Info(A1 = b)  is %5.3f" % a1CI[0][2])
    print("Info(A1 = a)  is %5.3f" % a1CI[1][2])

    print("Info(A2 <=25)  is %5.3f" % a2CI[0][2])
    print("Info(A2 >25 and <=30)   is %5.3f" % a2CI[1][2])
    print("Info(A2 >30 and <=40)   is %5.3f" % a2CI[2][2])
    print("Info(A2 >40)   is %5.3f" % a2CI[3][2])

    print("Info(A3 <= 1)   is %5.3f" % a3CI[0][2])
    print("Info(A3 >1 and <=3)   is %5.3f" % a3CI[1][2])
    print("Info(A3 >3 and <=8)   is %5.3f" % a3CI[2][2])
    print("Info(A3 >8)   is %5.3f" % a3CI[3][2])

    print("Info(A4 = u)  is %5.3f" % a4CI[0][2])
    print("Info(A4 = y)  is %5.3f" % a4CI[1][2])
    print("Info(A4 = l)  is %5.3f" % a4CI[2][2])
    print("Info(A4 = t)  is %5.3f" % a4CI[3][2])

    print("Info(A5 = g)  is %5.3f" % a5CI[0][2])
    print("Info(A5 = p)  is %5.3f" % a5CI[1][2])
    print("Info(A5 = gg)  is %5.3f" % a5CI[2][2])

    print("Info(A6 = c  is %5.3f" % a6CI[0][2])
    print("Info(A6 = d  is %5.3f" % a6CI[1][2])
    print("Info(A6 = cc  is %5.3f" % a6CI[2][2])
    print("Info(A6 = i)  is %5.3f" % a6CI[3][2])
    print("Info(A6 = j)  is %5.3f" % a6CI[4][2])
    print("Info(A6 = k)  is %5.3f" % a6CI[5][2])
    print("Info(A6 = m)  is %5.3f" % a6CI[6][2])
    print("Info(A6 = r)  is %5.3f" % a6CI[7][2])
    print("Info(A6 = q)  is %5.3f" % a6CI[8][2])
    print("Info(A6 = w)  is %5.3f" % a6CI[9][2])
    print("Info(A6 = x)  is %5.3f" % a6CI[10][2])
    print("Info(A6 = e)  is %5.3f" % a6CI[11][2])
    print("Info(A6 = aa)  is %5.3f" % a6CI[12][2])
    print("Info(A6 = ff)  is %5.3f" % a6CI[13][2])

    print("Info(A7 = v)  is %5.3f" % a7CI[0][2])
    print("Info(A7 = h)  is %5.3f" % a7CI[1][2])
    print("Info(A7 = bb)  is %5.3f" % a7CI[2][2])
    print("Info(A7 = j)  is %5.3f" % a7CI[3][2])
    print("Info(A7 = n)  is %5.3f" % a7CI[4][2])
    print("Info(A7 = z)  is %5.3f" % a7CI[5][2])
    print("Info(A7 = dd)  is %5.3f" % a7CI[6][2])
    print("Info(A7 = ff)  is %5.3f" % a7CI[7][2])
    print("Info(A7 = o)  is %5.3f" % a7CI[8][2])


    print("Info(A8 <=2)  is %5.3f" % a8CI[0][2])  
    print("Info(A8 >0.2 and <=1)   is %5.3f" % a8CI[1][2])  
    print("Info(A8 >1 and <=3)  is %5.3f" % a8CI[2][2])  
    print("Info(A8 >3)   is %5.3f" % a8CI[3][2])  


    print("Info(A10 = t)  is %5.3f" % a10CI[0][2])
    print("Info(A10 = f)  is %5.3f" % a10CI[1][2])


    print("Info(A11 = <=3)  is %5.3f" % a11CI[0][2])
    print("Info(A11 = >3)  is %5.3f" % a11CI[1][2])


    print("Info(A12 = t)  is %5.3f" % a12CI[0][2])
    print("Info(A12 = f)  is %5.3f" % a12CI[1][2])

    print("Info(A13 = g)  is %5.3f" % a13CI[0][2])
    print("Info(A13 = p)  is %5.3f" % a13CI[1][2])
    print("Info(A13 = s)  is %5.3f" % a13CI[2][2])


    print("Info(A14 = 000XX)  is %5.3f" % a14CI[0][2])
    print("Info(A14 = 001XX)  is %5.3f" % a14CI[1][2])
    print("Info(A14 = 002XX)  is %5.3f" % a14CI[2][2])
    print("Info(A14 = 003XX)  is %5.3f" % a14CI[3][2])
    print("Info(A14 = 004XX)  is %5.3f" % a14CI[4][2])
    print("Info(A14 = 005XX)  is %5.3f" % a14CI[5][2])
    print("Info(A14 = 006XX)  is %5.3f" % a14CI[6][2])
    print("Info(A14 = 007XX) is %5.3f" % a14CI[7][2])
    print("Info(A14 = 008XX)  is %5.3f" % a14CI[8][2])
    print("Info(A14 = 009XX)  is %5.3f" % a14CI[9][2])
    print("Info(A14 = 010XX)  is %5.3f" % a14CI[10][2])
    print("Info(A14 = 020XX)  is %5.3f" % a14CI[11][2])


    print("Info(A15 <=5)  is %5.3f" % a15CI[0][2])
    print("Info(A15 >5 and <=395)  is %5.3f" % a15CI[1][2])
    print("Info(A15 >395)  is %5.3f" % a15CI[2][2])

    print()
    print("Info A1 (D) is %5.3f" % Info_A1)
    print("Info A2 (D) is %5.3f" % Info_A2)
    print("Info A3 (D) is %5.3f" % Info_A3)
    print("Info A4 (D) is %5.3f" % Info_A4)
    print("Info A5 (D) is %5.3f" % Info_A5)
    print("Info A6 (D) is %5.3f" % Info_A6)
    print("Info A7 (D) is %5.3f" % Info_A7)
    print("Info A8 (D) is %5.3f" % Info_A8)
    print("Info A10 (D) is %5.3f" % Info_A10)
    print("Info A11 (D) is %5.3f" % Info_A11)
    print("Info A12 (D) is %5.3f" % Info_A12)
    print("Info A13 (D) is %5.3f" % Info_A13)
    print("Info A14 (D) is %5.3f" % Info_A14)
    print("Info A15 (D) is %5.3f" % Info_A15)
    """
    
    print("\n***Gain results of Lv.2 Right dataset***")
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
    gainA10=InD-Info_A10
    print("Gain (A10) is %5.3f"% gainA10)
    gainA11=InD-Info_A11
    print("Gain (A11) is %5.3f"% gainA11)
    gainA12=InD-Info_A12
    print("Gain (A12) is %5.3f"% gainA12)
    gainA13=InD-Info_A13
    print("Gain (A13) is %5.3f"% gainA13)
    gainA14=InD-Info_A14
    print("Gain (A14) is %5.3f"% gainA14)
    gainA15=InD-Info_A15
    print("Gain (A15) is %5.3f"% gainA15)



    #rule of Lv1 Right node

    Result_All=[gainA1,gainA2,gainA3,gainA4,gainA5,gainA6,gainA7,gainA8,gainA10,gainA11,gainA12,gainA13,gainA14,gainA15]
    max_gain=max(Result_All)
    pos=np.argmax(Result_All)
    print("max gain of attb is %5.3f" % max_gain,"position is",pos)
  

    X4L11=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A6 = c
    X4L12=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A6 = d
    X4L13=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A6 = cc
    X4L14=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A6 = i
    X4L15=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A6 = j
    X4L16=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A6 = k
    X4L17=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A6 = m
    X4L18=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A6 = r
    X4L19=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A6 = q
    X4L110=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A6 = w
    X4L111=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A6 = x
    X4L112=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A6 = e
    X4L113=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A6 = aa
    X4L114=[] #ข้อมูลสำหรับสร้าง level 3 ที่ A6 = ff


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
    crx3R1 = pd.DataFrame(X4L11)
    crx3R2 = pd.DataFrame(X4L12)
    crx3R3 = pd.DataFrame(X4L13)
    crx3R4 = pd.DataFrame(X4L14)
    crx3R5 = pd.DataFrame(X4L15)
    crx3R6 = pd.DataFrame(X4L16)
    crx3R7 = pd.DataFrame(X4L17)
    crx3R8 = pd.DataFrame(X4L18)
    crx3R9 = pd.DataFrame(X4L19)
    crx3R10 = pd.DataFrame(X4L110)
    crx3R11 = pd.DataFrame(X4L111)
    crx3R12 = pd.DataFrame(X4L112)
    crx3R13 = pd.DataFrame(X4L113)
    crx3R14 = pd.DataFrame(X4L114)

    crx3R1.to_csv('data/lv3/crx3R1.csv', index=False, header=False)
    crx3R2.to_csv('data/lv3/crx3R2.csv', index=False, header=False)
    crx3R3.to_csv('data/lv3/crx3R3.csv', index=False, header=False)
    crx3R4.to_csv('data/lv3/crx3R4.csv', index=False, header=False)
    crx3R5.to_csv('data/lv3/crx3R5.csv', index=False, header=False)
    crx3R6.to_csv('data/lv3/crx3R6.csv', index=False, header=False)
    crx3R7.to_csv('data/lv3/crx3R7.csv', index=False, header=False)
    crx3R8.to_csv('data/lv3/crx3R8.csv', index=False, header=False)
    crx3R9.to_csv('data/lv3/crx3R9.csv', index=False, header=False)
    crx3R10.to_csv('data/lv3/crx3R10.csv', index=False, header=False)
    crx3R11.to_csv('data/lv3/crx3R11.csv', index=False, header=False)
    crx3R12.to_csv('data/lv3/crx3R12.csv', index=False, header=False)
    crx3R13.to_csv('data/lv3/crx3R13.csv', index=False, header=False)
    crx3R14.to_csv('data/lv3/crx3R14.csv', index=False, header=False)
