import os
import glob
from os.path import abspath, realpath

BASE_DIR = os.path.dirname(os.getcwd())

# #ICD FOLDERS
# ICD_FILES_FOLDER = os.path.abspath(os.path.join(BASE_DIR, 'icd_files'))
# ICD_9_data_FOLDER = os.path.abspath(os.path.join(ICD_FILES_FOLDER, 'ICD_9_data'))
# ICD_10_data_FOLDER = os.path.abspath(os.path.join(ICD_FILES_FOLDER, 'ICD_10_data'))
#
# #ICD9 files
# ICD9_data_2018 = os.path.abspath(os.path.join(ICD_9_data_FOLDER, '2018_I9_data.csv'))
# ICD9_description = os.path.abspath(os.path.join(ICD_9_data_FOLDER, 'CMS32_DESC_LONG_SHORT_DX.xlsx'))
# ICD9_data_2017 = os.path.abspath(os.path.join(ICD_9_data_FOLDER, 'ICD9_walk_2017.csv'))
#
# # ICD10 files
# ICD10_data_2018 = os.path.abspath(os.path.join(ICD_10_data_FOLDER, '2018_I10gem.csv'))
# ICD10_description = os.path.abspath(os.path.join(ICD_10_data_FOLDER, 'ICD10_walk_2017.csv'))
# ICD10_data_2017 = os.path.abspath(os.path.join(ICD_10_data_FOLDER, 'icd10cm_order_2018.csv'))
#
# #cleaned_data
# cleaned_data_folder = os.path.abspath(os.path.join(ICD_FILES_FOLDER, 'cleaned_data'))



#ICD FOLDERS
ICD_FILES_FOLDER = r'C:\Users\Bordee\Desktop\mysite\electropy\icd_files'
ICD_9_data_FOLDER = r'C:\Users\Bordee\Desktop\mysite\electropy\icd_files\ICD_9_data'
ICD_10_data_FOLDER = r'C:\Users\Bordee\Desktop\mysite\electropy\icd_files\ICD_10_data'
# ALL_FILES_9 = os.listdir(ICD_9_data_FOLDER)
# ALL_FILES_10 = os.listdir(ICD_10_data_FOLDER)

#ICD9 files
ICD9_data_2018 = r'C:\Users\Bordee\Desktop\mysite\electropy\icd_files\ICD_9_data\2018_I9_data.csv'
ICD9_description = r'C:\Users\Bordee\Desktop\mysite\electropy\icd_files\ICD_9_data\CMS32_DESC_LONG_SHORT_DX.xlsx'
ICD9_data_2017 = r'C:\Users\Bordee\Desktop\mysite\electropy\icd_files\ICD_9_data\ICD9_walk_2017.csv'

# ICD10 files
ICD10_data_2018 = r'C:\Users\Bordee\Desktop\mysite\electropy\icd_files\ICD_10_data\2018_I10gem.csv'
ICD10_description = r'C:\Users\Bordee\Desktop\mysite\electropy\icd_files\ICD_10_data\ICD10_walk_2017.csv'
ICD10_data_2017 = r'C:\Users\Bordee\Desktop\mysite\electropy\icd_files\ICD_10_data\icd10cm_order_2018.csv'

#cleaned_data
cleaned_data_folder = r'C:\Users\Bordee\Desktop\mysite\electropy\icd_files\cleaned_data'

# print(os.path.abspath(os.path.join(BASE_DIR, 'icd_files')))