# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import random as rd
from functions import *

def train(w_vec,x_vec,t):
	#学習係数
	low = 1

	#不正解データの抽出 ansは、更新したwvecで計算なければならない!!!!
	ans = np.dot(w_vec,x_vec.T) * t

	if ans < 0:
		w_vec = w_vec + 0.5 * x_vec * t

	return w_vec



