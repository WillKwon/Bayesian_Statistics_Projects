'''
Title: Generating Gaussian Random Numbers using the Rejection Method 

First, exponential rv's were generated using inverse CDF method,
and Gaussian rv's are selected among those exponential rv's under 
acceptance-rejection criterion

Will Daewook Kwon - will.dw.kwon@gmail.com
'''

import random
import math
import numpy as np
random.seed(1231)

## PROCEDURES
# A procedure to generate exponential random numbers
def Exponential_RV(n, lamb):
    result = []; i = 0
    while i < n:
        inversecdf = (-1/lamb) * math.log(random.uniform(0, 1))
        result.append(inversecdf)
        i+=1
    return result

# A procedure to generate normal random numbers
def Gaussian_RV(n, mu, sigma):
    result =[]; i = 0
    while i < n:
        while True:
            x1 = Exponential_RV(1, 1)
            x2 = Exponential_RV(1, 1)
            X1 = x1[0]; X2 = x2[0]
            
            '''
            This criterion needs further description
            '''
            if X2 >= ((X1 - 1)**2) / 2:
                break

        # Since exponential rv's are all positive, assign minus with prob 0.5
        U = random.uniform(0, 1)
        if U <= 0.5:
            Z = X1
        else:
            Z = -1 * X1
        
        result.append(sigma * Z + mu)
        i+=1
    return (result)
####


res = Exponential_RV(1000, 1)
print ('Mean: '+ repr(np.mean(res)))
print ('Standard Deviation: '+ repr(np.std(res)))

num = Gaussian_RV(1000, 0, 1)
print ('Mean: '+ repr(np.mean(num)))
print ('Standard Deviation: '+ repr(np.std(num)))

