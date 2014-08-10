% ---------------------------------------
% --- FUNCTION - Matlab 7.9.0.529 (R2009b).
% --- plotar.m - plota distr, normal,
% --- gráficos com área sombreada e outros plots interessantes.
% --- criado em - jorgearacaty, 9 ago 2014 - 1200.
% --- jorgearacaty, 9 ago 2014 - 1200.
% ---------------------------------------

function [] = plotar(mu,sigma,alpha,x,y,limite_superior,limite_inferior)

    figure;

    plot(x,y)
    
    % legendas e titulos.
    title('Distribuição de Probabilidades','fontsize', 14);
    legend('pdf','Location','NorthEast');
    xlabel('x');
    ylabel('probabilidade (100% = 1)');
    
    % texto do limite com seta e bolinha.
    text(limite_inferior,alpha,...
    ['\bullet\leftarrow\fontname{times}critical value ' num2str(limite_inferior)],...
    'FontSize',14)
    
    % texto do limite com seta e bolinha.
    text(limite_superior,alpha,...
    ['\bullet\leftarrow\fontname{times}critical value ' num2str(limite_superior)],...
    'FontSize',14)

    % shaded area inferior.
    xlo = [x(x<=limite_inferior) limite_inferior];
    ylo = [y(x<=limite_inferior) 0];
    patch(xlo, ylo, 'y')

    % shaded area superior.
    xhi = [limite_superior x(x>=limite_superior)];
    yhi = [0 y(x>=limite_superior)];
    patch(xhi, yhi, 'y')
    
    % textbox.
    annotation('textbox',...
    [0.15 0.6 0.25 0.25],...
    'String',{['alpha = ' num2str(alpha)],['mu = ' num2str(mu)],...
    ['sigma = ' num2str(sigma)],['l.inf = ' num2str(limite_inferior)],...
    ['l.sup = ' num2str(limite_superior)]},...
    'FontSize',12,...
    'FontName','Arial',...
    'LineStyle','--',...
    'EdgeColor',[1 1 0],...
    'LineWidth',2,...
    'BackgroundColor',[0.9  0.9 0.9],...
    'Color',[0.84 0.16 0]);

