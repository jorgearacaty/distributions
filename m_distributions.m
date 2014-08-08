% ---------------------------------------
% --- Programa Matlab.
% --- Fit dezena 2 da quina para Rayleigh() e outras.
% --- jorgearacaty 31 jul 2014 - 11:07.
% ---------------------------------------

file_name = 'csvQuina.csv'; I = csvread(file_name);
Q = sort(I,2); 
[mQ, nQ] = size(Q);

figure;
hist(Q(:,2),80);
hold on;
% --- Rayleigh distribution, plota pdf entre 1 e 80.
pdfRay = raylpdf([1:80],21.5019);
plot([1:80],pdfRay*mQ,'g*');
guessRay = round(raylrnd(21.4913))

% --- Weibull distribution
pdfWbl = wblpdf([1:80],30.6001,2.0633);

% figure;
plot([1:80],pdfWbl*mQ,'r.');
% pdfWbl*mQ é a dica para manter o gráfico aceitável.
title('Distribuições para a segunda dezena da quina') 
legend('histograma','Rayleigh','Weibull','Location','NorthEast');
xlabel('porra');
ylabel('cacilda');

% ---------------------------------------------
% prova do CLT para a primeira dezena da quina.
% ---------------------------------------------
figure
P = Q(:,1);
hist(P);

mu = mean(P)
sigma = std(P);
n = 30;                 % tamanho das amostras.
q_samples = 30;          % quantidade de amostras.  
sigma_bar = sigma/sqrt(n)

% recolhe amostras.
A = zeros(q_samples, n);
for ind = 1:q_samples
    A(ind,:) = randsample(P,n);
end
% medias das amostras
samples_means = mean(A');
% parametros das amostras.
clt_mean_bar = mean(samples_means)
clt_sigma_bar = std(samples_means)

figure
hist(samples_means)



% ---------------------------------
if 1 == 2
    figure;
    pdfWbl = wblpdf([1:80],55,3.1123);
    plot([1:80],pdfWbl,'y.');
end

