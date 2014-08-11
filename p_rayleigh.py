# --------------------------------------------
# --- Python 2.7.3.
# --- p_raylegh.py - fit dezena 2 da quina para Rayleigh().
# --- criado em - jorgearacaty 1 aug 2014 - 0214.
# --- jorgearacaty, 8 aug 2014 - 2108.
# --------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.stats as scs

import os
import sys
import csv
import random 

# ------------------------------------------
# Fit 2ª dezena da Quina para distribuições. 
# ------------------------------------------
def lendo_csv():
    
    # ------------------------------------
    # File operations, lê CSV, ordena.
    # ------------------------------------
    file_name = 'csvQuina.csv'
    
    # importa do CSV, e ordena as linhas.
    total = np.sort(np.loadtxt(file_name,delimiter=','),1)
    print total, "\n"
    
    # escolhe segunda dezena como população
    y = total[:,1]
    size = y.size
    print str(size) + " - " + str(total[size-1,:]) + "\n"

    # -------------------------------------------
    # Multiple fitted - 2 WARNINGS (bypassed)
    # -------------------------------------------
    if 1 == 0:
        x = scipy.arange(1,size+1)
        
        banda_de_bins = scipy.arange(0,80,5)
        h = plt.hist(y, bins=range(80),color='white')
        #----------------------normed=1,alpha=.3,
        #h = plt.hist(y,bins=banda_de_bins,color='white')        
        dist_names = ['alpha', 'beta', 'arcsine','weibull_min', 'weibull_max', 'rayleigh']
        
        for dist_name in dist_names:
            
            dist = getattr(scs, dist_name)
            param = dist.fit(y)

            pdf_fitted = dist.pdf(x, *param[:-2], loc=param[-2], scale=param[-1]) * size
            plt.plot(pdf_fitted, label=dist_name)
            
            # limites de apresentação do eixo 'x'
            plt.xlim(1,80)
            
        plt.legend(loc='upper left')
        plt.show()
    
    # -----------------------------------------------
    # operações de fit para rayleigh distribution.
    # -----------------------------------------------
    if 1 == 1:
        
        # parametros para brincar.
        par1 = 1
        par2 = 20

        # seta nome da janela.
        fig = plt.gcf()
        fig.canvas.set_window_title('Estudo de distribuição Rayleigh')
        
        plt.figure        
        param = scs.rayleigh.fit(y)     # capta parametros da população.
        
        # imprime parãmetros captados.
        print 'parametros -> ', param[0], " - ", param[1]
        
        x = np.linspace(1,80,80)    # eixo dos 'x' de 1 a 80.
        #x = scipy.arange(1,81) - ou um ou outro.

        # gera pdf rayleigh com parametros chutados.
        pdf = scs.rayleigh.pdf(x,loc=par1,scale=par2)
        
        # gera pdf rayleigh com parâmetros da população captados com rayleigh.fit(y).
        pdf_fitted = scs.rayleigh.pdf(x,loc=param[0],scale=param[1])

        # título, labels e grid.
        plt.title('Rayleigh distribution')
        plt.ylabel('Probabilidade')
        plt.xlabel('Numeros')
        plt.grid(True)

        # plota as duas curvas e seta local da legenda.
        plt.plot(x,pdf_fitted,'r-', label = 'fitted')
        plt.plot(x,pdf,'b.', label = 'chute')
        plt.legend(loc='upper right')        

        # plota histograma da população.
        plt.hist(y,normed=1,alpha=.3,bins=range(80),color = 'cyan')

        # gera pontos randomicos e traça histograma de acordo com random.weibullvariate.
        pontos = []
        for x in xrange(3000):
            pontos.append(random.weibullvariate(30.6001,2.0633))

        # histograma com largura de bins customizados.    
        banda_de_bins = scipy.arange(0,80,5) #[0,5,10,15,20,25,30,35,40,45,50,55,60,65.70,75.80]
        plt.hist(pontos,normed=1,alpha=.3, \
                 bins=banda_de_bins, \
                 color='crimson')
        plt.show()

        # seta nome da janela.
        fig = plt.gcf()
        fig.canvas.set_window_title('Histograma random.weibullvariate')
        
        # nova janela.
        plt.figure
        plt.hist(pontos,normed=1,alpha=.3, \
                 bins=banda_de_bins, \
                 color='crimson')
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
    
    lendo_csv()
    
    print "\nDONE"
    The_End = raw_input("press any key to go out, thks.\n")
