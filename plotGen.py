#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 11:15:10 2018

@author: Dan
"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def spectrum(n):

    #Generate peak parameters using Warwick ID (command line argument) as random seed. 
    np.random.seed(n)
    s=str(n)+"_spectrum.csv"
  
    #Peak0 lies in range 1710-1720, Peak1 in the range 1730-1740, and peak3 is a shoulder 3-4 away (high or low side) from either peak 0 or peak1
    peak0=np.random.randint(1710,1720)
    peak1=np.random.randint(1730,1740)
    
    #Decide which peak has the shoulder
    peakChoice=np.random.randint(0,2) #random range is exclusive of upper number

    #determine how far away the shoulder is
    offset=np.random.uniform(3,4)
    offsetSign=np.random.randint(0,2)
    
    if offsetSign==0:
        offset=-offset
    
    if peakChoice==0:
        peak2=peak0+offset
    else:
        peak2=peak1+offset
    
    #Peaks have different amplitudes, but the same spectral width    
    peakAmp=np.random.uniform(1,3,3)
    peakWidth=np.random.uniform(1.5,2)
    
    #Generate simulated spectrum - 512 data points in the range 1700 - 1750, and add Gaussian noise (mean=0, variance=1)
    x=np.linspace(1700,1750,512)
    simSpectrum=peakAmp[0]*np.exp(-((x-peak0)/peakWidth)**2)+peakAmp[1]*np.exp(-((x-peak1)/peakWidth)**2)+peakAmp[2]*np.exp(-((x-peak2)/peakWidth)**2)
    noise=np.random.randn(512)*0.07
    noisySpectrum=simSpectrum+noise
     
    fig,ax=plt.subplots(figsize=(10,6))
    ax.scatter(x,noisySpectrum,alpha=0.7)

    ax.set_title('Vibrational Spectrum for u{}'.format(n),fontsize=20)
    ax.set_xlabel('Wavenumber / cm$^{-1}$',fontsize=16)
    ax.set_ylabel('Intensity',fontsize=16)
    plt.show()
    
    #write spectrum to file for download
    f = open(s, "w")
    #write column headers
    f.write("Wavenumber,Intensity\n") 

    #output spectrum data to file
    for i in range(len(x)):
        f.write("{},{}\n".format(x[i], noisySpectrum[i]))

    f.close()
    
def kinetics(n):
    
    np.random.seed(n)
    s=str(n)+"_kineticTraces.csv"
    
    t=np.linspace(0,25,256)
    
    k_F=np.random.uniform(0.5,0.99)
    k_ISC=np.random.uniform(0.1,0.4)
    k_P=np.random.uniform(0.03,0.09)
    
    noiseA=np.random.randn(256)*0.03
    noiseB=np.random.randn(256)*0.03
    noiseC=np.random.randn(256)*0.03
     
    A_conc=np.exp(-(k_F+k_ISC)*t)+noiseA
    B_conc=(k_ISC*(np.exp(-k_P*t)-np.exp(-(k_F+k_ISC)*t)))/(k_F+k_ISC-k_P)+noiseB
    C_conc=(k_F+k_ISC-k_P+(k_P-k_F)*np.exp(-(k_F+k_ISC)*t)-k_ISC*np.exp(-k_P*t))/(k_F+k_ISC-k_P)+noiseC
    
    fig,ax=plt.subplots(figsize=(10,6))
    
    ax.plot(t,A_conc,label='[A]')
    ax.plot(t,B_conc,label='[B]')
    ax.plot(t,C_conc,label='[C]')
    
    ax.set_title('Kinetic Traces for u{}'.format(n),fontsize=20)
    ax.legend(frameon=False,fontsize=16)
    ax.set_xlabel('Time / ns', fontsize=16)
    ax.set_ylabel('Concentration / mol dm$^{-3}$',fontsize=16)
    plt.show()
    
    f = open(s, "w")
    #write column headers
    f.write("Time,[A],[B],[C]\n") 

    #output spectrum data to file
    for i in range(len(t)):
        f.write("{},{},{},{}\n".format(t[i], A_conc[i],B_conc[i],C_conc[i]))

    f.close()


    
