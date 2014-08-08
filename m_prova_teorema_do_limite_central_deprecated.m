% --- teorema do limite central.
% --- jorgearacaty 19:44 08/06/2013.

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
        ri = randi(ls,n,1) % gera nums uniformemente distribuidos.
        M = [M sum(ri)];
end
hist(M)

% tentativa de fazer com exponencial
for inx = 1:q
        % amostra de n itens, valores poss�veis 1 to ls,
        % o limite inferior � sempre 1 em randi().
        ri = exprnd(5:50) % gera nums uniformemente distribuidos.
        M = [M sum(ri)];
end
% hist(M)


normcdf(1,0,1); % substitue a tabela z. 