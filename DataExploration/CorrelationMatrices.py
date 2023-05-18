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
    ax.matshow(corr, cmap='Blues')
    plt.xticks(range(len(corr)), disc_feats, rotation=90)
    plt.yticks(range(len(corr)), disc_feats)
    plt.show()
    
