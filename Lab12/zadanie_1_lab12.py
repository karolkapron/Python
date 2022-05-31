import numpy as np

inputs = np.array([0.33, 1.44, -1])

def network(X):


    w1 = np.array([[1.06, 0.27, 1.27]
                  ,[0.05, -0.37, 1.1]
                  ,[0.63, 1.42, 0.48]])
    answ = np.dot(w1, X.T)
    output = np.array([0.84, -0.47, 0.98])


    return np.dot(output, answ.T)

print(network(inputs))