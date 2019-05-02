import os
from file_path import ICD9_description, ICD9_data_2017, ICD9_data_2018, ICD10_description,cleaned_data_folder
from data_clean_compare import check_icd_with_previous_year, generic_clean_2018_data


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


def updated_icd9_list():
    updated_df = check_icd_with_previous_year(clean9_2018_data(), ICD9_data_2017, column='ICD9')
    updated_df = updated_df[['ICD9', 'ICD9_Desc',
                             'ICD10', 'ICD10_Desc',
                             'APPROX', 'NOMAP',
                             'COMBO', 'SCENARIO',
                             'CHOICE', 'Obsolete'
                             ]]
    updated_df['Icd_type'] = 'I9'

    path = os.path.join(cleaned_data_folder, "ICD9_updated_data.csv")
    updated_df.to_csv(path, index=False)
    return "Created CSV file successfully"
    # return updated_df


if __name__ == '__main__':
    print(updated_icd9_list())
