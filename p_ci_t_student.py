# --------------------------------------------
# --- Python 2.7.3.
# --- p_ci_t_student.py - fit dezena 2 da quina para Rayleigh().
# --- criado em - jorgearacaty 10 aug 2014 - 2300.
# --- jorgearacaty, 11 aug 2014 - 1345.
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

    # --------------------------------------
    # 95% confidence interval - t Student.    
    # sigma unknown - Anderson 2008 pag 310.
    # http://adventuresinpython.blogspot.com.br/2012/12/confidence-intervals-in-python.html

    # Levine pag 292, exercício 8.14.
    s = np.array([1, 2, 3, 4, 5, 6, 20])

    # extrai parametros do vetor.
    n, min_max, mean, var, skew, kurt = stats.describe(s)
    print '\ndiferente, var extraida por stats.describe(s) e np.var(s)'
    print 'denominador (n-1) = ', str(var), ', denominador (n) = ', str(np.var(s)), '\n'

    # set parametros.
    s_amostra = math.sqrt(var)
    n_amostra = n
    mu_amostra = mean
    alpha = 0.05

    # calcula os t scores para os pontos críticos,
    # percent point function (ppf), dada uma cdf calcula o ppf,
    # ou seja, o valor x do ponto na Student curve
    # (n_amostra - 1) é o grau de liberdade.
    # norm.ppt equivale a norminv e norm.pdf a normpdf.
    tinf = t.ppf(alpha/2,n_amostra-1)
    tsup = t.ppf(1-(alpha/2),n_amostra-1)

    
    xis_inf = mu_amostra + (tinf * (s_amostra / math.sqrt(n_amostra)))
    xis_sup = mu_amostra + (tsup * (s_amostra / math.sqrt(n_amostra)))

    print xis_inf, xis_sup

    # ---------------------------------------------
    # desenha curva baseada na distribuição normal.
    # ---------------------------------------------
    mu = mu_amostra
    sigma = s_amostra
    limite_inferior = xis_inf
    limite_superior = xis_sup

    xa = np.linspace(mu-(4*sigma),limite_inferior)
    xb = np.linspace(limite_inferior,limite_superior)
    xc = np.linspace(limite_superior,mu+(4*sigma))
    
    x = np.concatenate((xa,xb,xc), axis=0)

    ya = norm.pdf(xa,mu,sigma)
    yb = norm.pdf(xb,mu,sigma)
    yc = norm.pdf(xc,mu,sigma)

    y = np.concatenate((ya,yb,yc), axis=0)

    pf_plota.plotar('Confidence Interval','t student scores','x bar', \
           'probabilidade','pdf',x,y,limite_inferior, \
           limite_superior,sigma,mu,xa,ya,xc,yc,alpha,np.array([]),n_amostra)
    
    # ----------------------------------------------
    # desenha curva baseada na distribuição Student.
    # ----------------------------------------------    
    mu = mu_amostra
    sigma = s_amostra
    limite_inferior = tinf
    limite_superior = tsup
    
    xa = np.linspace(-4,limite_inferior)
    xb = np.linspace(limite_inferior,limite_superior)
    xc = np.linspace(limite_superior,4)
    
    x = np.concatenate((xa,xb,xc), axis=0)
    
    ya = t.pdf(xa,n_amostra-1)
    yb = t.pdf(xb,n_amostra-1)
    yc = t.pdf(xc,n_amostra-1)
    
    y = np.concatenate((ya,yb,yc), axis=0)

    za = norm.pdf(xa)
    zb = norm.pdf(xb)
    zc = norm.pdf(xc)
    
    z = np.concatenate((za,zb,zc), axis=0)
    
    pf_plota.plotar('Confidence Interval','t student scores','x bar', \
               'probabilidade','pdf',x,y,limite_inferior, \
               limite_superior,sigma,mu,xa,ya,xc,yc,alpha,z,n_amostra)

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


