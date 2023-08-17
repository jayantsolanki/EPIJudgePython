import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


"""
#Counting Sort, Important
You are given an array of student objects. Each student has an integer -valued age field that is to be treated as a key.
Rearrange the elements of the array, so that student with same age appear together. The order of ages dont matter. 
How would your solution change if agges have to be appear in sorted order?
Logic:
    Space not a constraint, then use a hashmap to find the count and then create another the hash map to store the offsets of the index where
    each distinct age student will belong. For example, if age 21 appears 2 times, and age 19 appears 3 times in total array of 5,
    then hash map have offset 0 for age 21, and offset 2 for age 19. So on. Then again scan the array and place each student by the age in
    new array based on the offset.

    If to update the array in place, follow below
    Maintain a subarray for each different types of elements. Each subarray marks out entries which have not been 
    assigned elements of that type. We keep on swapping elements across these subarrays to move them to their correct positions then move to next.
    USe two hastables to track subarrays. one for offsets, other for its size. As soon as subarray is empty, we remove it.
    Key is that we swap
    Tldr: get the first age key from offset hash,, find the index(from_idx) where it should have belonged, then get the actual element
    currently present there, find its index(to_idx) where it should have actually belonged, now swap the elements at those two indices
    , update the counter and offset hash maps for element at to_idx

If not sorted:
    Time: O(n), has tables O(m), m is distinct ages
    If ordered required, use BST, Chapter 14, Time O(n + mlogm). Use BST for mapping ages to counts. Then process it
"""

Person = collections.namedtuple('Person', ('age', 'name'))


def group_by_age(people: List[Person]) -> None:

    age_to_count = collections.Counter((person.age for person in people))#first hashmap for counting
    age_to_offset, offset = {}, 0
    for age, count in age_to_count.items():#creating offsets
        age_to_offset[age] = offset
        offset += count
    while age_to_offset:#complete all the offsets
        from_age = next(iter(age_to_offset))# this keeps on returning the same first value until it is deleted in the last line, 
        # then it return next first value
        # print(from_age)
        from_idx = age_to_offset[from_age] #find the index where from_age should have belonged in ordered result
        to_age = people[from_idx].age # get the actual element currently present there
        # to_idx = age_to_offset[people[from_idx].age]  # this also correct
        to_idx = age_to_offset[to_age]#find correct index for to_age in the ordered result
        people[from_idx], people[to_idx] = people[to_idx], people[from_idx] #now swap
        # Use age_to_count to see when we are finished with a particular age.
        age_to_count[to_age] -= 1
        if age_to_count[to_age]:
            age_to_offset[to_age] = to_idx + 1
        else:
            del age_to_offset[to_age]
        #why below is wrong, we dont know if from_age is still at correct location, since the element we picked from to_idx
        #may not be the element with age == from_age, but we are sure that element we pciked from from_idx can be moved to correct idx (to_idx). Hence we update counter and offset for to_age
        # age_to_count[from_age] -= 1
        # if age_to_count[from_age]:
        #     age_to_offset[from_age] = from_idx + 1
        # else:
        #     del age_to_offset[from_age]

# people = [[13, "Oliver"], [4, "Quincy"], [10, "Bob"], [27, "Quincy"], [11, "Sam"], [11, "Frank"], [15, "Mary"], [3, "Thomas"], [28, "William"], [26, "Adam"], [19, "Mary"], [14, "Vincent"], [29, "Harry"], [31, "Sam"], [9, "Vincent"], [5, "Vincent"], [11, "Vincent"], [20, "David"], [26, "Nancy"], [22, "William"], [8, "Adam"], [8, "Quincy"], [9, "Sam"], [5, "Thomas"], [13, "Quincy"], [11, "Eddie"], [20, "Adam"], [1, "Sam"], [27, "Zachary"], [19, "Bob"], [2, "Zachary"], [30, "Frank"], [3, "Quincy"], [17, "Peter"], [12, "Ike"], [24, "Xavier"], [5, "Harry"], [19, 
# "Xavier"], [13, "Yogi"], [3, "Frank"], [30, "Eddie"], [1, "Thomas"], [29, "Thomas"], [19, "Larry"], [9, "Harry"], [10, "Ike"], [3, "Sam"], [24, "Vincent"], [2, "Roger"], [6, "David"], [10, "Jim"], [1, "Xavier"], [11, "Mary"], [6, "Oliver"], [21, "Nancy"], [31, "Zachary"], [16, "Peter"], [31, "Larry"], [4, "Oliver"], [2, "Kenny"], [29, "William"], [31, "David"], [17, "Ike"], [1, "Ike"], [18, "Thomas"], [19, "Xavier"], [31, "Zachary"], [7, "Roger"], [14, "Ike"], [18, "Adam"], [30, "Nancy"], [1, "Mary"], [30, "Adam"], [16, "Sam"], [22, "Thomas"], [3, "Kenny"], [15, "Ike"], [4, "Nancy"], [15, "Yogi"], [9, "Quincy"], [18, "Sam"], [22, "Roger"], [1, "Jim"], [2, "William"], [3, "Harry"], [19, "Adam"], [24, "Quincy"], [30, "Peter"], [24, "Quincy"], [27, "Ike"], [4, "Nancy"], [27, "Bob"], [13, "Oliver"], [11, "Vincent"], [20, "Mary"], [31, "Harry"], [14, "Larry"], [5, "Peter"], [17, "Sam"], [7, "Larry"], [2, "Quincy"], [30, "Ike"], [16, "Adam"], [8, "Peter"], [10, 
# "David"], [19, "Mary"], [13, "Jim"], [29, "Peter"], [14, "David"], [13, "Carol"], [12, "Thomas"], [19, "Adam"], [12, "Mary"], [1, "Ike"], [28, "Nancy"], [17, "Frank"], [19, "Bob"], [11, "Uncle"], [25, "Roger"], [5, "Harry"], [16, "Zachary"], [15, "Peter"], [18, "Zachary"], [26, "Yogi"], [31, "Vincent"], [14, "Mary"], [23, "Sam"], [12, "Larry"], [6, "Peter"], [18, "Mary"], [2, "David"], [28, "Nancy"], [5, "Thomas"], [11, "Vincent"], [16, "Bob"], [26, "Frank"], [12, "Roger"], [5, "Roger"], [27, "Quincy"], [25, "Oliver"], [17, "Xavier"], [23, "Nancy"], [16, "Bob"], [9, "Uncle"], [10, "Uncle"], [16, "Larry"], [13, "Kenny"], [16, "Frank"], [17, "Carol"], [12, "Nancy"], [27, "Bob"], [23, "Adam"], [14, "Yogi"], [16, "Bob"], [19, "David"], [12, "Larry"], [15, "Bob"], [9, "Eddie"], [24, "Carol"], [9, "Ike"], [7, "George"], [11, "Larry"], [1, "Roger"], [14, "Zachary"], [4, "Vincent"], [16, "Quincy"], [13, "Eddie"], [2, "Jim"], [16, "Jim"], [28, "Vincent"], [13, "Bob"], [16, "Quincy"], [29, "David"], [17, "Kenny"], [12, "Roger"], [28, "Uncle"], [29, "Nancy"], [6, "Roger"], [15, "Roger"]]
# people = [Person(*x) for x in people]
# group_by_age(people)

@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure('Empty result')

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure('Entry set changed')

    ages = set()
    last_age = people[0].age

    for x in people:
        if x.age in ages:
            raise TestFailure('Entries are not grouped by age')
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('13-09-group_equal_entries.py',
                                       'group_equal_entries.tsv',
                                       group_by_age_wrapper))
