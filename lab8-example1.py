#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 14:05:23 2025

@author: raesheng
"""

"""
Rae Sheng
PHYS 1200
Professor Alavi
26 March 2025

LAB 8: Mathematical Modeling Midterm

EXAMPLE 1: HIV Viral Load

Here we explore a model of the viral load -the number of virions in the blood
of a patient infected with HIV- after the administration of an antiretroviral
drug. One model for the viral load predicts that the concentration V(t) of HIV
in the blood at time t after the start of treatment will be.

Equation 1: V(t) = Ae^(+αt) + Be^(−βt)

The four parameters A, α, B, and β are constants that control the behavior of
the model. A and B specify the initial viral load, α is the rate at which new
cells are infected, and β is the rate at which virions are removed from the
blood. In this lab, you will use what you have learned about Python up to this
point to generate plots based on the model, import and plot experimental data,
and then fit model parameters to the data.
"""

# Import the HIV series data as an array, as directed
import numpy as np
data_set = np.loadtxt("HIVseries.csv", delimiter = ",")

"""
1-1 Explore the model:
    
To get started, launch Spyder, import NumPy and PyPlot, and then create an
array “time” for the time intervals between 0 and 10 seconds with 101 numbers.
Next, you will evaluate a compound expression involving this array by using
the solution of the viral load model given in Equation 1.

The first step is to give the constants in the mathematical equation names
you can type, such as alpha and beta instead of α and β. It is wise to give
longer, more descriptive names even to the variables whose names you can type:
for example, time fort and viral load for V (t).

Now, set B = 0, and choose some interesting values for A, α, and β. Then,
evaluate V(t). You should now have two arrays of the same length, time and
viral_load, so plot them. Create a few more plots using different values of
the four model parameters.
"""

# Numpy already imported
import matplotlib.pyplot as plt

# Initialize variables
A = 0.0
alpha = 0.0
B = 0.0
beta = 0.0

# Create array of time containing 0.0 to 10.0, inclusive with 0.1 increment
time = np.arange(0, 10.1, 0.1)

# Viral load equation, copy and paste as needed
# viral_load = A * np.exp(alpha * time) + B * np.exp(-1 * beta * time)

# Set variables and calculate, 1
A = 2
alpha = 1.1
B = 0.0
beta = 1
viral_load_1 = A * np.exp(alpha * time) + B * np.exp(-1 * beta * time)

# Set variables and calculate, 2
A = 3
alpha = 1
B = 3
beta = 0.1
viral_load_2 = A * np.exp(alpha * time) + B * np.exp(-1 * beta * time)

# Set variables and calculate, 3
A = 5
alpha = 0.8
B = 3
beta = 0.4
viral_load_3 = A * np.exp(alpha * time) + B * np.exp(-1 * beta * time)

# Use plots to plot all 4 V(t) graphs on the same graph / set of axes.
plt.plot(time, viral_load_1, color = 'r', label = '1')
plt.plot(time, viral_load_2, color = 'g', label = '2')
plt.plot(time, viral_load_3, color = 'b', label = '3')

# Plot experimental data
plt.plot(data_set, color = 'y')

plt.xlabel("Time elapsed (seconds)")
plt.ylabel("Viral load (virions in blood after drug)")
plt.title("Time elapsed vs. viral load")

plt.legend()
plt.show()
