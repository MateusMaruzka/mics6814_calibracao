# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 18:05:35 2021

@author: maruzka
"""


from multiprocessing import Process

from plot_from_csv import main as pfc
from data_gen import main as main_datagen
from mics6814_serial import main as serial_mics6814

from datetime import date
from pathlib import Path

import glob
import time



def main():
    
    
    # fn = "mics_teste.csv"
    
    hoje = date.today()
    path_hoje = "dados/" + str(hoje)
    
    (Path('.')/ path_hoje ).mkdir(exist_ok = True)
    
    
    
    n_arq = len(glob.glob(path_hoje + "/*.csv"))
    print(n_arq)
    
    fn =  path_hoje + '/' + str(n_arq) + ".csv"
    print(fn)
    
    
    f = open(fn, "w")
    f.close()
    
    datagen = Process(target=serial_mics6814, args = (fn, ))
    datagen.start()   

    plot = Process(target=pfc, args = (fn, ))
    plot.start()   
    
    # plot.join()

if __name__ == "__main__":
    main()

    # datagen.join()

# import pandas as pd
# import numpy as np
# import time
# from multiprocessing import Process, Queue

# def f(q):
#     data = pd.read_csv('mics_calib.csv')
#     y1 = np.array(data['R_CO'])
#     # y2 = data['V_CO']
#     x = np.arange(len(y1))
#     q.put([len(y1), x[-1]])

# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(q.get())    # prints "[42, None, 'hello']"
#     p.join()
#     time.sleep(0.5)
    

