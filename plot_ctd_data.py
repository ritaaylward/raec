"""
Code to plot data from the Canadian CTD text file.

Goal is the make a plot of temperature vs. depth and save it as a png
in the output directory.
"""

# imports
import sys, os
sys.path.append(os.path.abspath('shared'))
import my_module as mymod

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

myplace = 'raec' # *** YOU NEED TO EDIT THIS ***

# input directory
in_dir = '../' + myplace + '_data/'

# make sure the output directory exists
out_dir = '../' + myplace + '_output/'
mymod.make_dir(out_dir)

# define the input filename
in_fn = in_dir + '2017-01-0118.ctd'
# this is some Canadian CTD data, formatted in a strict but
# difficult-to-use way

# define the output filenames
out_fn_1 = out_dir + 'out_test_1.png'
out_fn_2 = out_dir + 'out_test_2.png'

'--------------------------------------------------'
# version 1: do it by hand

# go through the input file one line at a time, and start accumulating data
# when we are done with the header

f = open(in_fn, 'r', errors='ignore')
# typical real-world issue: the read operation throws an error
# around line 383 for unknown reasons - we ignore it.
get_data = False # like a light switch. starts in off position
# initialize empty data holder arrays.
depth_arr = np.empty(0)
temp_arr = np.empty(0)
for line in f:
    if '*END OF HEADER' in line:
        get_data = True # toggel the switch to 'on' once you reach END OF HEADER
    elif get_data == True: # the switch is now on, so it'll do the stuff in elif
        line_list = line.split() # split items on line into strings
        # and save selected items as floating point numbers in our lists
        depth_arr = np.append(depth_arr, float(line_list[1]))
        temp_arr = np.append(temp_arr, float(line_list[2]))

f.close()

# "Z" is minus the depth

# plotting
plt.close('all')
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)
ax.plot(temp_arr, -depth_arr, 'ob')
ax.grid(True)
ax.set_xlabel('Temperature [deg C]')
ax.set_ylabel('Z [m]')
ax.set_title(in_fn + ': From Scratch')
plt.show()
plt.savefig(out_fn_1)
