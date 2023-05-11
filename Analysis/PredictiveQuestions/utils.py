import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, skew 
from scipy import stats

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

     
