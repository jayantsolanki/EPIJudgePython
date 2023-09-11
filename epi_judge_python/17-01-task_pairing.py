import collections
from typing import List

from test_framework import generic_test

"""
Compute an optimum assignment of tasks
Design an algorithm that takes as input a set of tasks and returns an optimum assignment.
Logic:
    Sort it, and then pair shortest and longest, then second shortest and second longest, and so on.
Time: O(nlogn)
"""
PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))

def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    result = []
    task_durations.sort()
    for i in range(len(task_durations) // 2):
        # result.append(PairedTasks(task_durations[i], task_durations[~i]))
        result.append((task_durations[i], task_durations[~i]))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('17-01-task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))
