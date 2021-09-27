import numpy as np
from numpy import *
from scipy import signal
import matplotlib.pyplot as plt
import os
import pandas as pd


def spect(Acc, dt):  # acc is in in/s2, dt is time step
    
    '''
    This program takes the inputs (Time Histories in txt files) to calculate
    the spectra for 5% damping and save them in excel file in specific Directory.  
    Have all the txt file for THs in a  folder
    '''
    
    Tn=0.05
    zeta=0.05
    m=1
    u_1=0
    Ax=[]
    PI=3.14159265359
    for i in range (795+400):
        wn=2*PI/Tn
        u=[0]
        for j in range (len(Acc)):
           if j==0:
               khat=1/(dt**2)+wn*zeta/(dt)
               a=1/(dt**2)- wn*zeta/(dt)
               b=(wn**2)-2/(dt**2)
               phat=(386*Acc[j]-a*u_1-b*u[j])
               u.append(phat/khat)
               
           else:
               phat=386*Acc[j]-a*u[j-1]-b*u[j]
               u.append(phat/khat)
        Tn += 0.01
        an=np.multiply((wn**2), u)
        Ax.append(max(np.absolute(an))/386)        
    return Ax

class loadData(object):
    def __init__ (self, directory, THx, THy, skip_header, factor):
        self.directory=directory
        self.THx=THx
        self.THy=THy
        self.skip_header=skip_header
        self.factor=factor
        self.datax=np.genfromtxt(self.directory+'/' + self.THx, skip_header=self.skip_header)
        self.datay=np.genfromtxt(self.directory+'/' + self.THy, skip_header=self.skip_header)
    def Spectra(self):
        
        Ax=spect(self.datax[:,1], self.datax[2,0]-self.datax[1,0])
        Ay=spect(self.datay[:,1], self.datay[2,0]-self.datay[1,0])
        d=[np.multiply(self.factor, Ax), np.multiply(self.factor,Ay)]
        Srss=np.sqrt(np.sum(np.square(d), axis=0))
        freqs=Srss
        # t=np.linspace(0.05,8,795)
        t=np.linspace(0.05,12,795+400)
        return [d[0],d[1], freqs, t]
        


# directory='D:\\EPS\\PROJECTS\\68_Data Center _ Chile\\THs received from chile\\Original'
directory=input('Directory of THx, THy :')
os.chdir(directory)
EQ=os.listdir(directory)
print(EQ)
NumTh=len(EQ)

SAVE='Yes'
SAVEmean='Yes'

SpecType=input('Which spectra are you plotting? MCE or DBE? =')
skip_header=int(input('How many lines in the text file to skip? (It is usually 5) ='))
factor=float(input('Scaling factor to be applied in TH x and y (Usually 0.75 for MCE and 0.75/1.5 for DBE)='))
SaveDirectory=input('Save to  Directory=')


AllSpect=[]

DBE_df_all=pd.DataFrame()
MCE_df_all=pd.DataFrame()

for i in range (0,NumTh,2):
    os.chdir(SaveDirectory)
    THx=EQ[i]
    THy=EQ[i+1]

    W=loadData(directory, THx, THy, skip_header, factor)
    [Ax, Ay, freqs, t]=W.Spectra()
    AllSpect.append(freqs)

    if SpecType=='DBE':
        #creating DataFrame of DBE
        DBE_df=pd.DataFrame(np.transpose([t,Ax,Ay,freqs]), columns=['time', 'Spectra_Sa(g)_X', 'Spectra_Sa(g)_Y', 'Spectra_SRSS(g)'])
        DBE_df['Earthquake Name']=EQ[i][:-6]
        DBE_df[' ']=' '
        DBE_df_all=pd.concat([DBE_df_all,DBE_df], axis=1)
    elif SpecType=='MCE':  
        #creating DataFrame of MCE
        MCE_df=pd.DataFrame(np.transpose([t,Ax,Ay,freqs]), columns=['time', 'Spectra_Sa(g)_X' , 'Spectra_Sa(g)_Y', 'Spectra_SRSS(g)'])
        MCE_df['Earthquake Name']=EQ[i][:-6]
        MCE_df[' ']=' '
        MCE_df_all=pd.concat([MCE_df_all,MCE_df], axis=1)
        # plt.show()

Mean= np.mean(AllSpect, axis=0)
# Save to excel
if SpecType=='DBE':
    DBE_df_all[' ']= ' '
    DBE_df_all['mean of all spectras']= Mean
    DBE_df_all.to_excel('DBE_spectra.xlsx', index=False)

# Save to excel 
if SpecType=='MCE':
    MCE_df_all[' ']= ' '
    MCE_df_all['mean of all spectras']= Mean
    MCE_df_all.to_excel('MCE_spectra.xlsx', index=False)





