# --------------------------------------------
# --- Python 2.7.3.
# --- p_ci_normal.py - confidence interval sigma_bar conhecido.
# --- criado em - jorgearacaty 10 aug 2014 - 0214.
# --- jorgearacaty, 15 aug 2014 - 1715.
# --------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from scipy.stats import t
from scipy import stats 

import os
import sys
import csv
import random
import math

import pf_plota

# -----------------------------------------------
# intervalos de confiança - confidence intervals.
# -----------------------------------------------
def confidence_interval():
        
    s_pop = 20
    n =100
    
    # confidence interval, media e
    alpha, mu = 0.05, 60,
    
    # desvio padrao das médias das amostras.
    sigma_bar = s_pop/math.sqrt(n)
    
    print s_pop/math.sqrt(n)

    # valores criticos.
    limite_inferior = norm.ppf(alpha/2, mu, sigma_bar);
    limite_superior = norm.ppf(1-(alpha/2), mu, sigma_bar);
        
    if 1 == 1:

        # eixo horizontal - com 4 vezes pode dar erro to tamanho do eixo.
        xa = np.linspace(mu-(3.99*sigma_bar),limite_inferior)
        xb = np.linspace(limite_inferior,limite_superior)
        xc = np.linspace(limite_superior,mu+(3.99*sigma_bar))

        x = np.concatenate((xa,xb,xc), axis=0)

        #print xa.min(), x.min()

        # eixo vertical.
        ya = norm.pdf(xa,mu,sigma_bar)
        yb = norm.pdf(xb,mu,sigma_bar)
        yc = norm.pdf(xc,mu,sigma_bar)
        
        y = np.concatenate((ya,yb,yc), axis=0)

        if 1 == 1:
            pf_plota.plotar('Confidence Interval','normal','x bar', \
                'probabilidade','pdf',x,y,limite_inferior, \
                limite_superior,sigma_bar,mu,xa,ya,xc,yc,alpha,np.array([]),n)

    if 1 == 1:

        li_st = norm.ppf(alpha/2);
        ls_st = norm.ppf(1-(alpha/2));

        xa = np.linspace(-4,li_st)
        xb = np.linspace(li_st,ls_st)
        xc = np.linspace(ls_st,4)

        x = np.concatenate((xa,xb,xc), axis=0)

        ya = norm.pdf(xa)
        yb = norm.pdf(xb)
        yc = norm.pdf(xc)
        
        y = np.concatenate((ya,yb,yc), axis=0)

        if 1 == 1:
            pf_plota.plotar('Confidence Interval','z scores','x bar', \
                'probabilidade','pdf',x,y,li_st, \
                ls_st,1,0,xa,ya,xc,yc,alpha,np.array([]),n)

# **************************************************
# ***                   MAIN.                    ***
# **************************************************
if __name__ == '__main__':
    # -----------------------------------------
    # Splash
    # -----------------------------------------
    print 'Python running... '
    print sys.argv[0]
    print 'numpy version: ' + np.__version__
    print 'scipy version: ' + scipy.__version__
    print "..."
    
    confidence_interval()
    
    print "\nDONE"
    
    #The_End = raw_input("press any key to go out, thks.\n")

