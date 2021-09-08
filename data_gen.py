# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 19:09:48 2021

@author: maruzka
"""


import csv
import random
import time

import numpy as np


# -*- coding: utf-8 -*-
"""
Exemplo de simulaÃ§Ã£o discreta de uma funÃ§Ã£o de transferÃªncia

Processo de primeira ordem - temperatura ("secador de cabelo")

Y(s)/U(s) = 25/(s + 1)

@author: Prof. Daniel Cavalcanti Jeronymo
"""

import scipy.signal
import numpy as np
import math
from itertools import count
import matplotlib.pyplot as plt

# y  = K*(1 − exp(−t tau))
# y = 1/tau*exp(-t tau)
def df(x, k = 1, tau = 10):
    return np.exp(-x/tau) / tau

def first_order_response(x, k = 1, tau = 10):
    return k*(1 - np.exp(-x/tau))

             
def first_order_response_generator(iter_max):
  # Inicialização dos elementos
  # Resposta a uma entrada degrau de um sistema de primeira ordem
  # K / ts + 1
  
  i = count()
  x = next(i)
  k = 1
  tau = 10
  while x < iter_max:
      
      yield k*(1 - np.exp(-x/tau))
      
      x = next(i)
      

def main(fn = 'mics_calib.csv'):

    
    n = 250
    x = np.arange(n)
    
    np.random.seed(0)
    #For random samples from N(u, s^2), use:
    sigma = 0.001
    mu = 0
    noise = sigma * np.random.randn(n) + mu
    
    # fig, ax = plt.subplots()
    # ax.plot(x, first_order_response(x, tau = 100) + noise)
    
    
    r_co = first_order_response(x, tau = 100) + noise
    v_co = df(x, tau = 100)
    r_nh3 = first_order_response(x, tau = 150) + noise
    r_no2 = first_order_response(x, tau = 75) + noise


    fieldnames = ['R_CO', 'V_CO', 'R_NH3', "V_NH3", "R_NO2", "V_NO2", "TEMP", "UMID"]

    with open(fn, 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    for i in range(n):

        with open(fn, 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
            info = {
                "R_CO": r_co[i],
                "V_CO": v_co[i],
                "R_NH3": r_nh3[i],
                "V_NH3": 0,
                "R_NO2": r_no2[i],
                "V_NO2": 0,
                "TEMP" : 0,
                "UMID" : 0
            }
    
            csv_writer.writerow(info)

        time.sleep(0.5)
  
if __name__ == "__main__":
    main()
    
    



