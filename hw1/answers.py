r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""

1. False. Some splits can represent the original distribution better then others, and that can make them more usefull. 
In addition, some splits can be extremly unuseful because of imbalance, for example if a class dont apear in the train but only in the test, or there may be edge cases that apear only in the test. 


2. False. The test-set must remain untuched in the training proccess, because using it may reduce the test affecienity and also cause overfitting.


3. True. In the cross validation proccess we average all the validation-set performence so the error is based on several trains and validation splits instead of on one.

4. True. Injecting noises can help to test if the model is overfitting, because it make the data more random and prevent memorizing patterns.
"""

part1_q2 = r"""

No. As we answered in q1-2, the test must remain untuched during the training - or the all train proccess will be biased by the test-set.
"""

# ==============
# Part 2 answers

part2_q1 = r"""

$\Delta$ is representing the margin, so when $\Delta < 0$, the margin we allow is negetive, what mean that we 'tolerate' misclassify as far as they are small enough (smaller the $\Delta$).
In other words, the model will incur zero loss even in cases of misclassify. 

"""
part2_q2 = r"""

The model learn the 'average digit shape', giving score to each pixel based on the probability it is part of the digit. 
Errors could coure because of rotation of a digit; bigger or smaller, thiner or thicker digit than expected;  a digit written in iregular way; or, two similiar templates.
For example, there is a 6 that the model 'think' is 2, maybe because it rotated. also, a 4,5 and 7 written in an irregilar way that tagged wrongly. 

"""

part2_q3 = r"""
learning rate is good. if it was too high, we could see the graph going down very fast, and then stay the same. if it was too low, we could see the graph going down slowly and not get the minimal loss. in our grapg, the graph go down fast but keep getting down all the way.

The model is slightly overfitted to the training set. we can see the accuracy rate of the training is bettet then the test accuracy, but not by much and the test accuracy is high itself. 

"""

# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
**Your answer:**

The ideal pattern to see in a residual plot should be an evenly spread cluster
of residual points along the horizontal axis and centered around the zero value 
of that same axis indicating a small errors.

Plot examination:
Examining the top-5 features we can see  a trend that tends away from zero,
meaning larger residuals that translate into less accurate results.
Moreover, we can see that the residuals in the top-5 plots
are spread far away from the fitted line indicating in poor learning of the data.
After applying the non-linearity, we can see a clear improvement in the plotted
residuals, such that they're more evenly distributed across the horizontal axis
and mostly centered around the zero value. We can also see that the fitted line
describes the residuals much more accurately according to our description in the
first part of the question.


"""

part3_q2 = r"""
**Your answer:**
1. After adding non-linear features to our data the model is still a linear model.
   the non-linear features map our data to a higher dimension, yet the produced decision boundary is still linear in that
   dimension.
2. Yes, as shown in intro to machine learning (tutorial 9 on Regression) we can fit any non=linear function of the
original features but our model will be verry prone to overfitting. Various approaches were shown
as to how to mitigate the problem of overfitting e.x adding a regularization component to the loss function.

3. Adding non-linear features would produce decision boundaries that are more complex and most likely to curved in the
   in the original input space. Moreover, in that transformed space the (given the dimension is high enough) $W$ is a 
   linear hyperplane. As where in the original space the decision boundary is not a linear hyperplane.

"""

part3_q3 = r"""
**Your answer:**


Given $x, y \sim \text{Uniform}(0,1)$, the probability density function (PDF) is $f(x,y) = 1$ for $0 \le x,y \le 1$.

$$
\begin{aligned}
\mathbb{E}[|y-x|] &= \int_{0}^{1} \int_{0}^{1} |y-x| \, dy \, dx \\
&= \int_{0}^{1} \left[ \int_{0}^{x} (x-y) \, dy + \int_{x}^{1} (y-x) \, dy \right] dx \\
&= \int_{0}^{1} \left[ \left[xy - \frac{y^2}{2}\right]_{0}^{x} + \left[\frac{y^2}{2} - xy\right]_{x}^{1} \right] dx \\
&= \int_{0}^{1} \left[ \left(x^2 - \frac{x^2}{2}\right) + \left(\left(\frac{1}{2} - x\right) - \left(\frac{x^2}{2} - x^2\right)\right) \right] dx \\
&= \int_{0}^{1} \left[ \frac{x^2}{2} + \frac{1}{2} - x + \frac{x^2}{2} \right] dx \\
&= \int_{0}^{1} \left(x^2 - x + \frac{1}{2}\right) \, dx \\
&= \left[ \frac{x^3}{3} - \frac{x^2}{2} + \frac{x}{2} \right]_{0}^{1} \\
&= \frac{1}{3} - \frac{1}{2} + \frac{1}{2} \\
&= \mathbf{\frac{1}{3}}
\end{aligned}
$$

"""

# ==============

# ==============
