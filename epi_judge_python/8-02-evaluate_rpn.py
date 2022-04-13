from test_framework import generic_test


def evaluate(expression: str) -> int:
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('8-02-evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
