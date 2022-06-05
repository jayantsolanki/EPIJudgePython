from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    # TODO - you fill in here.
    num = 0
    for s in col:
        num = 26 * num + ord(s) - ord('A') + 1
    return num


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('6-03-spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
