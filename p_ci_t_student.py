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

    xa = np.linspace(mu-(3.99*sigma),limite_inferior)
    xb = np.linspace(limite_inferior,limite_superior)
    xc = np.linspace(limite_superior,mu+(3.99*sigma))
    
    x = np.concatenate((xa,xb,xc), axis=0)

    ya = norm.pdf(xa,mu,sigma)
    yb = norm.pdf(xb,mu,sigma)
    yc = norm.pdf(xc,mu,sigma)

    y = np.concatenate((ya,yb,yc), axis=0)

    plotar('Confidence Interval','t student scores','x bar', \
           'probabilidade','pdf',x,y,limite_inferior, \
           limite_superior,sigma,mu,xa,ya,xc,yc,alpha,np.array([]))
    
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
    
    plotar('Confidence Interval','t student scores','x bar', \
               'probabilidade','pdf',x,y,limite_inferior, \
               limite_superior,sigma,mu,xa,ya,xc,yc,alpha,z)
        
# -----------------------------------------------
# desenha gráficos.
# -----------------------------------------------        
def plotar(tit_janela,tit_graf,x_lbl,y_lbl,leg_1,x,y, \
           linf,lsup,sigma,mu,xa,ya,xc,yc,alpha,z):
    
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
        plt.text(linf, ya.max(),' v. critico (' + "%0.2f" % linf+')', \
                 horizontalalignment='right')
        plt.text(lsup, ya.max(),' v. critico (' + "%0.2f" % lsup+')', \
                 horizontalalignment='left')

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
        plt.plot(x,y,'r-', label = 't scores')
        if len(z) > 0:
            plt.plot(x,z,'b.', label = 'z scores')

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


