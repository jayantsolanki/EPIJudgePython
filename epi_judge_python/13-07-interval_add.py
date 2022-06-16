import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

"""
Write a program which takes as input an array of disjoint closed intervals with integerts endpoints which are sorted by 
increasing order of left endpoint, and an interncval to be added, and returns the union of the intervals in the array 
and the added intervals. Result should be expressed as the unior of disjoint intervals sorted by left endpoint.
Logic:
    Use the sroted proprty of the intervals
    We process the sroted intervals in three stages
    1 - We add those intervals which appear completely before the given disjoint interval, into the result
    2- As soon as we encounter the interval in the array that intersects the interval, compute its union.
        the union itself becomes new interval. We iterate through subsequent intervals, as long they intersect 
        with the union that is being formed. This single union is then added to the result
    3 - Finally, add those remaining intervals into the result

    # https://stackoverflow.com/questions/325933/determine-whether-two-date-ranges-overlap/325964#325964
    (StartA <= EndB) and (EndA >= StartB)

    Proof:
    Let ConditionA Mean that DateRange A Completely After DateRange B

    _                        |---- DateRange A ------|
    |---Date Range B -----|                          _
    (True if StartA > EndB)

    Let ConditionB Mean that DateRange A is Completely Before DateRange B

    |---- DateRange A -----|                        _ 
    _                          |---Date Range B ----|
    (True if EndA < StartB)

    Then Overlap exists if Neither A Nor B is true -
    (If one range is neither completely after the other,
    nor completely before the other, then they must overlap.)

    Now one of De Morgan's laws says that:

    Not (A Or B) <=> Not A And Not B

    Which translates to: (StartA <= EndB)  and  (EndA >= StartB)

Time: O(n)
"""
Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals: List[Interval],
                 new_interval: Interval) -> List[Interval]:

    i, result = 0, []

    # Processes intervals in disjoint_intervals which come before new_interval.
    while (i < len(disjoint_intervals)
           and new_interval.left > disjoint_intervals[i].right): #simple lol
        result.append(disjoint_intervals[i])
        i += 1

    # Processes intervals in disjoint_intervals which overlap with new_interval.
    # https://stackoverflow.com/questions/3269434/whats-the-most-efficient-way-to-test-if-two-ranges-overlap
    # https://stackoverflow.com/questions/325933/determine-whether-two-date-ranges-overlap/325964#325964
    # while (i < len(disjoint_intervals)
    #        and new_interval.right >= disjoint_intervals[i].left):
    while (i < len(disjoint_intervals)
           and new_interval.right >= disjoint_intervals[i].left and disjoint_intervals[i].right >= new_interval.left):
        # If [a, b] and [c, d] overlap, union is [min(a, c), max(b, d)].
        new_interval = Interval(
            min(new_interval.left, disjoint_intervals[i].left),
            max(new_interval.right, disjoint_intervals[i].right))
        i += 1
    # Processes intervals in disjoint_intervals which come after new_interval.
    return result + [new_interval] + disjoint_intervals[i:]


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('13-07-interval_add.py',
                                       'interval_add.tsv',
                                       add_interval_wrapper,
                                       res_printer=res_printer))
