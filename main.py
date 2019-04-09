# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 00:11:23 2019

@author: Julia
"""

import PSpy
import WhiteningFilterspy
import ICApy
import numpy as np

#defining read and write directories


inputFileName = "/home/uei/pamplona/datasets/autonomousVehicle/greyImages.hdf5"
resultsDirectory = "images/"
#resultsDirectory = "C:/Users/Julia/Desktop/Graduação/MI210/images"


#defining images and output file names 
averagePSResultsFileName = resultsDirectory + "averagePS.hdf5" 
averagePSFigureFileName = resultsDirectory + "averagePS.png"

averagePSLocalResultsFileName = resultsDirectory + "averagePSLocal.hdf5" 
averagePSLocalFigureFileName = resultsDirectory + "averagePSLocal.png"

whiteningFiltersFigureFileName = resultsDirectory + "whiteningFilters.png"
whiteningFiltersResultsFileName = resultsDirectory + "whiteningFilters.hdf5"

ICResultsFileName = resultsDirectory +  "IC.hdf5"
ICFigureFileName = resultsDirectory + "IC.png"

ICASourcesResultsFileName = resultsDirectory +"SourcesICA.hdf5"
ICASourcesSparsenessFigureFileName = resultsDirectory +"SourcesICA.png"

#defining some parameters
sampleSizePS = [36,36] #image sample size for the power spectrum
gridSize = [3,3]
numberOfSamplesPS = 10000; #number of samples from the dataset for estimating PS



sampleSizeICA = [12,12] #image sample size for the ICA
numberOfSamplesICA = 50000; #number of samples from the dataset for making ICA


#power spectrum estimation functions
averagePS = PSpy.getAveragePS(inputFileName, sampleSizePS,numberOfSamplesPS)
'''
PSpy.saveH5(averagePSResultsFileName,'averagePS',averagePS)
PSpy.makeAveragePSFigure(averagePS, averagePSFigureFileName)
 
averagePSRadial = PSpy.getRadialPS(averagePS)
radialFreq = PSpy.getRadialFreq(averagePS.shape)
PSpy.saveH5(averagePSRadialResultsFileName,'averagePSRadial',averagePSRadial)
PSpy.makeAveragePSRadialFigure(radialFreq,averagePSRadial, averagePSRadialFigureFileName)

averagePSLocal = PSpy.getAveragePSLocal(inputFileName, sampleSize, gridSize)
PSpy.saveH5(averagePSLocalResultsFileName,'averagePS',averagePSLocal)
PSpy.makeAveragePSLocalFigure(averagePSLocal, averagePSLocalFigureFileName,gridSize)

#whitening filters estimation functions

averagePS = PSpy.readH5(averagePSResultsFileName,'averagePS')

maxPS = np.max(averagePS);
noiseVarianceList = [maxPS*10**(-9),maxPS*10**(-8),maxPS*10**(-7),maxPS*10**(-6)] #if you do not see anything interesting you can change this values

whiteningFilters = [];
for noiseVariance in noiseVarianceList:
    whiteningFilters.append(WhiteningFilterspy.getPowerSpectrumWhiteningFilter(averagePS,noiseVariance))

PSpy.saveH5(whiteningFiltersResultsFileName,'whiteningFilters',np.array(whiteningFilters))
WhiteningFilterspy.makeWhiteningFiltersFigure(whiteningFilters,whiteningFiltersFigureFileName)


#ica estimation functions


X = ICApy.getICAInputData(inputFileName, sampleSizeICA, numberOfSamplesICA)
X = ICApy.preprocess(X);
W = ICApy.getIC(X)

PSpy.saveH5(ICResultsFileName,'IC',W)
ICApy.makeIdependentComponentsFigure(W,sampleSizeICA, ICFigureFileName)

S = ICApy.estimateSources(W,X)
K = ICApy.estimateSourcesKurtosis(S)
PSpy.saveH5(ICASourcesResultsFileName,'Sources',S)
ICApy.makeKurtosisFigure(S, ICASourcesSparsenessFigureFileName)

'''
