import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as ss          


def plot_num_corr_matrix(df):
    '''
    Plot the correlation matrix between the numerical features
    '''
    num_features = [col for col in df.columns if type(df.iloc[0, df.columns.get_loc(col)]) != str]
    df_num_features = df[num_features]
    num_corr= df_num_features.corr()
    plt.figure(figsize=(8,6))
    # draw correlation matrix with green shades
    sns.heatmap(num_corr, annot=True, cmap='Blues')
    plt.title(f"Correlation matrix between features")
    plt.show()
    


def cramers_v(data, col1, col2):
    """ 
        This was modified from SO: https://stackoverflow.com/questions/46498455/categorical-features-correlation/46498792#46498792
    """
    confusion_matrix = pd.crosstab(data[col1], data[col2]).values
    chi2 = ss.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min((kcorr-1), (rcorr-1)))
    
def plot_cat_corr_matrix(df):
    '''
    plot a correlation matrix for the categorical features in the dataset
    '''
    disc_feats = [feat for feat in df.columns if type(df.iloc[0, df.columns.get_loc(feat)]) == str]
    df_disc = df[disc_feats]
    
    corr = np.zeros((len(disc_feats), len(disc_feats)))
    for i in range(len(disc_feats)):
        for j in range(len(disc_feats)):
            corr[i, j] = cramers_v(df_disc, disc_feats[i], disc_feats[j])
    
    # now plot the correlation matrix
    fig, ax = plt.subplots(figsize=(10, 10))
    for i in range(len(corr)):
        for j in range(len(corr)):
             ax.text(j, i, '{:.2f}'.format(corr[i, j]), ha="center", va="center", color="w")
    # sns.heatmap(corr, annot=True, cmap='Greens')
    ax.matshow(corr, cmap='Greens')
    plt.xticks(range(len(corr)), disc_feats, rotation=90)
    plt.yticks(range(len(corr)), disc_feats)
    plt.show()
    


def correlation_ratio(df, col1, col2):
    '''
    A measure of association between a categorical variable and a continuous variable.
    - Divide the continuous variable into N groups, based on the categories of the categorical variable.
    - Find the mean of the continuous variable in each group.
    - Compute a weighted variance of the means where the weights are the size of each group.
    - Divide the weighted variance by the variance of the continuous variable.
    
    It asks the question: If the category changes are the values of the continuous variable on average different?
    If this is zero then the average is the same over all categories so there is no association.
    '''
    categories = np.array(df[col1])
    values = np.array(df[col2])
    
    group_variances = 0
    for category in set(categories):
        group = values[np.where(categories == category)[0]]
        group_variances += len(group)*(np.mean(group)-np.mean(values))**2
    total_variance = sum((values-np.mean(values))**2)

    return (group_variances / total_variance)**.5

def plot_mix_corr_matrix(df):
    '''
    plot a correlation matrix for the categorical and continuous features in the dataset
    '''
    disc_feats = [feat for feat in df.columns if type(df.iloc[0, df.columns.get_loc(feat)]) == str]
    cont_feats = [feat for feat in df.columns if type(df.iloc[0, df.columns.get_loc(feat)]) != str]
    
    corr = np.zeros((len(disc_feats), len(cont_feats)))
    for i in range(len(disc_feats)):
        for j in range(len(cont_feats)):
            corr[i, j] = correlation_ratio(df, disc_feats[i], cont_feats[j])
    
    # now plot the correlation matrix
    fig, ax = plt.subplots(figsize=(10, 10))
    for i in range(len(corr)):
        for j in range(len(corr)):
             ax.text(j, i, '{:.2f}'.format(corr[i, j]), ha="center", va="center", color="w")
    ax.matshow(corr, cmap='bwr')
    plt.xticks(range(len(corr)), cont_feats, rotation=90)
    plt.yticks(range(len(corr)), disc_feats)
    plt.show()

def read_sample(path):
    '''
    A read_sample function for when the model is to be evaluated
    '''
    pass
