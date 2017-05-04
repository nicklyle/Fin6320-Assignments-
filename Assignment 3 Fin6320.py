import numpy as np
from scipy.stats import binom

class VanillaOption(object):
    def __init__(self, strike, expiry, payoff):
        self.__strike = strike
        self.__expiry = expiry
        self.__payoff = payoff
        
    @property
    def strike(self):
        return self.__strike
    
    @property
    def expiry(self):
        return self.__expiry
    
    def payoff(self, spot):
        return self.__payoff(self, spot)
        
def callpayoff(option, spot):
    return np.maximum(spot - strike, 0.0)

def putpayoff(option, spot):
    return np.maximum(strike - spot, 0.0)
    
def AmericanBinomial(option, spot, rate, volatility, dividend, steps):
    return np.maximum()

## Problem 1
    

def EuropeanBinomialPricer(spot, strike, rate, vol, div, steps, expiry, payoff):
    h = expiry / steps
    nodes = steps + 1
    u = np.exp((rate - div) * h + vol * np.sqrt(h))
    d = np.exp((rate - div) * h - vol * np.sqrt(h))
    pstar = (np.exp((rate - div) * h) - d) / (u - d)
    disc = np.exp(-(rate - div))
    putT = 0.0
    
    for i in range(nodes):
        spotT = spot * (u ** (steps - i)) * (d ** i)
        putT += payoff(spotT, strike) * binom.pmf(steps - i, steps, pstar)
        
    putPrc = putT * disc
    return putPrc

spot = 41
strike = 40
vol = 0.3
rate = 0.08
div = 0.0
expiry = 1
steps = 3
nodes = steps + 1
M = 50000

result = EuropeanBinomialPricer(spot, strike, rate, vol, div, steps, expiry, putpayoff)
print("The Option Price for problem 1 is {0:.4f}".format(result))

## Problem 2

dt = expiry / steps
u = np.exp((rate * dt) + vol * np.sqrt(dt))
d = np.exp((rate * dt) - vol * np.sqrt(dt))
pu = (np.exp(rate * dt) - d) / (u - d)
pd = 1 - pu
disc = np.exp(-rate * dt)
dpu = disc * pu
dpd = disc * pd
    
cashFlow_t = np.zeros((nodes, ))
spot_t = np.zeros((nodes, ))
option = VanillaOption(strike, expiry, callpayoff)
    
for i in range(nodes):
    spot_t[i] = spot * (u ** (steps - i)) * (d ** i)
    cashFlow_t[i] = option.payoff(spot_t[i]) 

for i in range((steps - 1), -1, -1):
    for j in range(i+1):
        cashFlow_t[j] = dpu * cashFlow_t[j] + dpd * cashFlow_t[j+1]
        spot_t[j] = spot_t[j] / u
        cashFlow_t[j] = np.maximum(cashFlow_t[j], option.payoff(spot_t[j]))    
    
price = cashFlow_t[0]
    
print ("The Option Price for problem 2 is: {0:.4f}".format(price))

## Problem 3

spotT = np.empty((M, ))
callT = np.empty((M, ))

for i in range(M):
    z = np.random.normal(size=1)
    spotT[i] = spot * np.exp((rate - 0.5 * vol * vol)* expiry + vol * np.sqrt(expiry) * z)
    callT[i] = np.maximum(spotT[i] - strike, 0.0)

se = callT.std(ddof = 1) / np.sqrt(M)
price = np.exp(-rate * expiry) * callT.mean()
print("The Call Price for problem 3 is: {0:.3f}".format(price))
print("The Standard Error for problem 3 is: {0:.5}".format(se))