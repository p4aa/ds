# import library for code implementation
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
 
# activation function -> sigmoid
 
 
def sigmoid(x):
    return 1/(1+np.exp(-x))
 
 
x_sample = np.linspace(-20, 20, 50)
z_sample = sigmoid(x_sample)
 
# To display graph
plt.plot(x_sample, z_sample)
