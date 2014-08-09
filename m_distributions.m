% ---------------------------------------
% --- Matlab 7.9.0.529 (R2009b).
% --- m_distributions.m - fit dezena 2 da quina,
% --- para Rayleigh() e outras.
% --- criado em - jorgearacaty, 31 jul 2014 - 11:07.
% --- jorgearacaty, 8 aug 2014 - 2211.
% ---------------------------------------

% -------------------------------
% Splash.
% -------------------------------
clear; clc;
nome_programa = 'm_distributions.m';
fprintf('\n------------------------------------------');
fprintf('\n--- programa: %s',nome_programa);
fprintf('\n------------------------------------------\n');

% File operations, lê CSV, ordena linhas, matrix dimensions.
file_name = 'csvQuina.csv'; I = csvread(file_name);
Q = sort(I,2); 
[mQ, nQ] = size(Q);

figure;

% histograma da segunda dezena.
hist(Q(:,2),80);
hold on;

% Rayleigh distribution, plota pdf.
pdfRay = raylpdf([1:80],21.5019);
plot([1:80],pdfRay*mQ,'g*');

% palpite ilustrativo.
%guessRay = round(raylrnd(21.4913))

% Weibull distribution, plota pdf.
pdfWbl = wblpdf([1:80],30.6001,2.0633);
plot([1:80],pdfWbl*mQ,'r.');  % pdfWbl*mQ é para manter o gráfico aceitável.

% titulos e legendas.
title('Distribuições para a segunda dezena da quina') 
legend('histograma','Rayleigh','Weibull','Location','NorthEast');
xlabel('x');
ylabel('y');

% ---------------------------------------------
% prova do CLT para a primeira dezena da quina.
% ---------------------------------------------
figure;

% histograma da distribuição da primeira dezena
P = Q(:,1);
hist(P);

mu = mean(P)
sigma = std(P);

% tamanho das amostras.
n = 30;

% quantidade de amostras. 
q_samples = 30;  

% standard deviation calculado (sample means).
sigma_bar = sigma/sqrt(n)

% amostragem.
A = zeros(q_samples, n);
for ind = 1:q_samples
    A(ind,:) = randsample(P,n);
end

% medias das amostras.
samples_means = mean(A');

% parametros das amostras.
clt_mean_bar = mean(samples_means)
clt_sigma_bar = std(samples_means)

figure;

% histograma das samples means.
hist(samples_means)


