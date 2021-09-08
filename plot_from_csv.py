# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 01:23:52 2021

@author: maruzka
"""


import csv

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time 
# x_vals = []
# y_vals = []

index = count()

fig, ax = plt.subplots(2, 1)


def animate(i, fn):
    
    data = pd.read_csv(fn)
    y1 = np.array(data['R_CO'])
    # y2 = data['V_CO']
    x = np.arange(len(y1))


    ax[0].cla()
    ax[1].cla()
    
    ax[0].plot(x, y1, label='R_CO')
    # ax[1].plot(x, y2, label = "D")
    # mDU = mDU[...,1:-1] - mDU[...,0:-2]
    ax[1].plot(x[2:], (y1[...,1:-1] - y1[...,0:-2]) , label='D2')
    # ax[1].set_ylim([0, 1])

    # plt.legend(loc='upper left')
    ax[0].legend(loc='upper left')
    ax[1].legend(loc='upper right')
    plt.tight_layout()



def main(fn = "mics_calib.csv"):
    
    # ani = animation.FuncAnimation(fig, animate, frames=len(x), fargs=(K,),
                              # interval=100, blit=True)
                              
    ani = FuncAnimation(plt.gcf(), animate, fargs = (fn,), interval=250)
    
    
    plt.tight_layout()
    plt.show()
    time.sleep(0.5)


