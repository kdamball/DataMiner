## WEEK 1

**Supervised vs Unsupervised Learning.**
  - Supervised: Giving data with "right answers" given (algorithm produces more of these "right answers")
    - Think of them as regression problems. (Predicting house prices, malignant tumors (cancer))
    - Classification problems
    - You can have several features (SVM can deal with infinite number of features)
    - Basically, you always know what is it you're trying to find

  - Unsupervised learning:
    - You have data without a known structure.
    - You can find clusters (i.e: clustering) or associative/structure
    - Lots and lots of clustering analysis

### Linear Regression (One Variable)

- **Hypothesis Function**

It has a general form `h(x) = theta0 + theta1(x)`.
This is the general function to general our linear equation.



- **Cost Function**

This measures the accuracy of the *hypothesis function*. It takes an average of all results of the hypothesis with inputs(`x`s) compared to the actual outputs (`y`s). 

`J(theta0, theta1) = (1/2m)SUM(h(x`<sup>i</sup>`) - y`<sup>i</sup>`))`<sup>2</sup>

Where:

  `(1/2m)` => Squared error function or mean squared error. Mean is halved as a convenience of 
