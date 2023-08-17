from typing import List

from test_framework import generic_test

"""
Design an algorithm for computing the salary cap. Given that existing salaries and the target payroll (sum of all the salaries)
Logic:
    First sort the array
    Let the salary cap be c and given target payroll be T. Condition is that if any salary is >=  C, that will be capped to c.
    So, for each salary in the sorted salaries, we calculate the total payroll. Then we find those two salaries whose total payroll
    calculation becomes the interval in which T(Target) lies. Then we use the formula to calculate exact c
    Let those two salaries are at K and K + 1. See book for formula C = (T - (A[0] + A[1] ... A[k - 1]))/ (n - k)
    That means C will be =< for values A[k], A[k+1]....A[n-1]. So we calcualte C everytime and check if upcoming A[i] is
    < C 
    Main crux is finding K and K+1 in the loop
Time: O(nlogn)
"""

def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:

    current_salaries.sort()
    unadjusted_salary_sum = 0.0
    #find the first salary which makes the total payroll surpass target_payroll, that salary and heereafter will be capped
    for i, current_salary in enumerate(current_salaries):
        adjusted_people = len(current_salaries) - i #(n - k)
        adjusted_salary_sum = current_salary * adjusted_people #here current salary is being treated as cap
        if unadjusted_salary_sum + adjusted_salary_sum >= target_payroll:#find the first total payroll which exceeds the target
            return (target_payroll - unadjusted_salary_sum) / adjusted_people
        unadjusted_salary_sum += current_salary
    # No solution, since target_payroll > existing payroll.
    return -1.0

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('13-12-find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
