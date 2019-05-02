import numpy as np
import pandas as pd
from multiprocessing import cpu_count, Pool

from pandas.util.testing import assert_frame_equal

pd.options.mode.chained_assignment = None # warning disable

from dot_function import addDot_icd9, addDot_icd10


num_partitions = 10
num_cores = 4



from file_path import ICD9_description, ICD9_data_2017, ICD9_data_2018, ICD10_description


def clean9_2018_data():
    df = generic_clean_2018_data(ICD_data=ICD9_data_2018, I9_desc=ICD9_description,
                                 I10_desc=ICD10_description, column1='ICD9',
                                 column2='ICD10')

    df = df[['ICD9', 'ICD9_Desc',
             'ICD10', 'ICD10_Desc',
             'APPROX', 'NOMAP',
             'COMBO', 'SCENARIO',
             'CHOICE', 'Obsolete'
             ]]
    return df




def hello(data):
    data['ICD9'] = data['ICD9'].map(lambda x: addDot_icd9(x))
    data['ICD10'] = data['ICD10'].map(lambda x: addDot_icd10(x))
    return data


def parallelize_dataframe(df, func):
    df_split = np.array_split(df, num_partitions)
    pool = Pool(processes=num_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df


def generic_clean_2018_data(ICD_data=None, I9_desc=None, I10_desc=None, column1 = None, column2 = None):

    df = pd.read_csv(ICD_data,
					names = [column1, column2, "unwanted"],
					dtype={'unwanted': object} )
    description9 = pd.read_excel(I9_desc, names=['ICD9', 'Long_text_9', 'Short_text_9'])
    description10 = pd.read_csv(I10_desc, dtype={'ICD9': object}, names=['ICD9_c', 'ICD10', 'unknown', 'Short_text', 'Long_text' ])

    df = df.merge(description9, on='ICD9', how='left')
    df = df.merge(description10, on='ICD10', how='left')
    # df = parallelize_dataframe(df, hello)
    df['APPROX'] = df['unwanted'].str[0]
    df['NOMAP'] = df['unwanted'].str[1]
    df['COMBO'] = df['unwanted'].str[2]
    df['SCENARIO'] = df['unwanted'].str[3]
    df['CHOICE'] = df['unwanted'].str[4]
    df['Obsolete'] = 0
    df['ICD9_Desc'] = df['Short_text_9']
    df['ICD10_Desc'] = df['Short_text']

    df = parallelize_dataframe(df, hello)
    # df['ICD9'] = df.ICD9.map(lambda x: addDot_icd9(x))
    # df = hello(df)
    # df['ICD9'], df['ICD10'] = parallelize_dataframe(df, hello)
    # df['ICD10'] = df.ICD10.map(lambda x: addDot_icd10(x))
    # df['ICD9'] = parallelize_dataframe(df, df.ICD10.map(lambda x: addDot_icd10(x)))

    return df

if __name__ == '__main__':
    import time
    start = time.time()
    print(clean9_2018_data())
    end = time.time()
    print(end-start)