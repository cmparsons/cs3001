import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


def main():
    # Manually specify category types for pandas. Everything else will be interpreted like it should
    category_dtypes = {
        'Survived': pd.api.types.CategoricalDtype(categories=[0, 1]),
        'Pclass': pd.api.types.CategoricalDtype(categories=[1, 2, 3]),
        'Sex': 'category',
        'Cabin': 'category',
        'Embarked': 'category',
    }

    train_df = pd.read_csv('hw2/input/train.csv', dtype=category_dtypes)
    test_df = pd.read_csv('hw2/input/test.csv', dtype=category_dtypes)
    combined = [train_df, test_df]
    combined_df = pd.concat(combined, sort=False)

    print(task_5(train_df))
    print(task_7(train_df))
    print(task_8(train_df))
    print(task_9(train_df))
    print(task_10(train_df))
    task_11(train_df)
    task_12(train_df)
    task_13(train_df)
    print(task_14(train_df))
    print(task_15(combined_df))
    print(task_16(combined_df))
    print(task_17(combined_df))
    print(task_18(train_df))
    print(task_19(test_df))
    print(task_20(combined_df))


def task_5(df):
    """Find features with missing values"""
    return [col for col in df.columns if df[col].isnull().any()]


def task_7(df):
    """Get summary statistics for numerical features"""
    return df[['Age', 'SibSp', 'Parch', 'Fare']].describe()


def task_8(df):
    """Get summary statistics for categorical features"""
    return df[['Survived', 'Pclass', 'Sex', 'Cabin', 'Embarked']].describe()


def task_9(df):
    """Determine correlation between Pclass=1 and Survived"""
    pclass_survival_results = {}

    for pclass in df['Pclass'].cat.categories:
        pclass_data = df[df['Pclass'] == pclass]
        pclass_survival_results[pclass] = len(
            pclass_data[pclass_data['Survived'] == 1]) / len(pclass_data)

    return pclass_survival_results


def task_10(df):
    """Determine correlation between Sex=female and Survived"""
    female_data = df[df['Sex'] == 'female']
    return len(female_data[female_data['Survived'] == 1]) / len(female_data)


def task_11(df):
    """Plot histograms to visual Age vs (not) Survived correlation"""

    sub_df = df[df['Age'].notnull()]
    survived_df = sub_df[sub_df['Survived'] == 1]['Age']
    not_survived_df = sub_df[sub_df['Survived'] == 0]['Age']

    fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

    survived_df.plot(
        kind='hist', ax=axs[0], bins=40, grid=False, title='Survived = 1')
    not_survived_df.plot(
        kind='hist', ax=axs[1], bins=40, grid=False, title='Survived = 0')

    fig.savefig('hw2/plots/task11.png')


def task_12(df):
    """Plot histograms to visualize age, Pclass, and survived correlation"""
    sub_df = df[df['Age'].notnull()]
    sub_df = df[['Age', 'Pclass', 'Survived']]

    fig, axs = plt.subplots(3, 2, sharey=True, sharex=True)

    for i, pclass in enumerate(sub_df['Pclass'].cat.categories):
        for j, survived in enumerate(sub_df['Survived'].cat.categories):
            # Query for rows that match the pclass and survived values and plot histogram based on age
            sub_df[(sub_df['Pclass'] == pclass) & (
                sub_df['Survived'] == survived)]['Age'].plot(
                    kind='hist',
                    ax=axs[i, j],
                    bins=40,
                    grid=False,
                    title='Pclass = {} | Survived = {}'.format(pclass, survived))

    fig.savefig('hw2/plots/task12.png')


def task_13(df):
    """Plot to visualize correlation between categorical and numerical features
    - Embarked
    - Survived
    - Fare
    - Sex
    """
    fig, axs = plt.subplots(3, 2, sharey=True, sharex=True)

    sub_df = df[['Age', 'Fare', 'Sex', 'Embarked', 'Survived']]

    plt.ylabel('Fare')
    for i, embarked in enumerate(sub_df['Embarked'].cat.categories):
        for j, survived in enumerate(sub_df['Survived'].cat.categories):
            # Query for rows based on embarked and survived values. Group by sex and plot a bar chart for the mean fare for each sex
            sub_df[(sub_df['Embarked'] == embarked) & (sub_df['Survived'] == survived)].groupby(
                ['Sex'])['Fare'].mean().plot(
                    x='Sex',
                    y='Fare',
                    ax=axs[i, j],
                    grid=False,
                    kind='bar',
                    title='Embarked = {} | Survived = {}'.format(embarked, survived))

    fig.savefig('hw2/plots/task13.png')


def task_14(df):
    """Determine rate of duplicates for Tickets and correlation between Ticket and survival"""
    return 1 - df['Ticket'].nunique() / len(df['Ticket'].dropna())


def task_15(df):
    """Count all missing Cabin values"""
    return df['Cabin'].isnull().sum(), df['Cabin'].isnull().sum() / len(df['Cabin'])


def task_16(df):
    """Replace all male and female values with 0 and 1, respectively. Convert column to Gender"""
    df['Sex'].cat.rename_categories(
        [1 if sex == 'female' else 0 for sex in df['Sex'].cat.categories], inplace=True)
    df.rename(index=str, columns={'Sex': 'Gender'}, inplace=True)
    return df


def task_17(df):
    """Replace all missing values in Ages with random values between mean and standard deviation"""
    age_std = int(df['Age'].std())
    age_mean = int(df['Age'].mean())

    low = age_std if age_std < age_mean else age_mean
    high = age_std if age_std >= age_mean else age_mean

    df['Age'].fillna(random.randrange(low, high), inplace=True)
    return df


def task_18(df):
    """Replace all missing values in Embarked with most frequent occurrence (mode)"""
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    return df


def task_19(df):
    """Replace missing value in Fare with the mode"""
    df['Fare'].fillna(df['Fare'].mode()[0], inplace=True)
    return df


def task_20(df):
    """Convert Fare to ordinal values based on FareBand feature:
    0 -> (-0.0001, 7.91]
    1 -> (7.91, 14.454]
    2 -> (14.454, 31.0]
    3 -> (31.0, 512.329]
    """
    def get_ordinal_value(fare):
        if fare > 31.0:
            return 3
        elif fare > 14.454:
            return 2
        elif fare > 7.91:
            return 1
        else:
            return 0

    df['Fare'] = df['Fare'].apply(get_ordinal_value)
    return df


if __name__ == "__main__":
    main()
