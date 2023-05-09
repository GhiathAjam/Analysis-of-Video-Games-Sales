import matplotlib.pyplot as plt
import seaborn as sns

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

    for i in range(0, 16, 4):
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15,5))

        column1 = df.iloc[:, i]
        column2 = df.iloc[:, i+1]

        top_15_1 = column1.value_counts().nlargest(15)
        top_15_2 = column2.value_counts().nlargest(15)

        data1 = column1.where(column1.isin(top_15_1.index), 'Other').astype(str)
        data2 = column2.where(column2.isin(top_15_2.index), 'Other').astype(str)

        #plot histogram for each column
        data1.value_counts().plot(kind='bar', ax=axes[0], title=column1.name)
        data2.value_counts().plot(kind='bar', ax=axes[1], title=column2.name)

      
        # add xticks and xlabels
        axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=45, ha='right')
        axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45, ha='right')

        # add title for each figure 
        axes[0].set_title(column1.name)
        axes[1].set_title(column2.name)
     
    plt.show()

def plot_corr_matrix(df):
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