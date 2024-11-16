# Solution code for the Iris Dataset Homework (run.py)

import pandas as pd
from scipy.stats import zscore

# Question 1: Pre-process the data
def preprocess_data(input_filename) -> dict:

    df = pd.read_csv(input_filename)
    df.columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
    df['SepalLengthCm_z'] = zscore(df['SepalLengthCm'])
    df['SepalWidthCm_z'] = zscore(df['SepalWidthCm'])
    df_clear = df[
        (df['SepalLengthCm_z'] > -2) & (df['SepalLengthCm_z'] < 2) &
        (df['SepalWidthCm_z'] > -2) & (df['SepalWidthCm_z'] < 2)
    ]
    df_clear = df_clear.reset_index(drop=True)
    df_clear['ID'] = range(1, len(df_clear) + 1)

    return df_clear

#print(preprocess_data("iris.data"))


# Question 2: Descriptive Statistics Functions
def species_count(data) -> dict:
    return (preprocess_data(data)['Species'].value_counts()).to_dict()


#print(species_count("iris.data"))
def average_sepal_length(data) -> float:
    return round(preprocess_data(data)['SepalLengthCm'].mean(),1)


#print(average_sepal_length("iris.data"))
def max_petal_width(data):
    return round(preprocess_data(data)['PetalWidthCm'].max(),1)

#print(max_petal_width('iris.data'))
def min_petal_length(data) -> float:
    return round(preprocess_data(data)['PetalLengthCm'].min(),1)

#print(min_petal_length('iris.data'))

def count_sepal_length_above_5(data) -> int:
    df = preprocess_data(data)
    return len(df[df['SepalLengthCm'] > 5])

#print(count_sepal_length_above_5('iris.data'))

# Question 3: Analysis Functions
def count_petal_length_below_2(data) -> int:
    df = preprocess_data(data)
    return len(df[df['PetalLengthCm'] < 2])
#print(count_petal_length_below_2('iris.data'))

def get_sepal_width_above_3_5(data) -> list:
    df = preprocess_data(data)
    df = df[df['SepalWidthCm'] > 3.5]

    ids = df['ID'].tolist()

    return ids
#print(get_sepal_width_above_3_5('iris.data'))
def species_count_petal_width_above_1_5(data) -> dict:
    df = preprocess_data(data)
    return df[df['PetalWidthCm'] > 1.5]['Species'].value_counts().to_dict()

#print(species_count_petal_width_above_1_5('iris.data'))

def get_virginica_petal_length_above_6(data) -> list:
    df = preprocess_data(data)
    df = df[df['PetalLengthCm'] > 6]
    ids = df['ID'].tolist()
    return ids
#print(get_virginica_petal_length_above_6('iris.data'))

    
def get_largest_sepal_width(data):
    df = preprocess_data(data)
    max_value = df['SepalWidthCm'].max()
    max_value_row = df[df['SepalWidthCm'] == max_value]
    first_id_value = max_value_row.iloc[0]['ID']
    return first_id_value

print(get_largest_sepal_width('iris.data'))




