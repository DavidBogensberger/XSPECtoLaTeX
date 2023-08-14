#This code uses an input string of a standard XSPEC output of the parameters, and errors of the parameters, and converts it into a LaTex compatible format.

import numpy as np
import math

#input the parameters as a string for the parameter Itxr below, in the same format as is shown here. Make sure that all the new lines are deleted, so the entire entry acts as one string. 

Itxr = "   3    3   zTBabs     nH         10^22    15.3363      +/-  0.223211        4    3   zTBabs     Redshift            1.81900E-03  frozen   5    4   powerlaw   PhoIndex            1.64028      +/-  2.56684E-02     6    4   powerlaw   norm                0.123691     +/-  5.71198E-03     7    5   gaussian   LineE      keV      6.38330      +/-  6.64119E-03     8    5   gaussian   Sigma      keV      1.87832E-02  +/-  3.58059E-03     9    5   gaussian   norm                2.51810E-04  +/-  2.60813E-05    10    6   gaussian   LineE      keV      1.73718      +/-  1.75231E-03    11    6   gaussian   Sigma      keV      3.21755E-03  +/-  7.28040E-04    12    6   gaussian   norm                3.52250E-03  +/-  5.79174E-04    13    7   gaussian   LineE      keV      2.30402      +/-  6.93591E-03    14    7   gaussian   Sigma      keV      2.09709E-03  +/-  2.72130E-03    15    7   gaussian   norm                3.05840E-04  +/-  9.18047E-05    16    8   constant   factor              2.70452E-03  +/-  2.44195E-04  "

#Similarly, for the error:

Itxe = "     3      15.2828      15.3874    (-0.0535163,0.0510769)     5      1.63792      1.64258    (-0.00236093,0.00230104)     6     0.123268     0.124147    (-0.000422981,0.000456704)     7      6.38067      6.38668    (-0.00262524,0.00338101)     8    0.0159503    0.0233946    (-0.00283299,0.00461134)     9  0.000222234  0.000268758    (-2.95759e-05,1.69478e-05)    10      1.73638      1.73775    (-0.00079526,0.000574295)    11   0.00234676   0.00409084    (-0.000870786,0.000873292)    12   0.00290763   0.00388129    (-0.00061487,0.000358785)    13      2.30206      2.30518    (-0.00196434,0.00115808)    14            0   0.00431441    (-0.00209709,0.00221731)    15  0.000239778  0.000407738    (-6.60618e-05,0.000101898)    16   0.00257711   0.00296508    (-0.000127416,0.000260559)    20      1.01061      1.02486    (-0.00683213,0.00741552)"

#print(Itxr, Itxe)

#Now select the numbers of interest:

Nts = [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] #Number corresponding to the set of parameters to select. Make sure that each entry is larger than its preceding one. 

Ftm = [1, 1, 1, 1, 1000, 10000, 1, 1000, 10000, 1, 1000, 10000, 1000] #Factor to multiply results by, for putting in table. Manually adjust based on preference.

#The following section selects the relevant numbers from the results and error strings, and converts them into numbers. 

N = len(Nts)

R = [0]*N
Re = [[0,0] for i in range(N)]

u = 0
for i in range(1, len(Itxr)-1):
    if math.floor(Nts[u]/10) == 0:
        if Itxr[i] == str(Nts[u]):
            if Itxr[i-1] == ' ':
                if Itxr[i+1] == ' ':
                    if Itxr[i+5].isnumeric() == 1:
                        R1 = Itxr[i]
                        j = 1
                        while Itxr[i+j] != "+":
                            R1+= Itxr[i+j]
                            j += 1
                        i += j
                        k1 = 0
                        while R1[-1-k1].isnumeric() == 0:
                            k1 += 1
                        k = 0
                        while k < 15:
                            if R1[-1-k1-k].isnumeric() == 1:
                                k += 1
                            elif R1[-1-k1-k] == '-':
                                k += 1
                            elif R1[-1-k1-k] == 'E':
                                k += 1
                            elif R1[-1-k1-k] == '.':
                                k += 1
                            else:
                                break
                        R2 = ''
                        for m in range(len(R1)-k-k1, len(R1)-k1):
                            R2 += R1[m]
                        R2 = float(R2) * Ftm[u]
                        R[u] = R2
                        u += 1
    else:
        if Itxr[i] == str(math.floor(Nts[u]/10)):
            if Itxr[i+1] == str(Nts[u]%10):
                if Itxr[i-1] == ' ':
                    if Itxr[i+2] == ' ':
                        if Itxr[i+6].isnumeric() == 1:
                            R1 = Itxr[i]
                            j = 1
                            while Itxr[i+j] != "+":
                                R1+= Itxr[i+j]
                                j += 1
                            i += j
                            k1 = 0
                            while R1[-1-k1].isnumeric() == 0:
                                k1 += 1
                            k = 0
                            while k < 15:
                                if R1[-1-k1-k].isnumeric() == 1:
                                    k += 1
                                elif R1[-1-k1-k] == '-':
                                    k += 1
                                elif R1[-1-k1-k] == 'E':
                                    k += 1
                                elif R1[-1-k1-k] == '.':
                                    k += 1
                                else:
                                    break
                            R2 = ''
                            for m in range(len(R1)-k-k1, len(R1)-k1):
                                R2 += R1[m]
                            R2 = float(R2) * Ftm[u]
                            R[u] = R2
                            u += 1
                            if u == N:
                                break
                        

print('\nR = ', R)

#Now repeat for the errors.
u = 0
for i in range(1, len(Itxe)-1):
    if math.floor(Nts[u]/10) == 0:
        if Itxe[i] == str(Nts[u]):
            if Itxe[i-1] == ' ':
                if Itxe[i+1] == ' ':
                    em, ep = '', ''
                    j = 1
                    while Itxe[i+j] != '(':
                        j += 1
                    i += j + 1
                    k1 = 0
                    while Itxe[i+k1] != ',':
                        em += Itxe[i+k1]
                        k1 += 1
                    i += k1 + 1
                    k2 = 0
                    while Itxe[i+k2] != ')':
                        ep += Itxe[i+k2]
                        k2 += 1
                    i += k2
                    Em, Ep = float(em) * Ftm[u], float(ep) * Ftm[u]
                    Re[u][0] = Em
                    Re[u][1] = Ep
                    u += 1
    else:
        if Itxe[i] == str(math.floor(Nts[u]/10)):
            if Itxe[i+1] == str(Nts[u]%10):
                if Itxe[i-1] == ' ':
                    if Itxe[i+2] == ' ':
                        em, ep = '', ''
                        j = 1
                        while Itxe[i+j] != '(':
                            j += 1
                        i += j + 1
                        k1 = 0
                        while Itxe[i+k1] != ',':
                            em += Itxe[i+k1]
                            k1 += 1
                        i += k1 + 1
                        k2 = 0
                        while Itxe[i+k2] != ')':
                            ep += Itxe[i+k2]
                            k2 += 1
                        i += k2
                        Em, Ep = float(em) * Ftm[u], float(ep) * Ftm[u]
                        Re[u][0] = Em
                        Re[u][1] = Ep
                        u += 1
                        if u == N:
                            break
print('\nRe = ', Re)

#Now determine where the first significant figure occurs relative to 0.

def p10fsf(x): #power of 10 first significant figure.
    sfx = 4
    while math.floor(np.abs(x)/10**sfx) == 0:
        sfx -= 1
    return sfx

FsfR = [p10fsf(R[u]) for u in range(N)]
FsfRe = [[p10fsf(Re[u][k]) for k in range(2)] for u in range(N)]

print('FsfR = ', FsfR)
print('FsfRe = ', FsfRe)

#Find which of the two errors is larger.
iLe = [0]*N #Larger
ile = [1]*N #smaller
for i in range(N):
    if Re[i][1] > np.abs(Re[i][0]):
        iLe[i] = 1
        ile[i] = 0
#print(ile)

#Determine how many sf to show for the number and error:
SFR = [0]*N
SFRe = [[0]*2 for i in range(N)]
for i in range(N):
    if FsfR[i] - FsfRe[i][iLe[i]] > 1:
        SFR[i] = 1 + (FsfR[i] - FsfRe[i][iLe[i]])
        SFRe[i][iLe[i]] = 1
        SFRe[i][ile[i]] = 1
    elif FsfR[i] - FsfRe[i][iLe[i]] == 1:
        SFR[i] = 3
        SFRe[i][iLe[i]] = 2
        if FsfRe[i][iLe[i]] == FsfRe[i][ile[i]]:
            SFRe[i][ile[i]] = 2
        else:
            SFRe[i][ile[i]] = 1
    elif FsfR[i] - FsfRe[i][iLe[i]] == 0:
        SFR[i] = 2
        SFRe[i][iLe[i]] = 2
        if FsfRe[i][iLe[i]] == FsfRe[i][ile[i]]:
            SFRe[i][ile[i]] = 2
        else:
            SFRe[i][ile[i]] = 1
    else:
        SFR[i] = 1
        SFRe[i][iLe[i]] = 2
        if FsfRe[i][iLe[i]] == FsfRe[i][ile[i]]:
            SFRe[i][ile[i]] = 2
        else:
            SFRe[i][ile[i]] = 1

print("\nSFR = ", SFR)

print("\nSFRe = ", SFRe)

#Now determine whether to do a single plus minus, or distinguish between the two errors.
EE = [0]*N #When this is 1, the errors are equal, and I can use \pm
for i in range(N):
    if np.abs(Re[i][iLe[i]]/Re[i][ile[i]]) < 1.05: #Can adjust this value to whatever suits you. 
        if SFRe[i][0] == SFRe[i][1]:
            EE[i] = 1
#print('\nEE = ', EE)

#And now generate all the errors in latex format:

LX = ['$' for i in range(N)]
for i in range(N):
    #First the value:
    if FsfR[i] - SFR[i] > -1:
        r0 = int(round(R[i]))
        r = str(round(r0, SFR[i]-FsfR[i]-1))
    else:
        r = str(round(R[i], SFR[i]-FsfR[i]-1))
    LX[i] += r
    #Now the error:
    if EE[i] == 1:
        if FsfRe[i][iLe[i]] - SFRe[i][iLe[i]] > -1:
            re0 = int(round(0.5*(np.abs(Re[i][0])+Re[i][1])))
            re = str(round(re0, SFRe[i][iLe[i]]-FsfRe[i][iLe[i]]-1))
        else:
            re = str(round(0.5*(np.abs(Re[i][0])+Re[i][1]), SFRe[i][iLe[i]]-FsfRe[i][iLe[i]]-1))
        LX[i] += '\pm' + re
    else:
        if FsfRe[i][1] - SFRe[i][1] > -1:
            re0 = int(round(Re[i][1]))
            rp = str(round(re0, SFRe[i][1]-FsfRe[i][1]-1))
        else:
            rp = str(round(Re[i][1], SFRe[i][1]-FsfRe[i][1]-1))
        LX[i] += '^{+'+rp+'}'
        if FsfRe[i][0] - SFRe[i][0] > -1:
            re0 = int(round(Re[i][0]))
            rm = str(round(re0, SFRe[i][0]-FsfRe[i][0]-1))
        else:
            rm = str(round(Re[i][0], SFRe[i][0]-FsfRe[i][0]-1))
        LX[i] += '_{'+rm+'}'
    LX[i] += '$'

#Output is printed in a way that can easily be copy pasted.         
print('\nOutput:')
for i in range(N):
    print(LX[i])
        

           
            
            
        
