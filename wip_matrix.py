import math
import pandas as pd
import pylab
import numpy as np
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

#i=0
#j=0
dfRead = pd.read_excel(open('Profil12.xls', 'rb'), sheetname='Tabelle1')
df = dfRead.as_matrix()
GFkt = np.zeros((1000, 1000))
Abstand = np.zeros((1000, 1))

#while (i <= len(df))==True: 
#        #Abstand[i, 0]=float(((df[i+1,1]-(df[i, 1]))))
#        Abstand[i, 0]=((df[i+1,0]-(df[i, 0])))
#        print(Abstand[i, 0])
#        i += 1
#else:

for i in range(len(df)):
    
    for j in range(len(df)):
        GFkt[i, j] = abs((df[i, 0] - df[j, 0]))
        print(GFkt[i,j])
    print(i)
