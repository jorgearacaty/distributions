# --------------------------------------------
# --- Python 2.7.3.
# --- p_ci_normal.py - fit dezena 2 da quina para Rayleigh().
# --- criado em - jorgearacaty 10 aug 2014 - 0214.
# --- jorgearacaty, 10 aug 2014 - 2021.
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

# -----------------------------------------------
# intervalos de confiança - confidence intervals.
# -----------------------------------------------
def confidence_interval():
   
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
  
        plotar('Confidence Interval','distribuicao','x bar', \
               'probabilidade','pdf',x,y,limite_inferior, \
               limite_superior,sigma,mu,xa,ya,xc,yc,alpha)

    if 1 == 1:
        
        #sigma = 1

        li_st = norm.ppf(alpha/2);
        ls_st = norm.ppf(1-(alpha/2));

        #s_pop = 20
        #n = 100
        #print (60 + (li_st * s_pop/math.sqrt(n)))

        xa = np.linspace(-4,li_st)
        xb = np.linspace(li_st,ls_st)
        xc = np.linspace(ls_st,4)

        x = np.concatenate((xa,xb,xc), axis=0)

        ya = norm.pdf(xa)
        yb = norm.pdf(xb)
        yc = norm.pdf(xc)
        
        y = np.concatenate((ya,yb,yc), axis=0)
        
        plotar('Confidence Interval','z scores','x bar', \
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

        # "%0.2f" % linf
        # labels valor critico.
        plt.text(linf, ya.max(),' v. critico (' + "%0.2f" % linf+')',horizontalalignment='right')
        plt.text(lsup, ya.max(),' v. critico (' + "%0.2f" % lsup+')', horizontalalignment='left')

        # label alpha/2 inferior.
        plt.text(xa.min()+((linf-xa.min())/2), ya.max()/2, \
                 str(alpha/2),horizontalalignment='center')
        # label alpha/2 superior.
        plt.text(lsup+((xc.max()-lsup)/2), ya.max()/2, \
                 str(alpha/2), horizontalalignment='center')

        # linha até a área inferior.
        plt.plot((xa.min()+((linf-xa.min())/2), (xa.min()+((linf-xa.min())*.85))),  \
                 (ya.max()/2, ya.max()/4), 'b-')
        # xiszinho.
        plt.plot(xa.min()+((linf-xa.min())*.85),  \
                 (ya.max()/4), 'bx')

        # linha até a área superior.
        plt.plot((lsup+((xc.max()-lsup)/2), (xc.max()-((linf-xa.min())*.85))),  \
                 (ya.max()/2, ya.max()/4), 'b-')  
        # xiszinho.
        plt.plot((xc.max()-((linf-xa.min())*.85)),  \
                  ya.max()/4, 'bx')  

        # box com informações principais.
        str_text = 'val crit inf = ' + str(linf) + '\n' + \
                   'val crit sup = ' + str(lsup) + '\n' + \
                   'media = ' + str(mu) + '\n' + \
                   'desvio padrao = ' + str(sigma)  + '\n' + \
                   'alpha = ' + str(alpha)
        plt.text(x.min()+(h_len/27), y.max()-(v_len/20),str_text,
             horizontalalignment='left',
             verticalalignment='top')
        
        # desenha curva em forma de sino.
        plt.plot(x,y,'r-', label = leg_1)

        # áreas anchuradas de alpha/2.
        plt.fill_between(xa,ya,0,color='cyan')
        plt.fill_between(xc,yc,0,color='cyan')

        # plota linhas verticais dos limite criticos
        plt.plot((linf, linf), (0, ya.max()), 'y-')
        plt.plot((lsup, lsup), (0, ya.max()), 'y-')
        plt.plot((lsup), (ya.max()), 'k*')
        plt.plot((linf), (ya.max()), 'k*')
        
        plt.legend(loc='upper right')        
        plt.show()

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
    The_End = raw_input("press any key to go out, thks.\n")

