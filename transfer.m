syms s x u

% Define the system dynamics (example equation)
f = u^3 + u^2*x + u*x^2 + x^3;

% Define the input and output variables
U = laplace(u);
X = laplace(x);

% Calculate the transfer function
TF = simplify(X/U);

% Display the transfer function
pretty(TF)
