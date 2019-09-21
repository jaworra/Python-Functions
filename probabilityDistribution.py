import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns


#Poisson Distribution
# n = number of events, lambd = expected number of events
# which can take place in a period
for lambd in range(2, 8, 2):
    n = np.arange(0, 10)
    poisson = stats.poisson.pmf(n, lambd)
    plt.plot(n, poisson, '-o', label="λ = {:f}".format(lambd))
    plt.xlabel('Number of Events', fontsize=12)
    plt.ylabel('Probability', fontsize=12)
    plt.title("Poisson Distribution varying λ")
    plt.legend()
plt.show()



'''
#Bernoulli Distribution
probs = np.array([0.75, 0.25])
face = [0, 1]
plt.bar(face, probs)
plt.title('Loaded coin Bernoulli Distribution', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.xlabel('Loaded coin Outcome', fontsize=12)
axes = plt.gca()
axes.set_ylim([0,1])
plt.show()



#Exponential Distribution
for lambd in range(1,10, 3):
    x = np.arange(0, 15, 0.1)
    y = 0.1*lambd*np.exp(-0.1*lambd*x)
    plt.plot(x,y, label="λ = {:f}".format(0.1*lambd))
    plt.xlabel('Random Variable', fontsize=12)
    plt.ylabel('Probability', fontsize=12)
    plt.title("Exponential Distribution varying λ")
    plt.legend()
plt.show()  

#Uniform Distribution
probs = np.full((6), 1/6)
face = [1,2,3,4,5,6]
plt.bar(face, probs)
plt.ylabel('Probability', fontsize=12)
plt.xlabel('Dice Roll Outcome', fontsize=12)
plt.title('Fair Dice Uniform Distribution', fontsize=12)
axes = plt.gca()
axes.set_ylim([0,1])
plt.show()

#Binomial Distribution
# pmf(random_variable, number_of_trials, probability)
for prob in range(3, 10, 3):
    x = np.arange(0, 25)
    binom = stats.binom.pmf(x, 20, 0.1*prob)
    plt.plot(x, binom, '-o', label="p = {:f}".format(0.1*prob))
    plt.xlabel('Random Variable', fontsize=12)
    plt.ylabel('Probability', fontsize=12)
    plt.title("Binomial Distribution varying p")
    plt.legend()
plt.show()

#Normal Distribution
n = np.arange(-50, 50)
mean = 0
normal = stats.norm.pdf(n, mean, 10)
plt.plot(n, normal)
plt.xlabel('Distribution', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.title("Normal Distribution")
plt.show()
'''