"""
This is a typical way to format a program.
"""

# always do imports first
import numpy as np
import matplotlib.pyplot as plt

# now make some variable
x = np.linspace(0,10,100)
y = x**2

# plotting to the screen

# first get rid of old figures
#plot.close('all')

#initialize a figure object
fig = plt.figure(figsize=(8,8))

# initialize an axis object
ax = fig.add_subplot(111)

# use the 'plot' method of the ax object
ax.plot(x, y, '--g', linewidth=3)

# and make sure it shows up
plt.show()
