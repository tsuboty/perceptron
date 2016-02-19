# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import random as rd
from functions import *


def train(w_vec,x_vec,t):
	#学習係数
	low = 0.5

	#不正解データの抽出
	print "w"
	print w_vec
	print "x"
	print x_vec
	ans = np.dot(w_vec,x_vec) * t
	print "----ans"
	print ans

	for i in range(len(ans)):

		if ans[i] < 0:
			w_vec = w_vec + low * x_vec[:,i] * t[i]
			print t[i]
			print "old"
			print w_vec
			print "add"
			print  low * x_vec[:,i] * t[i]
			print "wnew"
			print w_vec
			print "---- i "
			print i
			return w_vec
		else:
			continue


