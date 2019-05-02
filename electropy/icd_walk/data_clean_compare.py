import pandas as pd
from pandas.util.testing import assert_frame_equal

pd.options.mode.chained_assignment = None  # warning disable

from dot_function import addDot_icd9, addDot_icd10


# from multitasking import parallelize_dataframe, hello


def generic_clean_2018_data(ICD_data=None, I9_desc=None, I10_desc=None, column1=None, column2=None):
    df = pd.read_csv(ICD_data,
                     names=[column1, column2, "unwanted"],
                     dtype={'unwanted': object})
    description9 = pd.read_excel(I9_desc, names=['ICD9', 'Long_text_9', 'Short_text_9'])
    description10 = pd.read_csv(I10_desc, dtype={'ICD9': object},
                                names=['ICD9_c', 'ICD10', 'unknown', 'Short_text', 'Long_text'])

    df = df.merge(description9, on='ICD9', how='left')
    df = df.merge(description10, on='ICD10', how='left')

    df['APPROX'] = df['unwanted'].str[0]
    df['NOMAP'] = df['unwanted'].str[1]
    df['COMBO'] = df['unwanted'].str[2]
    df['SCENARIO'] = df['unwanted'].str[3]
    df['CHOICE'] = df['unwanted'].str[4]
    df['Obsolete'] = 0
    df['ICD9_Desc'] = df['Short_text_9']
    df['ICD10_Desc'] = df['Short_text']
    df['ICD9'] = df.ICD9.map(lambda x: addDot_icd9(x))
    df['ICD10'] = df.ICD10.map(lambda x: addDot_icd10(x))

    return df


def check_icd_with_previous_year(new_data=None, old_data=None, column=None):
    if new_data is None:
        return 0

    else:
        old_icd_data = pd.read_csv(old_data, sep=',')
        try:
            assert_frame_equal(old_icd_data, new_data)
            return "Both Frames are Identical"
        except:
            # ICD codes that are not in new data
            icd_not_in_new_df = old_icd_data[~old_icd_data[column].isin(new_data[column])]
            icd_not_in_new_df['Obsolete'] = 1
            if icd_not_in_new_df.empty:
                print("New " + column + " list has all old " + column + " codes in it !")
                return new_data
            else:
                updated_df = new_data.append(icd_not_in_new_df, ignore_index=True)
                return updated_df
