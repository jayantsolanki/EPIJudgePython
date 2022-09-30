from typing import List

from test_framework import generic_test

"""
Given an array of positive integers, find the largest h such that there are at least h entries
in the array that are greater than or equal to h
h index is h number of papers having at least h citations
Logic:
    Sort it and find the value h at position i, such that h >= n - i 
Time: O(nlogn)
"""

def h_index(citations: List[int]) -> int:

    citations.sort()
    n = len(citations)
    for i, c in enumerate(citations):
        if c >= n - i:#if a value is encountered which is greater than equal to n - i, return it
            return n - i #(h index is the count of values remained including value at i, hence n - i)
    return 0

# https://leetcode.com/problems/h-index/
#alternate you need to find the side of the square, value 
#you need to find the largest, hence start from left
#i+1 is the square side
#descending
def h_index_v1(citations: List[int]) -> int:

    citations.sort(reverse=True)
    n = len(citations)
    i = 0
    while i < n:#stop as soon as you find citation[i] which is less than i + 1
        if citations[i] >=  i + 1:
            i += 1
            continue
        else:
            break
        
    return i

#https://leetcode.com/problems/h-index/discuss/70946/AC-Python-40-ms-solution-O(n)-time-O(n)-space-using-counting-sort
"""
Also variant 3
alternate using counting sort
here we dont need to actually sort the array. Since we only need to find out the number of papers is equal to h number of citations
We just count papers distributed across each citations
The counting results are:
https://leetcode.com/problems/h-index/solution/
Exmple:  citations=[1,3,2,3,100]. Counting sorts work by making sure that range of values in an array in within the total length of array. However, in real word, not every citation will be less than total papers. So we just convert those high number = total papers. Example, if authors has 10 papers, and three of them have > 10 citations, so we just fix those values to 10. H-index wont change. No k is the index of each number, 0 citation goes to 0 position, 1 citation paper go to index 1, and so on, also called k citations
Count takes the total number of those citations encountered and create a array of those. Analogous to hash map for the counts of each citations.
The value sk is defined as "the sum of all counts with citation >= k". That is sk[0] is count of papers having at least 0 citations,
sk[1] is count of papers having at least 1 citations. So as soon as we find sk going below k, thats the answer
k     	0	1	2	3	4	5 #citation values
count	0	1	1	2	0	1 #paper count
sk  	5	5	4	3	1	1
The observation h index is limited by both citation and paper count gives us the idea of counting/bucket sort. 
Imagine above as a histgram of each paper count, bar height at value x is the value that is equal how many papers which has count x
"""
def h_indexs(citations: List[int]) -> int:
    n = len(citations)
    citationCounts = [0] * (n + 1)  # citationCounts[i] is the number of papers with i citations.
    for c in citations:#each citation becomes the index
        citationCounts[min(n, c)] += 1  # All papers with citations larger than n is counted as n.
    k = 0
    s = len(citations) #or n+1 #total papers
    while s >= k:
        s = s - citationCounts[k]#keep on lowering the paper count
        k += 1

    return k-1
#variant 1
"""
Suppose you cannot alter the input array, and cannot allocate additional memory space. 
Design a fast algo for computing the h-index
Confusing

"""

#variant 2
"""
https://leetcode.com/problems/h-index-ii/
Suppose the input array is sorted. Design a fast algorithm for computing the h-index
Logic: Use binary search to find the paper whose citation is >= n - i
    We are finding the index where the value at that index is >= papers left that is n - i
    We need to find the left most value where the condition citation[mid] >= n - i, still stands
https://leetcode.com/problems/h-index/discuss/70990/Java-AC-solution-by-Binary-Search
binary search could be used to solve this problem; at each check point, say mid, and its value is citation[mid]; we could check whether there are not more than citation[mid] citations behind it, by comparing citation[mid] and n - mid; and after processing, the pointer left will be at the index which is just invalid; so the final answer is n - left;
"""
import bisect
def h_index_var3(citations: List[int]) -> int:

    citations.sort()
    n = len(citations)
    left, right = 0, n - 1
    mid = 0
    while left <= right:
        mid = left + (right - left)//2
        if citations[mid] >= n - mid:
            right = mid - 1
        else:#citations[mid] < n - i
            left =  mid + 1

    return n - left
h_index_var3([1,3,2,3,100])
h_index_var3([3,0,6,1,5])
h_index_var3([1,3,1])
h_index_var3([0])

if __name__ == '__main__':
    exit(generic_test.generic_test_main('13-03-h_index.py', 'h_index.tsv', h_index))
