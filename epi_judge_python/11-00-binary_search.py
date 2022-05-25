#binary search
import bisect
from typing import List
import collections
def binarySearch(t: int, A: List[int]) -> int:
    left, mid, right = 0, 0, len(A) - 1

    while left <= right:#equal to sign important
        mid = left + (right - left)//2 # instead of (left + right)//2, prevents overflow
        print('i ran', mid)
        if A[mid] == t:
            return mid
        elif A[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
    return - 1

binarySearch(10, [1, 3, 5, 7, 9, 10, 11, 13, 15])

#custom search based on binary search, using custom comparator

Student = collections.namedtuple('Student', ('name', 'grade_point_average'))

def comp_gpa(student):# custom comparator
    return (-student.grade_point_average, student.name)#minus sign, because list is in descending order, hence we need to convert
    # it into ascending order

def search_student(students: List[Student], target: Student):#tuples can be also sorted, they are compared lexigraphically
    # This function returns the position in the sorted list, where the number passed in argument can be placed 
    # so as to maintain the resultant list in sorted order. If the element is already present in the list, 
    # the left most position where element has to be inserted is returned.
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))#returns the position where the target can be inserted
    print(i)
    return 0 <= i < len(students) and students[i] == target#bisectleft suggest index to the left <= element, hence
    #student[i] should match it

data = [Student('a', 10), Student('b', 9), Student('c', 8), Student('d', 8), Student('e', 8), Student('f', 5), Student('g', 4), Student('h', 2)]
search_student(data, Student('c', 8))