clc
clear
rng(6050);
numsim      = (10);
tic
%% Assumptions & Variable Declarations for stock price simulations %%
S0          = 72.72;
vol         = 0.3715;
rfr         = 0.0697;
dt          = [0.8333,1,1,1,1,0.8849];
numsteps    = length(dt);

S = zeros(numsim,numsteps)
for i = 1:numsteps
    Z         = randn(numsim,1);
    if i==1
        S(:,i)    = S0      .*exp((rfr - vol^2/2).* dt(i) + sqrt(dt(i)) .* vol .* Z);
    else
        S(:,i)    = S(:,i-1).*exp((rfr - vol^2/2).* dt(i) + sqrt(dt(i)) .* vol .* Z);       
    end
end
Stock      = S(:,6)
toc
