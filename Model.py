import numpy as np
import re
import matplotlib.pyplot as plt 
import os

class Model:
    
    def __init__(self):
        self.filesHam = []
        self.filesSpam = []
        self.wordMapHam = {}
        self.wordMapSpam = {}
        self.totalNumberHam = 0
        self.totalNumberSpam = 0
    
    
        for i in os.listdir(os.getcwd()+ "/train"):
            if "ham" in i: 
                self.filesHam.append(os.getcwd()+ "/train/" + i)
            if "spam" in i: 
                self.filesSpam.append(os.getcwd()+ "/train/" + i)
        
        for i in self.filesHam: 
            for line in open(i):
                temp = re.split('[^a-zA-Z]',line.lower())
                for word in temp:
                    self.totalNumberHam +=1
                    #Only if the word exists
                    if word in self.wordMapHam:
                        self.wordMapHam[word] +=1
                    else:
                        self.wordMapHam[word] = 1
                        self.wordMapSpam[word] = 0
        
        for i in self.filesSpam: 
            for line in open(i):
                temp = re.split('[^a-zA-Z]',line.lower())
                for word in temp:
                    self.totalNumberSpam +=1
                    #Only if the word exists
                    if word in self.wordMapSpam:
                        self.wordMapSpam[word] +=1
                    else:
                        self.wordMapSpam[word] = 1
                        self.wordMapHam[word] = 0
        
        i = 1
        output =  open("model.txt","w")
        
        for keyWord in sorted(self.wordMapHam): 
            output.write(str(i) + "  " + keyWord + "  " + str(self.wordMapHam[keyWord]) + "  " + str(self.wordMapHam[keyWord]/self.totalNumberHam) + "  " + str(self.wordMapSpam[keyWord]) + "  " + str(self.wordMapSpam[keyWord]/self.totalNumberSpam) )
            output.write("\n")
            i += 1


