% ---------------------------------------
% --- Matlab 7.9.0.529 (R2009b).
% --- m_usando_allfitdist.m - fit dezena 2 da quina,
% --- usando allfitdist().
% --- criado em - jorgearacaty, 21 jul 2014 - 1837.
% --- jorgearacaty, 9 aug 2014 - 0904.
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

% usando allfitdist.
[D PD] = allfitdist(Q(:,2),'PDF');

% listando parametros.
D(1)
D(2)
D(3)
D(4)

