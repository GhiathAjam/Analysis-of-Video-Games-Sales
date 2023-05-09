import pandas as pd
import matplotlib.pyplot as plt

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
    if method == 'frequency':
        for col in df.columns:
                if col in [ 'Publisher', 'Developer', 'Platform', 'Genre','Rating']:
                    df[col] = df[col].map(df[col].value_counts())/len(df)
    return df


     
