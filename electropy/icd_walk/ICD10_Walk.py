import os
import pandas as pd
from file_path import ICD9_description, ICD10_data_2017, ICD10_data_2018, ICD10_description, cleaned_data_folder
from data_clean_compare import check_icd_with_previous_year, generic_clean_2018_data


def clean10_2018_data():
    df = generic_clean_2018_data(ICD_data=ICD10_data_2018, I9_desc=ICD9_description,
                                 I10_desc=ICD10_description, column1='ICD10',
                                 column2='ICD9')

    df = df[['ICD10', 'ICD10_Desc',
             'ICD9', 'ICD9_Desc',
             'APPROX', 'NOMAP',
             'COMBO', 'SCENARIO',
             'CHOICE', 'Obsolete'
             ]]

    # dff.fillna(dff.mean())
    return df


def updated_icd10_list():
    updated_df = check_icd_with_previous_year(clean10_2018_data(), ICD10_data_2017, column='ICD10')
    updated_df = updated_df[['ICD10', 'ICD10_Desc',
                             'ICD9', 'ICD9_Desc',
                             'APPROX', 'NOMAP',
                             'COMBO', 'SCENARIO',
                             'CHOICE', 'Obsolete'
                             ]]
    updated_df['Icd_type'] = "I10"
    path = os.path.join(cleaned_data_folder, "ICD10_updated_data.csv")
    updated_df.to_csv(path, index=False)
    return "Created CSV file successfully"
    # return updated_df


if __name__ == '__main__':
    print(updated_icd10_list())
    print("CSV file created successfully")
