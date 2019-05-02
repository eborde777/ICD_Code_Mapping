import pandas as pd


def addDot_icd9(x):
    '''
    ICD9 codes with prefix "E": dots are at index position 4, no dots if length is greater than 4
    ICD9 codes not with prefix "E": dots are at index position 3
    '''
    if (not pd.isnull(x)) and x[0] != 'E':
        if len(x) > 3:
            return str(x[0:3] + '.' + x[3:])
        else:
            return str(x)
    elif pd.isnull(x):
        return str(x)
    else:
        if len(x) == 4:
            return str(x)
        else:
            return str(x[0:4] + '.' + x[4:])


def addDot_icd10(x):
    if not pd.isnull(x) and len(x) > 3:
        return x[0:3] + '.' + x[3:]
    else:
        return x


