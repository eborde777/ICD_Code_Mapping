import re
import pandas as pd
import os
import time

from icd_walk.file_path import cleaned_data_folder


def icd9to10_mapping(code):
    file_name = os.path.join(cleaned_data_folder, 'ICD9_updated_data.csv')
    df = pd.read_csv(file_name)
    ICD9 = df[df['ICD9'].isin(code)]
    z1 = list(ICD9['ICD10'])
    return z1, ICD9  # returning column list and DataFrame


def icd10to9_mapping(code):
    file_name = os.path.join(cleaned_data_folder, 'ICD10_updated_data.csv')
    df = pd.read_csv(file_name)
    ICD10 = df[df['ICD10'].isin(code)]
    z = list(ICD10['ICD9'])
    return z, ICD10  # returning column list and DataFrame


def identify_icd(code):
    ICD9_list = []
    ICD10_list = []
    for i in code:
        alnum = re.search('[a-zA-Z]+', i)
        if alnum:

            if i.startswith('E') and len(i) == 6:
                ICD9_list.append(i)

            elif i.startswith('V') and i.endswith('A') or i.endswith('D') or i.endswith('S'):
                ICD10_list.append(i)

            ICD10_list.append(i)

        else:
            ICD9_list.append(i)

    return ICD9_list, ICD10_list


def check_back_forth(code):
    I9 = I10 = []

    ICD9_list, ICD10_list = identify_icd(code)

    if ICD9_list:
        I9, _na = icd9to10_mapping(ICD9_list)

    if ICD10_list:
        I10, _na = icd10to9_mapping(ICD10_list)

    ii9, _na = icd10to9_mapping(I9)
    ii10, _na = icd9to10_mapping(I10)

    y = list(set(ICD9_list + ICD10_list))

    x = list(set(ii9 + ii10))

    if sorted(x) == sorted(y):
        return final_df(x)
    else:
        return check_back_forth(x)


def final_df(lst):
    ICD9_list, ICD10_list = identify_icd(lst)

    _na, I9 = icd9to10_mapping(ICD9_list)
    _na, I10 = icd10to9_mapping(ICD10_list)

    I9 = I9[['ICD9', 'ICD9_Desc', 'ICD10', 'ICD10_Desc', 'Icd_type']]
    I10 = I10[['ICD10', 'ICD10_Desc', 'ICD9', 'ICD9_Desc', 'Icd_type']]

    I9.columns = ['code', 'code_desc', 'mapped_code', 'mapped_code_desc', 'Icd_type']
    I10.columns = ['code', 'code_desc', 'mapped_code', 'mapped_code_desc', 'Icd_type']

    I9.reset_index(drop=True, inplace=True)
    I10.reset_index(drop=True, inplace=True)

    final = I9.append(I10)

    return final.to_json(orient='records')


if __name__ == "__main__":
    code = input("Insert ICD code: ")
    start = time.time()
    code = list(set(code.strip('').split(',')))
    print(check_back_forth(code))
    end = time.time()
