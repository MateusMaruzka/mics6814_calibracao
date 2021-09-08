# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:12:52 2021

@author: maruzka
"""

import json
import serial
import csv
# import random
# import time
# import threading

# import numpy as np
# import matplotlib.pyplot as plt

# from matplotlib.animation import FuncAnimation
from itertools import count

PORT = "COM3"
baud = 9600

index = count()

def main(fn = "mics_teste.csv"):
    
    connection = serial.Serial(port=PORT, baudrate=baud)
    connection.reset_input_buffer()
    
    
    fieldnames = ['R_CO', 'V_CO', 'R_NH3', "V_NH3", "R_NO2", "V_NO2", "TEMP", "UMID"]
    with open(fn, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


    while True:
        
        data = connection.readline().decode("utf-8")
 
        try:
            
            dict_json = json.loads(data)            
            dict_json.pop("sensor")
            
            with open(fn, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(dict_json)
           
        except json.JSONDecodeError as e:
            print("JSON ERROR:", e)

        else: 
            print("JSON: ", dict_json)
            
            

if __name__ == "__main__":
    main()