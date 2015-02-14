'''
Title: Approximation of pi using Monte Carlo simulation

Randomly scatter points in the square and count how many point fall inside the circle
The value of pi is approximated by comparing the relative area of circle to the square

Will Daewook Kwon - will.dw.kwon@gmail.com

'''

import random
import math
random.seed(201502)

## PROCEDURES
# Generate n points in (0,1)
def unif_point_generator(n):
    i = 0; Data = []
    while i < n:
        Data.append(round(random.uniform(0,1), 2))
        i+=1
    return Data

# Scale points from (0,1) to (-b,b)
def scale_to_coordinate(a, X, b):
    X = [round((x*a + b),2) for x in X]
    return X

# Count how many points fall in the circle of radius r
def in_or_out_circle(X, Y, r):
    i = 0; j = 0; count = 0
    length = len(X)
    Z = []
    while i < length:
        Z.append(math.sqrt(X[i]**2+Y[i]**2))
        i+=1
    while j < length:
        if Z[j] < 1:
            count += 1
        j+=1
    return count, Zra()
####

    
# Generate X and Y coordinates ranging (-1,1)
X = scale_to_coordinate(2, unif_point_generator(1000), -1)
Y = scale_to_coordinate(2, unif_point_generator(1000), -1)
# Count how many number of the points are within the circle of radius r
num, Z = in_or_out_circle(X, Y, 1)
# Get the proportion and solve for pi
Estimated_Pi = ((num*4)/len(Z))

print ("The Monte Carlo Estimation for Pi is: " + repr(Estimated_Pi) )
