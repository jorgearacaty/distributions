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

% cria uma população de 100 numeros uniformamente distribuidos.
%S = unifrnd(10,30,1,1000);  
% unifrnd(lim-inf,lim-sup,rows,columns)

% cria população,
S = randi([10 30],1,1000);

% calcula parâmetros.
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

% função datasample não funciona.
%y = datasample(S,q_samples)

% medias das amostras
samples_means = mean(A');

% média das médias amostras.
clt_mean_bar = mean(samples_means);

% desvio padrão real das médias das amostras. CLT - as médias das amostras,
% terão uma distribuição normal para um tamanho das amostras suficientemente
% grande (>=30).
clt_sigma_bar = std(samples_means);

% hist(samples_means)

fprintf('\n---------------------------------\n')

sigma_bar
clt_sigma_bar

fprintf('\n---------------------------------\n')

% -------------------------------------------------------------------------
% Método de amostragem onde não existe a população definida e as amostras,
% são geradas randomicamente (no caso uniformemente distribuidas), este
% approach não define muito bem a distribuição das sample means como sendo
% normal, pois força as amostras a terem as distribuições, no caso
% uniformes, enquanto no método anterior, as amostras não têm uma
% distribuição forçada.
% -------------------------------------------------------------------------
ls = 10;      % limite superior.
li = -10;     % limite inferior.  
n = 30;       % qt. itens da amostra.
q = 100;      % n. de amostras.
M = [];
for inx = 1:q
        % amostra de n itens, valores possíveis 1 to ls,
        % o limite inferior é sempre 1 em randi().
        ri = randi([li ls],n,1); % gera nums inteiros uniformemente distribuidos.
        M = [M sum(ri)];    % constroi vetor com as somas
end

% hist(M)

% outro exemplo errado.
% ERRO (as amostras são uniformemente distribuidas).
MM = randi([-10 10],30,100); % nº rand uniform distro, intervalo -10 a 10,
                             % n=30 (row), 100 amostras (col), as amostras
                             % serão 100 vetores coluna com 30 elementos.
% fazendo o resultado um vetor coluna -> sum(MM)'                             
%hist(sum(MM))

