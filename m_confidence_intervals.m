% ---------------------------------------
% --- Matlab 7.9.0.529 (R2009b).
% --- m_confidence_intervals.m - Estudo de intervalos de confiança,
% --- gráficos com área sombreada e outros plots interessantes.
% --- criado em - jorgearacaty, 9 ago 2014 - 1200.
% --- jorgearacaty, 9 ago 2014 - 1900.
% ---------------------------------------

% -------------------------------
% Splash.
% -------------------------------
clear; clc;
nome_programa = 'm_confidence_intervals.m';
fprintf('\n------------------------------------------');
fprintf('\n--- programa: %s',nome_programa);
fprintf('\n------------------------------------------\n');

% -----------------------------------------------
% intervalos de confiança - confidence intervals.
% -----------------------------------------------
if 1 == 1;

    % confidence interval, media, desvio padrao.
    alpha = 0.05; 
    mu = 10;      
    sigma = 2;      
    
    % valores criticos.
    limite_inferior = norminv(alpha, mu, sigma);
    limite_superior = norminv(1-alpha, mu, sigma);

    % eixo horizontal.
    x = [linspace(mu-4*sigma,limite_inferior), ...
        linspace(limite_inferior,limite_superior), ...
        linspace(limite_superior,mu+4*sigma)];
    
    % eixo vertical.
    y = normpdf(x, mu, sigma);

    plotar(mu,sigma,alpha,x,y,limite_superior,limite_inferior)
    
    % ---------
    % z scores.
    % ---------
        
    % eixos horizontal e vertical.
    x_z = (x-mu)/sigma;
    y_z = normpdf(x_z);

    % valores criticos
    limite_inferior_z = norminv(alpha/2);
    limite_superior_z = norminv(1-(alpha/2));
    
    plotar(0,1,alpha,x_z,y_z,limite_superior_z,limite_inferior_z)
    
end

% -------------------------------------------------------------------------
% Confidence and Prediction Bounds
% http://www.mathworks.com/help/curvefit/confidence-and-prediction-bounds.h
% tml
% -------------------------------------------------------------------------
if 1 == 1;
    
    % Generate data with an exponential trend
    x = (0:0.2:5)';
    y = 2*exp(-0.2*x) + 0.5*randn(size(x));

    % Fit the data using a single-term exponential.
    fitresult = fit(x,y,'exp1');

    % Compute prediction intervals
    p11 = predint(fitresult,x,0.95,'observation','off');
    p12 = predint(fitresult,x,0.95,'observation','on');
    p21 = predint(fitresult,x,0.95,'functional','off');
    p22 = predint(fitresult,x,0.95,'functional','on');

    figure;
    
    % Plot the data, fit, and prediction intervals.
    subplot(2,2,1)
    plot(fitresult,x,y), hold on, plot(x,p11,'m--'), xlim([0 5])
    title('Nonsimultaneous observation bounds','Color','b')
    
    subplot(2,2,2)
    plot(fitresult,x,y), hold on, plot(x,p12,'m--'), xlim([0 5])
    title('Simultaneous observation bounds','Color','b')
    
    subplot(2,2,3)
    plot(fitresult,x,y), hold on, plot(x,p21,'m--'), xlim([0 5])
    title('Nonsimultaneous functional bounds','Color','b')
    
    subplot(2,2,4)
    plot(fitresult,x,y), hold on, plot(x,p22,'m--'), xlim([0 5])
    title('Simultaneous functional bounds','Color','b')
    
end

