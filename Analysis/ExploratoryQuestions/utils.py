from scipy.stats import f_oneway
import numpy as np


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


