from test_framework import generic_test

"""
Implement a function that converts a spreadsheet column id to the corresponding integer, with 'A' corresponding to 1. For example, you should retum 4 for "D", 27 for "AN", 702 for "ZZ" , etc. How would you test your code?
The time complexity is O(n)
"""
def ss_decode_col_id_v1(col: str) -> int:
    # TODO - you fill in here.
    num = 0
    for s in col:
        num = 26 * num + ord(s) - ord('A') + 1
    return num

def ss_decode_col_id(col: str) -> int:
    # TODO - you fill in here.
    power = 1
    num = 0
    for i in range(len(col) -1, -1, -1):
        num += power * (ord(col[i]) - ord('A') + 1) #similar to binary to decimal conversion
        power *= 26
    return num


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('6-03-spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
