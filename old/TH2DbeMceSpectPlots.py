import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


'''
This programe take the analysis results from TH2DbeMce 
file soterd in a folder togeter with DBE and MCE spectras. 
'''

#  Figure limits & properties
xlim = [3, 7]
ylim = [0, 1]
grid_lwidth = 0.15
C = ['DeepPink', 'Cyan', 'b', 'K']


# inputs
THs = int(input('input Number of TH pairs:'))
dir1 = input('Input the directory where the analysis results/MCE/DBE is stored:')


#  Read files in the folder
os.chdir(dir1)
mce = np.genfromtxt(dir1+'\\MCE.txt')
dbe = np.genfromtxt(dir1+'\\DBE.txt') 
df = pd.read_excel(dir1+'\\MCE_spectra.xlsx')


#  loop inside the dataframe and read the necessary info to plot spectra 
for i in range (THs):

    if i == 0:
        t = df['time']
        Ax = df['Spectra_Sa(g)_X']
        Ay = df['Spectra_Sa(g)_Y']
        freqs = df['Spectra_SRSS(g)']
        TH_name = df['Earthquake Name'].loc[0]

    else:
        t = df['time'+'.'+str(i)]
        Ax = df['Spectra_Sa(g)_X'+'.'+str(i)]
        Ay = df['Spectra_Sa(g)_Y'+'.'+str(i)]
        freqs = df['Spectra_SRSS(g)'+'.'+str(i)] 
        TH_name = df['Earthquake Name'+'.'+str(i)].loc[0]
    

    # Define the legends, yiyles of the plots and save them 

    # TH_name_title = TH_name.split('_')[1]  #Activate per TH files name
    TH_name_title = TH_name 

    plt.figure(figsize=(10,5))
    plt.plot(
                t,  Ax,  C[0],
                t,  Ay,  C[1],
                t, freqs, C[2],
                mce[:,0], mce[:,1], C[3]
                )
    plt.ylabel('Sa (g)')

    plt.xlabel('Period(sec)')

    plt.title(
        'Acceleration Response Spectra: ' + TH_name_title  +', MCE , \u03B6=0.05 ', 
        fontweight='bold'
        )

    plt.grid(linewidth=grid_lwidth)
    plt.legend(
        [
            TH_name_title +' E',
            TH_name_title +' N',
            'SRSS',
             'MCE Spectrum'
        ]
             )

    plt.xlim(xlim)
    plt.ylim(ylim)

    # save images
    saveName='M-' + TH_name

    plt.savefig(
        saveName +'.png',
         dpi=300, 
         bbox_inches='tight'
         )
    # plt.close() 


# Plot the Mean MCE: 
Mean = df['mean of all spectras']

plt.figure(figsize=(10,5))
plt.plot(
    t, Mean, C[2],
    mce[:,0], mce[:,1], C[3]
        )
plt.ylabel('Sa (g)')
plt.xlabel('Period(sec)')
plt.title(
           'MCE Average Scaled Acceleration Response Spectra \u03B6=0.05 ',
           fontweight='bold')
plt.grid(linewidth=grid_lwidth)
plt.legend(['Mean SRSS Spectra', 'MCE Spectrum'])
plt.xlim(xlim)
plt.ylim(ylim)
# plt.annotate("", xy=(3.56, 0.5), xytext=(6.38, 0.5), arrowprops=dict(arrowstyle="<->"), color='r')
# plt.annotate('$ ASCE7-16: 0.75T_M (UB) - 1.25T_M (LB) $', xy=(3.7, 0.6), color='r')
# plt.plot([3.56,3.56],[0,0.5],'r--' , [6.38,6.38], [0,0.5], 'r--')
saveName = 'mean_MCE'

plt.savefig(
    saveName +'.png', 
    dpi=300, 
    bbox_inches='tight')
plt.close()    



# DBE spectra graphing  
df=pd.read_excel(dir1+'\\DBE_spectra.xlsx')
for i in range (THs):

    if i == 0:
        t = df['time']
        Ax = df['Spectra_Sa(g)_X']
        Ay = df['Spectra_Sa(g)_Y']
        freqs = df['Spectra_SRSS(g)']
        TH_name = df['Earthquake Name'].loc[2]

    else:
        t = df['time'+'.'+str(i)]
        Ax = df['Spectra_Sa(g)_X'+'.'+str(i)]
        Ay = df['Spectra_Sa(g)_Y'+'.'+str(i)]
        freqs = df['Spectra_SRSS(g)'+'.'+str(i)] 
        TH_name = df['Earthquake Name'+'.'+str(i)].loc[2]
    
    # TH_name_title = TH_name.split('_')[1]
    TH_name_title = TH_name

    plt.figure(figsize=(10,5))
    plt.plot(
             t, Ax, C[0], 
             t, Ay, C[1],
             t, freqs, C[2],
             dbe[:,0], dbe[:,1], C[3]
             )
    plt.ylabel('Sa (g)')
    plt.xlabel('Period(sec)')
    plt.title(
        'Acceleration Response Spectra: ' +  TH_name_title  + ', DBE, \u03B6=0.05 ',
         fontweight='bold')

    plt.grid(linewidth=grid_lwidth)
    plt.legend([
        TH_name_title +' E',
        TH_name_title +' N',
        'SRSS', 
        'DBE Spectrum'
        ])
    plt.xlim(xlim)
    plt.ylim(ylim)
    # save images
    saveName = 'D-'+TH_name
    plt.savefig(
        saveName +'.png', 
        dpi=300, 
        bbox_inches='tight'
        )
    # plt.close() 
    # plt.show()

# Plot the Mean DBE: 
Mean = df['mean of all spectras']
plt.figure(figsize=(10,5))
plt.plot(
    t, Mean, C[2],
    dbe[:,0], dbe[:,1], C[3]
    )
plt.ylabel('Sa (g)')
plt.xlabel('Period(sec)')
plt.title(
    'DBE Average Scaled Acceleration Response Spectra \u03B6=0.05 ',
    fontweight='bold'
    )
plt.grid(linewidth=grid_lwidth)
plt.legend([
    'Mean SRSS Spectra', 
    'DBE Spectrum'
    ])
plt.xlim(xlim)
plt.ylim(ylim)
# plt.annotate("", xy=(3.56, 0.5), xytext=(6.38, 0.5), arrowprops=dict(arrowstyle="<->"), color='r')
# plt.annotate('$ ASCE7-16: 0.75T_M (UB) - 1.25T_M (LB) $', xy=(3.7, 0.6), color='r')
# plt.plot([3.56,3.56], [0,0.5],'r--' , [6.38,6.38], [0,0.5],'r--')
saveName = 'mean_DBE'
plt.savefig(
    saveName +'.png', 
    dpi=300,
    bbox_inches='tight'
    )
plt.close()   

