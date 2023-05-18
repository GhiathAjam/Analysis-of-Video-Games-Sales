import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, skew 
from scipy import stats
from scipy.stats import f_oneway

def plot(df,x,y, title):
    plt.figure(figsize=(5,5))
    x_axis= df[x]
    y_axis= df[y]
    plt.bar(x_axis, y_axis)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

def scatter(df,x,y, title):
    plt.figure(figsize=(8,4))
    x_axis= df[x]
    y_axis= df[y]
    plt.scatter(x_axis, y_axis)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

def encoding(df, method ='frequency'):
    '''
    Encode the categorical features using the given method
    '''
    if method == 'frequency':
        for col in df.columns:
                if col in [ 'Publisher', 'Developer', 'Platform', 'Genre','Rating']:
                    df[col] = df[col].map(df[col].value_counts())/len(df)
    # for all columns remove rows with string values
    # for col in df.columns:
    #     if df[col].dtype == 'object':
    #         df = df[df[col].str.isnumeric()]


    return df

def plot_distribution(df, col):
    '''
    Plot the distribution of the given column
    '''
    sns.distplot(df[col] , fit=norm);
    (mu, sigma) = norm.fit(df[col])
    plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu, sigma)],loc='best')
    plt.ylabel('Count')
    plt.title(col +' distribution')
    plt.show()

     
from scipy.stats import ttest_ind

def ttest(df, col, lbl):
    # get unique labels
    labels = df[lbl].unique()

    data = [df[df[lbl] == label][col].mean() for label in labels]

    t = 0
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            tij, pij = ttest_ind(df[df[lbl] == labels[i]][col].values,
                                 df[df[lbl] == labels[j]][col].values)
            if abs(tij) > t:
                t, p, label1, label2 = tij, pij, labels[i], labels[j]

    return t, p, label1, label2



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
