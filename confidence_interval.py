﻿# --------------------------------------------
# --- Python 2.7.3.
# --- confidence_interval.py - fit dezena 2 da quina para Rayleigh().
# --- criado em - jorgearacaty 10 aug 2014 - 0214.
# --- jorgearacaty, 10 aug 2014 - 2021.
# --------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.stats as scs
from scipy.stats import norm
#import matplotlib.mlab as mlab
#from scipy import stats
from scipy.stats import t
from scipy import stats 

import os
import sys
import csv
import random
import math

# -----------------------------------------------
# intervalos de confiança - confidence intervals.
# -----------------------------------------------
def confidence_interval():

    # --------------------------------------
    # sigma unknown - Amderson 2008 pag 310.
    # 95% confidence interval - t Student.
    # http://adventuresinpython.blogspot.com.br/2012/12/confidence-intervals-in-python.html

    s = np.array([1, 2, 3, 4, 5, 6, 20])
    
    n, min_max, mean, var, skew, kurt = stats.describe(s)
    
    s_amostra = math.sqrt(var)
    n_amostra = n
    mu_amostra = mean
    alpha = 0.05
    
    # n_amostra = 7


    tinf = t.ppf(alpha/2,n_amostra-1)
    tsup = t.ppf(1-(alpha/2),n_amostra-1)
    

    # outro metodo de achar os t scores.
    #tinf, tsup = t.interval(0.95, n_amostra-1, loc=1, scale=0)
    #print tinf, tsup, mean, s_amostra, n_amostra

    #print t.pdf(tinf,n_amostra-1)

    xis_inf = mu_amostra + (tinf * (s_amostra / math.sqrt(n_amostra)))
    xis_sup = mu_amostra + (tsup * (s_amostra / math.sqrt(n_amostra)))

    print xis_inf, xis_sup
        
    # ---------------------------------------
   
    if 1 == 1:
        
        s_pop = 20
        n =100
        # confidence interval, media, desvio padrao.
        alpha, mu, sigma = 0.05, 60, s_pop/math.sqrt(n) 
        print s_pop/math.sqrt(n) 


        # valores criticos.
        limite_inferior = norm.ppf(alpha/2, mu, sigma);
        limite_superior = norm.ppf(1-(alpha/2), mu, sigma);

        # eixo horizontal - com 4 vezes pode dar erro to tamanho do eixo.
        xa = np.linspace(mu-(3.99*sigma),limite_inferior)
        xb = np.linspace(limite_inferior,limite_superior)
        xc = np.linspace(limite_superior,mu+(3.99*sigma))

        x = np.concatenate((xa,xb,xc), axis=0)

        #print xa.min(), x.min()

        # eixo vertical.
        ya = norm.pdf(xa,mu,sigma)
        yb = norm.pdf(xb,mu,sigma)
        yc = norm.pdf(xc,mu,sigma)
        
        y = np.concatenate((ya,yb,yc), axis=0)
  
        plotar('Confidence Interval','Distribuicao','x bar', \
               'probabilidade','pdf',x,y,limite_inferior, \
               limite_superior,sigma,mu,xa,ya,xc,yc,alpha)

    if 1 == 1:
        sigma = 1

        li_st = norm.ppf(alpha/2);
        ls_st = norm.ppf(1-(alpha/2));
        #print li_st, ls_st

        s_pop = 20
        n = 100
        print (60 + (li_st * s_pop/math.sqrt(n)))

        xa = np.linspace(-4*sigma,li_st)
        xb = np.linspace(li_st,ls_st)
        xc = np.linspace(ls_st,4*sigma)

        x = np.concatenate((xa,xb,xc), axis=0)

        ya = norm.pdf(xa)
        yb = norm.pdf(xb)
        yc = norm.pdf(xc)
        
        y = np.concatenate((ya,yb,yc), axis=0)
        
        plotar('Confidence Interval','Distribuicao','x bar', \
               'probabilidade','pdf',x,y,li_st, \
               ls_st,1,0,xa,ya,xc,yc,alpha)
        
def plotar(tit_janela,tit_graf,x_lbl,y_lbl,leg_1,x,y, \
           linf,lsup,sigma,mu,xa,ya,xc,yc,alpha):

        font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 16,
        }
    
        # seta nome da janela.
        fig = plt.gcf()
        fig.canvas.set_window_title(tit_janela)
        
        plt.figure        
        
        # título, labels e grid.
        plt.title(tit_graf)
        plt.ylabel(y_lbl)
        plt.xlabel(x_lbl)
        plt.grid(True)

        v_len = y.max()-y.min()
        h_len = x.max()-x.min()
        
        # posição de labels e labels valor critico.
        dpl = 1.000/(sigma*10)
        scrto = '$valor$' + ' ' + '$critico$'
        plt.text(x.min()+(h_len/19), dpl, '$valor$' + ' ' + '$critico$', fontdict=font)
        plt.text(lsup, dpl,scrto , fontdict=font)

        str_text = 'val crit inf = ' + str(linf) + '\n' + \
                   'val crit sup = ' + str(lsup) + '\n' + \
                   'media = ' + str(mu) + '\n' + \
                   'desvio padrao = ' + str(sigma)  + '\n' + \
                   'alpha = ' + str(alpha)
        plt.text(x.min()+(h_len/27), y.max()-(v_len/20),str_text,
             horizontalalignment='left',
             verticalalignment='top')

        plt.plot(x,y,'r-', label = leg_1)
        
        plt.fill_between(xa,ya,0,color='cyan')
        plt.fill_between(xc,yc,0,color='cyan')

        # plota linhas dos limite criticos
        plt.plot((linf, linf), (0, ya.max()), 'y-')
        plt.plot((lsup, lsup), (0, ya.max()), 'y-')
        # não usar -> plt.axvline(x=linf, ymin=0, ymax = .1, linewidth=1, color='k')
        
        plt.legend(loc='upper right')        
#---------------------------------------------------
        plt.show()
#---------------------------------------------------        


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
