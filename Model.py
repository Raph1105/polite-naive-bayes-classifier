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
        
    def buildBaselineModel(self):
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
                        self.wordMapHam[word] = 1.5
                        self.wordMapSpam[word] = 0.5
        
        for i in self.filesSpam: 
            for line in open(i):
                temp = re.split('[^a-zA-Z]',line.lower())
                for word in temp:
                    self.totalNumberSpam +=1
                    #Only if the word exists
                    if word in self.wordMapSpam:
                        self.wordMapSpam[word] +=1
                    else:
                        self.wordMapSpam[word] = 1.5
                        self.wordMapHam[word] = 0.5
        
        i = 1
        output =  open("model.txt","w")
        
        for keyWord in sorted(self.wordMapHam): 
            output.write(str(i) + "  " + keyWord + "  " + str(self.wordMapHam[keyWord]) + "  " + str(self.wordMapHam[keyWord]/(1.5*self.totalNumberHam)) + "  " + str(self.wordMapSpam[keyWord]) + "  " + str(self.wordMapSpam[keyWord]/(1.5*self.totalNumberSpam)) )
            output.write("\n")
            i += 1
        
        output.close()
#Stopwords
    def buildStopModel(self):
        self.filesHam = []
        self.filesSpam = []
        self.wordMapHam = {}
        self.wordMapSpam = {}
        self.totalNumberHam = 0
        self.totalNumberSpam = 0
        
        self.stopwords = []
    
        with open("stopwords.txt","r") as f:
            for word in f:
                self.stopwords.append(word.strip())
    
        for i in os.listdir(os.getcwd()+ "/train"):
            if "ham" in i: 
                self.filesHam.append(os.getcwd()+ "/train/" + i)
            if "spam" in i: 
                self.filesSpam.append(os.getcwd()+ "/train/" + i)
        
        for i in self.filesHam: 
            for line in open(i):
                temp = re.split('[^a-zA-Z]',line.lower())
                for word in temp:
                    if word not in self.stopwords:
                        self.totalNumberHam +=1
                        #Only if the word exists
                        if word in self.wordMapHam:
                            self.wordMapHam[word] +=1
                        else:
                            self.wordMapHam[word] = 1.5
                            self.wordMapSpam[word] = 0.5
        
        for i in self.filesSpam: 
            for line in open(i):
                temp = re.split('[^a-zA-Z]',line.lower())
                for word in temp:
                    if word not in self.stopwords:
                        self.totalNumberSpam +=1
                        #Only if the word exists
                        if word in self.wordMapSpam:
                            self.wordMapSpam[word] +=1
                        else:
                            self.wordMapSpam[word] = 1.5
                            self.wordMapHam[word] = 0.5
        
        i = 1
        output =  open("model.txt","w")
        
        for keyWord in sorted(self.wordMapHam): 
            output.write(str(i) + "  " + keyWord + "  " + str(self.wordMapHam[keyWord]) + "  " + str(self.wordMapHam[keyWord]/(1.5*self.totalNumberHam)) + "  " + str(self.wordMapSpam[keyWord]) + "  " + str(self.wordMapSpam[keyWord]/(1.5*self.totalNumberSpam)) )
            output.write("\n")
            i += 1
        
        output.close()
        
#WordLength
    def buildWordLengthModel(self):
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
                    if len(word)>=2 and len(word)<=9 :
                        self.totalNumberHam +=1
                        #Only if the word exists
                        if word in self.wordMapHam:
                            self.wordMapHam[word] +=1
                        else:
                            self.wordMapHam[word] = 1.5
                            self.wordMapSpam[word] = 0.5
        
        for i in self.filesSpam: 
            for line in open(i):
                temp = re.split('[^a-zA-Z]',line.lower())
                for word in temp:
                    if len(word)>=2 and len(word)<=9:
                        self.totalNumberSpam +=1
                        #Only if the word exists
                        if word in self.wordMapSpam:
                            self.wordMapSpam[word] +=1
                        else:
                            self.wordMapSpam[word] = 1.5
                            self.wordMapHam[word] = 0.5
        
        i = 1
        output =  open("model.txt","w")
        
        for keyWord in sorted(self.wordMapHam): 
            output.write(str(i) + "  " + keyWord + "  " + str(self.wordMapHam[keyWord]) + "  " + str(self.wordMapHam[keyWord]/(1.5*self.totalNumberHam)) + "  " + str(self.wordMapSpam[keyWord]) + "  " + str(self.wordMapSpam[keyWord]/(1.5*self.totalNumberSpam)) )
            output.write("\n")
            i += 1
        
        output.close()
