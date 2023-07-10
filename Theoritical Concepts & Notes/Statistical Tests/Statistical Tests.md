Z-test: The Z-test is a statistical test used to determine if the mean of a sample differs significantly from a known population mean. It helps us understand whether an observed difference between a sample and a population is due to chance or represents a meaningful difference.

```
import scipy.stats as stats

sample = [4, 5, 6, 7, 8]  # Sample data
population_mean = 6.5  # Known population mean

z_score, p_value = stats.ztest(sample, value=population_mean)

if p_value < 0.05:
    print("Reject null hypothesis: Sample mean is significantly different from population mean.")
else:
    print("Fail to reject null hypothesis: Sample mean is not significantly different from population mean.")
```
Student's t-test: The Student's t-test is used to compare the means of two groups and determine if they are significantly different from each other. It is commonly employed when the sample size is small or when the population standard deviation is unknown.
```
import scipy.stats as stats

group1 = [1, 2, 3, 4, 5]  # First group data
group2 = [6, 7, 8, 9, 10]  # Second group data

t_statistic, p_value = stats.ttest_ind(group1, group2)

if p_value < 0.05:
    print("Reject null hypothesis: Means of the two groups are significantly different.")
else:
    print("Fail to reject null hypothesis: Means of the two groups are not significantly different.")

```
Chi-Square test: The Chi-Square test is a statistical test that assesses the independence between two categorical variables. It determines whether there is a significant association or relationship between the variables based on the observed frequencies in a contingency table.
```
import scipy.stats as stats

observed = [[10, 15, 5], [20, 25, 15]]  # Observed frequencies in a contingency table

chi2_statistic, p_value, _, _ = stats.chi2_contingency(observed)

if p_value < 0.05:
    print("Reject null hypothesis: There is a significant association between the variables.")
else:
    print("Fail to reject null hypothesis: There is no significant association between the variables.")

```
ANOVA (Analysis of Variance): ANOVA is a statistical test used to compare the means of three or more groups to determine if there are significant differences between them. It helps us understand if the observed variations in the means are due to true differences between the groups or random chance.
```
import scipy.stats as stats

group1 = [1, 2, 3, 4, 5]  # First group data
group2 = [6, 7, 8, 9, 10]  # Second group data
group3 = [11, 12, 13, 14, 15]  # Third group data

f_statistic, p_value = stats.f_oneway(group1, group2, group3)

if p_value < 0.05:
    print("Reject null hypothesis: Means of the groups are significantly different.")
else:
    print("Fail to reject null hypothesis: Means of the groups are not significantly different.")

```
Correlation: Correlation measures the strength and direction of the linear relationship between two variables. It quantifies how changes in one variable correspond to changes in another. A correlation coefficient ranges from -1 to 1, with -1 indicating a perfect negative correlation, 0 indicating no correlation, and 1 indicating a perfect positive correlation.
```
import numpy as np
import scipy.stats as stats

x = np.array([1, 2, 3, 4, 5])  # First variable
y = np.array([5, 4, 3, 2, 1])  # Second variable

correlation_coefficient, p_value = stats.pearsonr(x, y)

if p_value < 0.05:
    print("There is a significant correlation between the variables.")
else:
    print("There is no significant correlation between the variables.")

```
