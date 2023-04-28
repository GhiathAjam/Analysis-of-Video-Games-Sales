import matplotlib.pyplot as plt


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

    for i in range(0, 16, 2):
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