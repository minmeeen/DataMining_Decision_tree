import numpy as np
import pandas as pd

#Preprocessing data
def preprocessing(dataset):
    #checking
    #What attribute have missing values?
    for i in dataset.columns:
        print(dataset[i].unique())      #print only unique value. 

    dataset = dataset.replace('?',np.nan)   #replace ? in dataset with NaN

    #function to fill missing value
    #If type is numeric
    def fix_missing_mean(dataset,col):
        #replace missing values with mean in this attribute
        dataset[col] = pd.to_numeric(dataset[col], errors = 'coerce')
        dataset[col].fillna(dataset[col].mean(), inplace = True)    

    #If type is object
    def fix_missing_ffill(dataset, col):
        #replace missing values with value from next instance  
        dataset[col] = dataset[col].fillna(method='ffill')  

    #fill missing value by column
    fix_missing_ffill(dataset,'A1')
    fix_missing_ffill(dataset,'A2')
    fix_missing_ffill(dataset,'A4')
    fix_missing_ffill(dataset,'A5')
    fix_missing_ffill(dataset,'A6')
    fix_missing_ffill(dataset,'A7')
    fix_missing_ffill(dataset,'A14')

    # checking
    # Are missing values still available?
    for i in dataset.columns:
        print(dataset[i].unique())      #print only unique value. If NaN is still available, it will show


    dataset.to_csv('data/preprocessing_crx.csv', index=False, header=False)     #write preprocessing data in csv

    return dataset  #return proprocessing data