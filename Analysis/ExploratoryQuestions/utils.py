from scipy.stats import f_oneway
import numpy as np
from scipy.stats import ttest_ind


def ANOVA_test(df, cat_feature, num_feature, cats=[]):
    '''
    This function computes the ANOVA test between a categorical feature and a numerical feature
    can take df, categorical feature and numerical feature as input
    and optional list of  specific categories of the categorical feature
    '''
    if len(cats)==0:
        cats = df[cat_feature].unique()
    # Compute ANOVA test
    groups = []
    for category in cats:
        groups.append(df[df[cat_feature]==category] [num_feature])
    f_value, p_value = f_oneway(*groups)

    # Print the F-value and p-value
    print("P-value: ", p_value)
    print("F-value: ", f_value)

def ttest(df, col, lbl):
    # get unique labels
    labels = df[lbl].unique()
    # get data
    data = [df[df[lbl] == label][col] for label in labels]
    # ttest each pair
    # get worst p-value
    p = 1
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            tij, pij = ttest_ind(data[i], data[j])
            # print(f'p-value for {labels[i]} Vs. {labels[j]} = {p}')
            if pij < p:
                t, p, label1, label2 = tij, pij, labels[i], labels[j]
    # t, p = ttest_ind(data[0], data[1])
    # print
    print(f'p-value for {col} Vs. {lbl} = {p}')
    return t, p, label1, label2

# compute correlation ratio between publisher and sales
def correlation_coefficient(df, cat_feature, num_feature, cats=[]):

    if len(cats) == 0:
        cats = df[cat_feature].unique()

    categories = np.array(df[cat_feature])
    values = np.array(df[num_feature])
    
    group_variances = 0
    for category in cats:
        group = values[np.where(categories == category)[0]]
        group_variances += len(group)*(np.mean(group)-np.mean(values))**2
    total_variance = sum((values-np.mean(values))**2)

    print("Correlation coefficient: ", group_variances/total_variance)
    print("Correlation coefficient: ", (group_variances/total_variance)**.5)
