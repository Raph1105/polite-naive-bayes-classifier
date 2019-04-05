# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:32:06 2019

@author: m_taran
"""

import Classifier
import numpy as np
import Model

mod = Model.Model()

#mod.buildBaselineModel()
#mod.buildStopModel()
mod.buildWordLengthModel()

test = Classifier.Classifier()
test.loadModel()
test.evaluateAllInFolder("\\test")
#test.evaluateFile("test-ham-00001.txt")
test.writeBufferToFile()
#print(test.PwHAM@test.PwSPAM)
#print(test.name,test.PwHAM,test.PwSPAM, test.wordMap)