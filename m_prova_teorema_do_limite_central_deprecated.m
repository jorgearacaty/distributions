% --- teorema do limite central.
% --- jorgearacaty 19:44 08/06/2013.

% teorema do limite central.
% a soma dos itens (ou médias), de q amostras de uma população
% têm uma distribuição normal,
% se n for suficientemente grande (>=30),
% não importando qual a distribuição da população,
% podendo também ser uma coleção de rv's independentes.

ls = 200;     % limite superior.
n = 30;     % qt. itens da amostra.
q = 100;     % n. de amostras
M = [];
for inx = 1:q
        % amostra de n itens, valores possíveis 1 to ls,
        % o limite inferior é sempre 1 em randi().
        ri = randi(ls,n,1) % gera nums uniformemente distribuidos.
        M = [M sum(ri)];
end
hist(M)

% tentativa de fazer com exponencial
for inx = 1:q
        % amostra de n itens, valores possíveis 1 to ls,
        % o limite inferior é sempre 1 em randi().
        ri = exprnd(5:50) % gera nums uniformemente distribuidos.
        M = [M sum(ri)];
end
% hist(M)


normcdf(1,0,1); % substitue a tabela z. 