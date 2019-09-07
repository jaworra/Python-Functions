import numpy as np

#Define input
X = np.array([[0,0,1],
             [0,1,1],
             [1,0,1],
             [1,1,1]])

#Define expected output
Y = np.array([[0],
             [1],
             [1],
             [0]])

np.random.seed(1)

#Weights initailsed with mean 0
weights0 = 2*np.random.random((3,4))-1
weights1 = 2*np.random.random((4,1))-1

print(weights0)
print(weights1)

#sigmoid - activation function
def nonlin(x, deriv=False):
    if(deriv==True):
        return x*(1-x)

    return 1/(1+np.exp(-x))

#train the network
for j in range(60000):

    #Feed forward through layer 0,1 and 2
    layer0 = X
    layer1 = nonlin(np.dot(layer0,weights0))
    layer2 = nonlin(np.dot(layer1, weights1))

    #compare to expected result - calculate error term
    layer2_error = Y - layer2

    #seek optimal error or Gradient Descent, minimal error
    #backpropation. Using partial dervivatives(chainrule) - a feedfoward network is a composite function
    #updates the weights backpropagation recursively
    if (j% 10000) == 0:
        print("Error:" + str(np.mean(np.abs(layer2_error))))

#-------starts here -------
    #chain rule
    layer2_delta = layer2_error*nonlin(layer2,deriv=True)
    layer1_error = layer2_delta.dot(weights1.T)
    layer1_delta = layer1_error * nonlin(layer1, deriv=True)

    #Using deltas, update the weights to reduce error rate with interation
    #Gradient descent algorithm
    weights1 += layer1.T.dot(layer2_delta) *.1 #learning rate set to .1 here
    weights0 += layer0.T.dot(layer2_delta) *.1


#0utput shows increased accuracy in iteration.