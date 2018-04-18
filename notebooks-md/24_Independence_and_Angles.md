Independence and Angles 
In this section we take a closer look at how correlation can be interpreted geometrically in terms of angles. 

We have defined $X$ and $Y$ to have the standard bivariate normal density with correlation $\rho$ if

$$
Y ~ = ~ \rho X + \sqrt{1 - \rho^2} Z
$$

where $X$ and $Z$ are i.i.d. standard normal. We showed that $Y$ is also standard normal, and that the conditional density of $Y$ given $X = x$ is normal $(\rho x, 1 - \rho^2)$. 

Note that we are assuming that $\rho$ is neither $1$ nor $-1$, so that the conditional density is not degenerate.
------

{% include "../notebooks-html/24_Independence_and_Angles.html" %}
