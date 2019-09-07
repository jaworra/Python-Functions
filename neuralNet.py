import math
import numpy as np

class Network(object):
    def __init__(self, *args, **kwargs):
    #...yada yada, initialise weiths and biases

    #activiation
    def sigmoid(self,x):
        return 1 /(1+(math.e**-x)) #can add a biases here i.e +10


    def feedfoward(self,a):
        """Return the output of the network for an input vector a"""
        for b,w, in zip(self.biases, self.weights):
            a = self.sigmoid(np.dot(w, a) + b) # neuron
            return a


