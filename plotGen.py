#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 11:15:10 2018

@author: Dan
"""
import numpy as np
import matplotlib.pyplot as plt


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
    
    plt.figure(figsize=(10,6))
    
    plt.scatter(x,noisySpectrum,s=40, c='#4c3f54',alpha=0.7)
    plt.xlabel('Wavenumber / cm$^{-1}$',fontsize=18)
    plt.ylabel('Intensity / a.u.',fontsize=18)
    
    plt.title('Vibrational Spectrum for u{}'.format(n),fontsize=24)
    plt.tick_params(labelsize=14)
    plt.grid(linestyle='dotted',c='0.7')
    
    plt.show()
    
    #write spectrum to file for download
    f = open(s, "w")
    #write column headers
    f.write("Wavenumber/cm^-1,Intensity\n") 

    #output spectrum data to file
    for i in range(len(x)):
        f.write("{},{}\n".format(x[i], noisySpectrum[i]))

    f.close()
    
def kinetics(n):
    
    np.random.seed(n)
    s=str(n)+"_kineticTraces.csv"
    
    t=np.linspace(0,10,256)
    
    k_isom=np.random.uniform(0.5, 0.8)
    k_IC=np.random.uniform(0.2,0.5)
    k_diss=np.random.uniform(0.2,0.8)

    
    noiseA=np.random.randn(256)*0.03
    noiseB=np.random.randn(256)*0.03
    noiseC=np.random.randn(256)*0.03
    noiseP=np.random.randn(256)*0.03
     
    A_conc=np.exp(-(k_isom + k_IC)*t)+noiseA
    B_conc=((np.exp(-(k_IC+k_isom)*t)-np.exp(-k_diss*t))*k_isom)/(k_diss-k_IC-k_isom)+noiseB
    C_conc=(k_IC*(1-np.exp(-(k_IC+k_isom)*t)))/(k_IC+k_isom)+noiseC
    P_conc=(k_isom*(k_IC+k_isom-k_diss+k_diss*np.exp(-(k_IC+k_isom)*t)-(k_IC+k_isom)*np.exp(-k_diss*t)))/((k_IC+k_isom-k_diss)*(k_IC+k_isom))+noiseP
    plt.figure(figsize=(10,6))

             
    plt.plot(t,A_conc,lw=2,c='#4c3f54',label='[A]')
    plt.plot(t,B_conc,lw=2,c='#d13525',label='[B]')
    plt.plot(t,C_conc,lw=2,c='#f2c057',label='[C]')
    plt.plot(t,P_conc,lw=2,c='#486824',label='[P]')

             
    #add axis labels and a plot legend, and make the font larger
    plt.xlabel('Time / ps',fontsize=18) 
    plt.ylabel('Concentration / a.u.',fontsize=18)
    plt.tick_params(labelsize=14)
    plt.legend(frameon=False,fontsize=16)
    plt.grid(linestyle='dotted',c='0.7')

    plt.title('Kinetic traces for u{}'.format(n),fontsize=24)
    plt.show()             
                
    
    f = open(s, "w")
    #write column headers
    f.write("Time / ps,[A],[B],[C],[P]\n") 

    #output spectrum data to file
    for i in range(len(t)):
        f.write("{},{},{},{},{}\n".format(t[i], A_conc[i],B_conc[i],C_conc[i],P_conc[i]))

    f.close()


    
