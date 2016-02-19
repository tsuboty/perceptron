# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import random as rd


data = pd.read_csv("samplefile.csv")
# print data

# plt.scatter(data.x[data.t==1],data.y[data.t==1],c='m',s=120)

# plt.scatter(data.x[data.t==-1],data.y[data.t==-1],c='y',s=120)
# # plt.show()





def train(wvec, xvec, label):
    #学習係数
    low = 0.5
    print np.dot(wvec,xvec) * label
    if (np.dot(wvec,xvec) * label < 0): #不正解
        print wvec
        wvec_new = wvec + label*low*xvec
        print "add"
        print label*low*xvec

        return wvec_new
    else:
        return wvec




if __name__ == '__main__':

    train_num = 100#学習データ数

    #class1の学習データ
    x1_1=np.random.rand(train_num/2) * 5 + 1 #x成分
    x1_2=np.random.rand(int(train_num/2)) * 5 + 1 #y成分
    label_x1 = np.ones(train_num/2) #ラベル（すべて1）

    #class2の学習データ
    x2_1=(np.random.rand(train_num/2) * 5 + 1) * -1 #x成分
    x2_2=(np.random.rand(train_num/2) * 5 + 1) * -1 #y成分
    label_x2 = np.ones(train_num/2) * -1 #ラベル（すべて-1）

    x0=np.ones(train_num/2) # x0は常に1
    x1=np.c_[x0, x1_1, x1_2] #np.c_は横に連結していく。
    x2=np.c_[x0, x2_1, x2_2]

    xvecs=np.r_[x1, x2] #np.r_は縦に連結していく。
    # print xvecs
    labels = np.r_[label_x1, label_x2]

    wvec = np.array([3,1,-2])#初期の重みベクトル 適当に決める

    loop = 100
    for j in range(loop):
        for xvec, label in zip(xvecs, labels):
            wvec = train(wvec, xvec, label)
            # print wvec

    # print wvec

    plt.scatter(x1[:,1], x1[:,2], c='red', marker="o")
    plt.scatter(x2[:,1], x2[:,2], c='yellow', marker="o")
    #分離境界線
    x_fig = np.array(range(-8,8))
    y_fig = -(wvec[1]/wvec[2])*x_fig - (wvec[0]/wvec[2])

    plt.plot(x_fig,y_fig)
    plt.show()












