# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:19:51 2019

@author: m_taran
"""
import numpy as np
import re
import os

class Classifier:
    
    #Setup main data members
    def __init__(self):
        self.name = "none"
        self.resultBuffer = []
        self.wordMap = {}
        self.count = []
        self.PwHAM = np.zeros(1)
        self.PwSPAM = np.zeros(1)
    
    #Load data members based on modelFile given
    #Must specify name otherwise model.txt assumed
    def loadModel(self, modelFile = "model.txt"):
        
        self.name = modelFile.split(".")[0]
        
        file = open(modelFile)
        
        tempHam = []
        tempSpam = []
        
        for line in file:
            temp = line.strip().split("  ")
            self.wordMap[temp[1]] = int(temp[0])-1
            self.count.append(0)
            tempHam.append(float(temp[3]))
            tempSpam.append(float(temp[5]))
            
        self.PwHAM = np.array(tempHam)
        self.PwSPAM = np.array(tempSpam)
        
        file.close()
        
    #Evaluate a single file based on the current model
    def evaluateFile(self, fileName,path="",):
        #Determine expected result
        if "ham" in fileName:
            expected = "ham"
        else:
            expected = "spam"
        
        #Open file
        file = open(path+fileName,encoding='Latin-1')
        
        #Reset counts
        for i in range(len(self.count)):
            self.count[i] = 0
        
        #Increment counts of words in vocabulary
        for line in file:
            temp = re.split('[^a-zA-Z]',line.lower())
            for word in temp:
                #Only if the word exists
                if word in self.wordMap:
                    self.count[self.wordMap[word]] +=1
        
        #Calculate scores
        hamScore = np.log10(self.PwHAM)@self.count
        spamScore = np.log10(self.PwSPAM)@self.count
        
        if hamScore>=spamScore:
            choice = "ham"
        else:
            choice = "spam"
        
        if choice == expected:
            label = "right"
        else:
            label = "wrong"
        
        #Update resultBuffer
        self.resultBuffer.append([str(len(self.resultBuffer)+1),fileName,choice,str(hamScore),str(spamScore),expected,label])
        
        file.close()
    
    #Be sure to pass the folder name in the form \[name]
    #Be sure that the folder is located in the same level as the driver file
    #If either of those is not the case, the program is unlikely to open and evaluate
    #all files in the folder
    def evaluateAllInFolder(self,folderName):
        
        folder = os.listdir(os.getcwd()+folderName)
        
        for file in folder:
            self.evaluateFile(file, os.getcwd()+folderName+"\\")
    
    #Write contents of results to a text file
    def writeBufferToFile(self):
        resultsFileName = self.name.replace("model","result")+".txt"
        resultsFile = open(resultsFileName,"w")
        
        for item in self.resultBuffer:
            resultsFile.write("  ".join(item))
            resultsFile.write("\n")
            
        resultsFile.close()
        