import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
This programe take the analysis results from analyzeAll_SSE.py 
file soterd in a folder togeter with OBE and SSE spectras. 
'''
xlim=[0, 7]
ylim=[0, 2]
grid_lwidth=0.15
C=['DeepPink', 'Cyan', 'b', 'black']
THs=int(input('input Number of TH pairs:'))
# dir1='D:\\EPS\PROJECTS\\57-Ferraro Duzce Project\\TH_received_2_25_2021\\graph'
dir1=input('Input the directory where the analysis results/SSE/OBE is stored:')
os.chdir(dir1)
mce=np.genfromtxt(dir1+'\\SSE.txt')
dbe=np.genfromtxt(dir1+'\\OBE.txt')

# MCE spectra graphing  
df=pd.read_excel(dir1+'\\SSE_spectra.xlsx')


for i in range (THs):
    if i==0:
        t=df['time']
        Ax=df['Spectra_Sa(g)_X']
        Ay=df['Spectra_Sa(g)_Y']
        freqs=df['Spectra_SRSS(g)']
        TH_name=df['Earthquake Name'].loc[0].split('_')[0]

    else:
        t=df['time'+'.'+str(i)]
        Ax=df['Spectra_Sa(g)_X'+'.'+str(i)]
        Ay=df['Spectra_Sa(g)_Y'+'.'+str(i)]
        freqs=df['Spectra_SRSS(g)'+'.'+str(i)] 
        TH_name=df['Earthquake Name'+'.'+str(i)].loc[0].split('_')[0]
    
    TH_name_title=TH_name
    plt.figure(figsize=(10,5))
    plt.plot(t, Ax,C[0], t,Ay,C[1],t,freqs,C[2], mce[:,0], mce[:,1], C[3])
    plt.ylabel('Sa (g)')
    plt.xlabel('Period(sec)')
    plt.title('Acceleration Response Spectra: ' + TH_name_title+', SSE , \u03B6=0.05 ',fontweight='bold')
    plt.grid(linewidth=grid_lwidth)
    plt.legend([TH_name_title +' E',TH_name_title +' N','SRSS', 'SSE Spectra'])
    plt.xlim(xlim)
    plt.ylim(ylim)
    # save images
    saveName='S-'+TH_name
    plt.savefig(saveName +'.png', dpi=300)
    plt.close() 

# Plot the Mean MCE: 
Mean=df['mean of all spectras']
plt.figure(figsize=(10,5))
plt.plot(t,Mean,C[2],mce[:,0], mce[:,1], C[3])
plt.ylabel('Sa (g)')
plt.xlabel('Period(sec)')
plt.title('SSE Average Scaled Acceleration Response Spectra \u03B6=0.05 ',fontweight='bold')
plt.grid(linewidth=grid_lwidth)
plt.legend(['Mean SRSS Spectra', 'SSE Spectrum'])
plt.xlim(xlim)
plt.ylim(ylim)
saveName='mean_SSE'
plt.savefig(saveName +'.png', dpi=300)
plt.close()    



# DBE spectra graphing  
df=pd.read_excel(dir1+'\\OBE_spectra.xlsx')
for i in range (THs):
    if i==0:
        t=df['time']
        Ax=df['Spectra_Sa(g)_X']
        Ay=df['Spectra_Sa(g)_Y']
        freqs=df['Spectra_SRSS(g)']
        TH_name=df['Earthquake Name'].loc[0].split('_')[0]
    else:
        t=df['time'+'.'+str(i)]
        Ax=df['Spectra_Sa(g)_X'+'.'+str(i)]
        Ay=df['Spectra_Sa(g)_Y'+'.'+str(i)]
        freqs=df['Spectra_SRSS(g)'+'.'+str(i)] 
        TH_name=df['Earthquake Name'+'.'+str(i)].loc[0].split('_')[0]
    
    TH_name_title=TH_name
    plt.figure(figsize=(10,5))
    plt.plot(t, Ax,C[0], t,Ay,C[1],t,freqs,C[2], dbe[:,0], dbe[:,1], C[3])
    # plt.plot(t, Ax, t,Ay,t,freqs,'b', dbe[:,0],dbe[:,1], 'K')
    plt.ylabel('Sa (g)')
    plt.xlabel('Period(sec)')
    plt.title('Acceleration Response Spectra: ' +  TH_name_title +', OBE, \u03B6=0.05 ', fontweight='bold')
    plt.grid(linewidth=grid_lwidth)
    plt.legend([TH_name_title +' E',TH_name_title +' N','SRSS', 'OBE Spectra'])
    plt.xlim(xlim)
    plt.ylim(ylim)
    # save images
    saveName='O-'+TH_name
    plt.savefig(saveName +'.png', dpi=300)
    plt.close() 

# Plot the Mean DBE: 
Mean=df['mean of all spectras']
plt.figure(figsize=(10,5))
plt.plot(t,Mean,C[2],dbe[:,0], dbe[:,1], C[3])
plt.ylabel('Sa (g)')
plt.xlabel('Period(sec)')
plt.title('OBE Average Scaled Acceleration Response Spectra \u03B6=0.05 ',fontweight='bold')
plt.grid(linewidth=grid_lwidth)
plt.legend(['Mean SRSS Spectra', 'OBE Spectrum'])
plt.xlim(xlim)
plt.ylim(ylim)
saveName='mean_OBE'
plt.savefig(saveName +'.png', dpi=300)
plt.close()     