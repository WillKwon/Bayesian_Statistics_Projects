'''
Title: Metropolis-Hastings Algorithm for generating Standard Gaussian RV's

The following code simulates Standard Normal RV's using the 
method of Metropolis-Hastings Algorithm
The Gaussian distribution with sd = 3 was used as the proposal distribution

Will Daewook Kwon - will.dw.kwon@gmail.com
'''
import math as m
import numpy as np
import random
import scipy
import scipy.stats as stat 
random.seed(150214)


# PROCEDURE
def MCMC_Gaussian(n, initial):
    current = initial
    MarkovChain = []; i = 0
    # initial 2000 will be discarded as burn-in
    length = n + 2000
    
    while i < length:
        # Proposal is gaussian with sd = 3
        next = random.gauss(current, 3)
        
        # Caculating Acceptance
        U = random.uniform(0, 1)
        accept = (stat.norm.pdf(next)*stat.norm.pdf(next, current, 1)) / (stat.norm.pdf(current)*stat.norm.pdf(current, next, 1))
        if U <= accept:
            current = next
        else:
            current = current
        
        # Collect
        MarkovChain.append(current)
        i+=1
        
    # Discard the Burn-in
    return MarkovChain[2000:length+1] 
####

SimulatedGaussian = MCMC_Gaussian(10000, 0)
print(len(SimulatedGaussian))
print(np.mean(SimulatedGaussian))
print(np.sd(SimulatedGaussian))
        