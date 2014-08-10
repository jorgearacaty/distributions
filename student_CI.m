
clc
s = [1, 2, 3, 4, 5, 6, 20]
mu_amostra = mean(s)
s_amostra = std(s)
[no n_amostra] = size(s)
alpha = 0.05

tinf = tinv(alpha/2,n_amostra-1)
tsup = tinv(1-(alpha/2),n_amostra-1)

xis_inf = mu_amostra + (tinf * (s_amostra / sqrt(n_amostra)))
xis_sup = mu_amostra + (tsup * (s_amostra / sqrt(n_amostra)))