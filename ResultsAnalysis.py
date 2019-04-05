# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:44:55 2019

@author: m_taran
"""

import matplotlib.pyplot as plt
import numpy as np 

hamList = []
spamList = []
mat = []

A = 0
B = 0
C = 0
D = 0

with open("baseline-result.txt","r") as f:
    for line in f:
        temp = line.split("  ")
        if temp[2] == "ham":
            if temp[5] == "ham":
                A+=1
            else:
                C+=1
        else:
            if temp[5] == "spam":
                D+=1
            else:
                B+=1

mat.append([A,B,C,D])

p1 = A/(A+B)
r1 = A/(A+C)

hamList.append([(A+D)/(A+D+C+B), p1, r1, 2*p1*r1/(p1+r1)])

p2 = D/(D+C)
r2 = D/(D+B)

spamList.append([(A+D)/(A+D+C+B), p2, r2, 2*p2*r2/(p2+r2)])

A = 0
B = 0
C = 0
D = 0

with open("stopwords-result.txt","r") as f:
    for line in f:
        temp = line.split("  ")
        if temp[2] == "ham":
            if temp[5] == "ham":
                A+=1
            else:
                C+=1
        else:
            if temp[5] == "spam":
                D+=1
            else:
                B+=1

mat.append([A,B,C,D])
      
p1 = A/(A+B)
r1 = A/(A+C)

hamList.append([(A+D)/(A+D+C+B), p1, r1, 2*p1*r1/(p1+r1)])

p2 = D/(D+C)
r2 = D/(D+B)

spamList.append([(A+D)/(A+D+C+B), p2, r2, 2*p2*r2/(p2+r2)])

A = 0
B = 0
C = 0
D = 0

with open("wordlength-result.txt","r") as f:
    for line in f:
        temp = line.split("  ")
        if temp[2] == "ham":
            if temp[5] == "ham":
                A+=1
            else:
                C+=1
        else:
            if temp[5] == "spam":
                D+=1
            else:
                B+=1
 
mat.append([A,B,C,D])
               
p1 = A/(A+B)
r1 = A/(A+C)

hamList.append([(A+D)/(A+D+C+B), p1, r1, 2*p1*r1/(p1+r1)])

p2 = D/(D+C)
r2 = D/(D+B)

spamList.append([(A+D)/(A+D+C+B), p2, r2, 2*p2*r2/(p2+r2)])

titles = ['Baseline Confusion Matrix','Stopwords Confusion Matrix','WordLength Confusion Matrix']

for i in range(3):
    clust_data = np.array([[mat[i][0],mat[i][1]],[mat[i][2],mat[i][3]]])
    collabel=('Actual Ham','Actual Spam')
    rowLabel=('Predicted Ham','Predicted Spam')
    
    plt.axis('off')
    the_table = plt.table(cellText=clust_data,colLabels=collabel, rowLabels=rowLabel,loc='center')
    
    plt.title(titles[i],y=0.65)
    plt.show()