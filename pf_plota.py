# --------------------------------------------
# --- Python 2.7.3.
# --- pf_plota - fit dezena 2 da quina para Rayleigh().
# --- criado em - jorgearacaty 10 aug 2014 - 2300.
# --- jorgearacaty, 11 aug 2014 - 1345.
# --------------------------------------------

import matplotlib.pyplot as plt

# -----------------------------------------------
# desenha gráficos.
# -----------------------------------------------        
def plotar(tit_janela,tit_graf,x_lbl,y_lbl,leg_1,x,y, \
           linf,lsup,sigma,mu,xa,ya,xc,yc,alpha,z,ene):
    
        # seta nome da janela.
        fig = plt.gcf()
        fig.canvas.set_window_title(tit_janela)
        
        plt.figure        
        
        # título, labels e grid.
        plt.title(tit_graf)
        plt.ylabel(y_lbl)
        plt.xlabel(x_lbl)
        plt.grid(True)

        spot_h_inf = xa.min()+((linf-xa.min())/2)

        v_len = y.max()-y.min()
        h_len = x.max()-x.min()

        # "%0.2f" % linf
        # labels valor critico.
        plt.text(linf, ya.max(),' v. critico (' + "%0.2f" % linf+')', \
                 horizontalalignment='right')
        plt.text(lsup, ya.max(),' v. critico (' + "%0.2f" % lsup+')', \
                 horizontalalignment='left')

        # label alpha/2 inferior.
        plt.text(spot_h_inf, ya.max()/2, \
                 str(alpha/2),horizontalalignment='center')
        # label alpha/2 superior.
        plt.text(lsup+((xc.max()-lsup)/2), ya.max()/2, \
                 str(alpha/2), horizontalalignment='center')

        # linha até a área inferior.
        plt.plot((spot_h_inf, (xa.min()+((linf-xa.min())*.85))),  \
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
                   'alpha = ' + str(alpha) + '\n' + \
                   'n = ' + str(ene)
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
