#Prepare Telco data using various functions to clean up and section data off 


import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import seaborn as sns

import acquire
import prepare

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

###################### Prepare Telco Data ######################

def prep_telco(df):

    '''Prepares acquired Telco data for exploration'''
    
    # drop column in case it is created in addition to the index
    df =  df.drop(columns=['Unnamed: 0'])

    # drop column using .drop(columns=column_name)
    df = df.drop(columns=['customer_id', 'contract_type_id.1', 'internet_service_type_id.1','payment_type_id.1'])

    #drop duplicates if there are any
    df = df.drop_duplicates()
    
    # remame column using .rename(columns={current_column_name : replacement_column_name})
    #df = df.rename(columns={'col_name':'column'})
    
    # create dummies dataframe using .get_dummies(column_names,not dropping any of the dummy columns)
    features_multi = ['multiple_lines','online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies',
                        'contract_type','internet_service_type','payment_type']
    print(features_multi)

    dummy_df = pd.get_dummies(df, columns=features_multi, drop_first=False)

    print(dummy_df.columns)
    
    # join original df with dummies df using .concat([original_df,dummy_df], join along the index)
    df = pd.concat([df, dummy_df], axis=1)

    # Drop unnecessary columns after creating dummy variables to represent them
    df = df.drop(columns=['multiple_lines','online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies',
                        'contract_type','internet_service_type','payment_type'])


    # encode features that have string values 
    df.replace({'partner':{'Yes':1, 'No':0}}, inplace=True)
    df.replace({'dependents':{'Yes':1, 'No':0}}, inplace=True)
    df.replace({'phone_service':{'Yes':1, 'No':0}}, inplace=True)
    df.replace({'multiple_lines':{'Yes':1, 'No':0}}, inplace=True)
    df.replace({'paperless_billing':{'Yes':1, 'No':0}}, inplace=True)
    df.replace({'churn':{'Yes':1, 'No':0}}, inplace=True)
    df.replace({'gender':{'Male':1, 'Female':0}}, inplace=True)

    #yes_no_features = ['partner','dependents','phone_service','multiple_lines','paperless_billing','churn']

    #encode_columns(['partner','dependents','phone_service','multiple_lines','paperless_billing','churn'], df)  
    #encode_columns(yes_no_features, df) 
    
    return df

###################### Prepare Telco Data With Split ######################

def split_data(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames; stratify on churn.
    return train, validate, test DataFrames.
    '''
    
    # splits df into train_validate and test using train_test_split() stratifying on churn to get an even mix 
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.churn)
    
    # splits train_validate into train and validate using train_test_split() stratifying on churn to get an even mix
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.churn)
    return train, validate, test


def prep_telco_with_split(df):
    '''Prepares acquired Telco data for exploration
    This function take in the Telco data acquired, prepares it for exploration,
    performs a split and stratifies survived column.
    It returns train, validate, and test dfs.'''
    
    # drop column in case it is created in addition to the index
    df =  df. df_telco.drop(columns=['Unnamed: 0'])

    # drop column using .drop(columns=column_name)
    df = df.drop(columns=['customer_id', 'contract_type_id.1', 'internet_service_type_id.1','payment_type_id.1'])

    #drop duplicates if there are any
    df = df.drop_duplicates()
    
    # remame column using .rename(columns={current_column_name : replacement_column_name})
    #df = df.rename(columns={'col_name':'column'})
    
    # create dummies dataframe using .get_dummies(column_name,not dropping any of the dummy columns)
    dummy_df = pd.get_dummies(df['churn'], drop_first=False)
    
    # join original df with dummies df using .concat([original_df,dummy_df], join along the index)
    df = pd.concat([df, dummy_df], axis=1)
    
    # split data into train/validate/test using split_data function
    train, validate, test = split_data(df)
    
    return train, validate, test

#Encoding function for columns with string values of Yes or No
#def  encode_columns(features, df):
 #   for i in features:
  #      df[i] = df[i].map({'Yes':1, 'No':0})
   # return


def impute_mean_age(train, validate, test):
    '''
    This function imputes the mean of the age column for
    observations with missing values.
    Returns transformed train, validate, and test df.
    '''
    # create the imputer object with mean strategy
    imputer = SimpleImputer(strategy = 'mean')
    
    # fit on and transform age column in train
    train['age'] = imputer.fit_transform(train[['age']])
    
    # transform age column in validate
    validate['age'] = imputer.transform(validate[['age']])
    
    # transform age column in test
    test['age'] = imputer.transform(test[['age']])
    
    return train, validate, test