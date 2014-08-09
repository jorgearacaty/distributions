% ---------------------------------------
% --- Matlab 7.9.0.529 (R2009b).
% --- m_CLTproof.m - prova do CLT.,
% --- criado em - jorgearacaty, 3 aug 2014 - 1107.
% --- jorgearacaty, 9 aug 2014 - 0003.
% ---------------------------------------

% -------------------------------
% Splash.
% -------------------------------
clear; clc;
nome_programa = 'm_CLTproof.m';
fprintf('\n------------------------------------------');
fprintf('\n--- programa: %s',nome_programa);
fprintf('\n------------------------------------------\n');

% cria uma popula��o de 100 numeros uniformamente distribuidos.
%S = unifrnd(10,30,1,1000);  
% unifrnd(lim-inf,lim-sup,rows,columns)

% cria popula��o,
S = randi([10 30],1,1000);

% calcula par�metros.
mu = mean(S);
sigma = std(S);

% hist(R);

% tamanho das amostras.
n = 20;  

% quantidade de amostras.
q_samples = 30;           

% desvio das sample means calculado.
sigma_bar = sigma/sqrt(n);

% recolhe amostras.
A = zeros(q_samples, n);
for ind = 1:q_samples
    A(ind,:) = randsample(S,n);
end

% fun��o datasample n�o funciona.
%y = datasample(S,q_samples)

% medias das amostras
samples_means = mean(A');

% m�dia das m�dias amostras.
clt_mean_bar = mean(samples_means);

% desvio padr�o real das m�dias das amostras. CLT - as m�dias das amostras,
% ter�o uma distribui��o normal para um tamanho das amostras suficientemente
% grande (>=30).
clt_sigma_bar = std(samples_means);

% hist(samples_means)

fprintf('\n---------------------------------\n')

sigma_bar
clt_sigma_bar

fprintf('\n---------------------------------\n')

% -------------------------------------------------------------------------
% M�todo de amostragem onde n�o existe a popula��o definida e as amostras,
% s�o geradas randomicamente (no caso uniformemente distribuidas), este
% approach n�o define muito bem a distribui��o das sample means como sendo
% normal, pois for�a as amostras a terem as distribui��es, no caso
% uniformes, enquanto no m�todo anterior, as amostras n�o t�m uma
% distribui��o for�ada.
% -------------------------------------------------------------------------
ls = 10;      % limite superior.
li = -10;     % limite inferior.  
n = 30;       % qt. itens da amostra.
q = 100;      % n. de amostras.
M = [];
for inx = 1:q
        % amostra de n itens, valores poss�veis 1 to ls,
        % o limite inferior � sempre 1 em randi().
        ri = randi([li ls],n,1); % gera nums inteiros uniformemente distribuidos.
        M = [M sum(ri)];    % constroi vetor com as somas
end

% hist(M)

% outro exemplo errado.
% ERRO (as amostras s�o uniformemente distribuidas).
MM = randi([-10 10],30,100); % n� rand uniform distro, intervalo -10 a 10,
                             % n=30 (row), 100 amostras (col), as amostras
                             % ser�o 100 vetores coluna com 30 elementos.
% fazendo o resultado um vetor coluna -> sum(MM)'                             
%hist(sum(MM))

