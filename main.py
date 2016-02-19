# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import random as rd
from functions import *


data = pd.read_csv("samplefile.csv")
plt.scatter(data.x[data.t==1],data.y[data.t==1],c='m',s=120)
plt.scatter(data.x[data.t==-1],data.y[data.t==-1],c='y',s=120)

#2次元分割　w0 + w1*x + w2*y = f(x,y)
#初期値
w_vec = np.array([1.0,1.0,1.0])
x_vec = np.array([np.ones(len(data.x)),data.x,data.y])



loop = 100

for i in range(loop):
	w_vec = train(w_vec,x_vec,data.t)

print w_vec

#分離境界線
x_fig = np.array(range(0,100))
y_fig = - (w_vec[1]/w_vec[2])*x_fig - (w_vec[0]/w_vec[2])


plt.plot(x_fig,y_fig)

plt.show()
