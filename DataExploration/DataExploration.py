import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plott_missing_values(df):
    '''
    Get the number of missing values in each column 
    '''
    plt.title('Missing values')
    plt.xlabel('Features')
    plt.ylabel('Number of missing values')
    df.isna().sum().plot(kind='bar')
    plt.show()

def plot_hist(df):
    '''
    Plot a histogram for the top 15 values in each column
    '''

    for i in range(8):
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        for j, col in enumerate(df.columns[i*2:(i+1)*2]):
            # plot the histogram
            df[col].value_counts().head(15).plot(kind='bar', ax=axes[j])
            axes[j].set_title(col)
            axes[j].tick_params(labelrotation=90)
    plt.show()

def show_nulls(df):
    '''
    Show the percentage of missing values in each column
    '''
    null_data = (df.isnull().sum() / len(df)) * 100
    null_data = null_data.drop(null_data[null_data == 0].index).sort_values(ascending=False)[:30]
    missing_data = pd.DataFrame({'Missing Ratio' :null_data})
    return missing_data

def show_unique(df):
    '''
    Show the number of unique values in each column
    '''
    unique_data = df.nunique().sort_values(ascending=False)[:30]
    unique_data = pd.DataFrame({'#Unique Values' :unique_data})
    return unique_data

def plt_hist(col, title,df,color='blue'):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.histplot(df[col], color=color, kde=True, bins=25)
    plt.title(title, fontsize=18, y=1.02)
    ax.set_xlabel(col,fontsize=15)

def count_plot(col,df, title=''):
    # plot the distribution of ratings
    plt.figure(figsize=(6,4))
    sns.countplot(x=col, data=df)
    plt.title(title)
    plt.show()

def sub_plots(df, cat_col, grouby_col, col, title="",plot_kind='bar',figsize=(20, 10)):
    fig, axes = plt.subplots(3, 4, figsize=figsize)
    for i, (genre, ax) in enumerate(zip(df[cat_col].unique(), axes.flatten())):
        df_genre = df[df[cat_col] == genre]
        publisher_sales = df_genre.groupby(grouby_col)[col].mean().sort_values(ascending=False).head(10)
        publisher_sales.plot(kind=plot_kind, ax=ax, title=genre)
    plt.tight_layout()
    plt.show()

