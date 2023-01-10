import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

"""
836. Rectangle Overlap
https://leetcode.com/problems/rectangle-overlap/
"""

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    # TODO - you fill in here.
    def is_intersectw(r1, r2):
        return (r1.x <= r2.x + r2.width and r1.x + r1.width >= r2.x#checking if the intervals overlap
                and r1.y <= r2.y + r2.height and r1.y + r1.height >= r2.y)
    #both are right, demorgan
    def is_intersect(r1, r2):
        return not ((r1.x > r2.x + r2.width or r1.x + r1.width < r2.x)#checking if the intervals overlap
                or (r1.y > r2.y + r2.height or r1.y + r1.height < r2.y))

    if not is_intersect(r1, r2):
        return Rect(0, 0, -1, -1)  # No intersection.
    #The width is positive when min(rec1[2], rec2[2]) > max(rec1[0], rec2[0]), that is when the smaller of
    # (the largest x-coordinates) is larger than the larger of (the smallest x-coordinates). The height is similar.
    return Rect(max(r1.x, r2.x), max(r1.y, r2.y),
                min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x),
                min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y))


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('4-11-rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
