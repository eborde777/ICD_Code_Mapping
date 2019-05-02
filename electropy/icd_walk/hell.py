import sys

from ICD_conversion import check_back_forth

def mylines():
    # for v in sys.argv[1:]:
    #     code = v.strip('').split(',')
    #     for i in code:
    #         print(i)
    print(check_back_forth(['796.0']))
mylines()
