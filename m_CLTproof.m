%
% Prova do Teorema Central.
% jorgearacaty 3 ago 2014.

fprintf('\n---------------------------------\n')
fprintf('\n--- Prova do teorema central. ---\n')

% cria uma popula��o de 100 numeros uniformamente distribuidos.
%S = unifrnd(10,30,1,1000);  % unifrnd(lim-inf,lim-sup,rows,columns)
S = randi([10 30],1,1000);
mu = mean(S)
sigma = std(S)
% hist(R);
n = 20                  % tamanho das amostras.
q_samples = 30;         % quantidade de amostras.  

sigma_bar = sigma/sqrt(n)

% recolhe amostras.
A = zeros(q_samples, n);
for ind = 1:q_samples
    A(ind,:) = randsample(S,n);
end

y = datasample(S,q_samples)

% medias das amostras
samples_means = mean(A');

% parametros das amostras.
clt_mean_bar = mean(samples_means)
clt_sigma_bar = std(samples_means)

% hist(samples_means)

fprintf('\n---------------------------------\n')
sigma_bar
clt_sigma_bar

fprintf('\n---------------------------------\n')
% ERRO (as amostras s�o uniformemente distribuidas).
% teorema do limite central.
% a soma dos itens (ou m�dias), de q amostras de uma popula��o
% t�m uma distribui��o normal,
% se n for suficientemente grande (>=30),
% n�o importando qual a distribui��o da popula��o,
% podendo tamb�m ser uma cole��o de rv's independentes.

ls = 200;     % limite superior.
n = 30;     % qt. itens da amostra.
q = 100;     % n. de amostras
M = [];
for inx = 1:q
        % amostra de n itens, valores poss�veis 1 to ls,
        % o limite inferior � sempre 1 em randi().
        ri = randi([-10 10],n,1); % gera nums inteiros uniformemente distribuidos.
        M = [M sum(ri)];    % constroi vetor com as somas
end
% hist(M)

% resumo.
% ERRO (as amostras s�o uniformemente distribuidas).
MM = randi([-10 10],30,100); % n� rand uniform distro, intervalo -10 a 10,
                             % n=30 (row), 100 amostras (col), as amostras
                             % ser�o 100 vetores coluna com 30 elementos.
% fazendo o resultado um vetor coluna -> sum(MM)'                             
% hist(sum(MM))

