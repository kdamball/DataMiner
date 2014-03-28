function J = squareThisNumber(X, y, theta)
% X is the "design matrix" containing our training examples
% y is the class labels

m = size(X,1);					%number of training egs
predictions = X*theta; 	%predictions of hypothesis on all m examples
sqErrors = (predictions-y).^2; % square errors
J = 1/(2*m) * sum(sqErrors);