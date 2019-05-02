import sys
from icd_walk.ICD_conversion import check_back_forth


def response():
    input = sys.argv[1]
    code = input.strip('').split(',')
    print(check_back_forth(code))

if __name__ == '__main__':
    response()
