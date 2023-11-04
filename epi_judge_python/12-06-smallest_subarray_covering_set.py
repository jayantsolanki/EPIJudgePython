import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

#Below all are sliding window problem

"""
Write a program  which takes an array of strings and a set of strings, and return the indices of the starting and ending 
index of a shortest subarray of the given array that 'cover' all the elements in the set, irrespective of the order
Logic:
    Use a sliding window, but with flexible start and end.
    Move end first, and stop as soon as all elements covered, then start to reduce the size of that window by moving the
    start. If moving the start causes some element is the set not covered, then start moving the end, until all elements covered
    Repeat start and end adjustment until you reach the end of array. Then return the smallest window found.
Time: O(n)
"""
#works for duplicates too, also in leetcode 76
# https://leetcode.com/problems/minimum-window-substring/
Subarray = collections.namedtuple('Subarray', ('start', 'end'))
def find_smallest_subarray_covering_set_v2(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:

    keywords_to_cover = collections.Counter(keywords)
    result = Subarray(start=-1, end=-1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:#keyword is a set, lookup is O(1)
            keywords_to_cover[p] -= 1 
            ##this is very important, because same word can be encountered many times, 
            # dont update if counter is negative
            if keywords_to_cover[p] >= 0: 
                # so lower the cover count when it goes to zero,  if it is negative then no need
                remaining_to_cover -= 1 #if p is covered, then reduce the size

        # Keeps advancing left until keywords_to_cover does not contain all
        # keywords.
        #once all the elements are covered, start to reduce the size, that is increment left index
        while remaining_to_cover == 0:
            if result == Subarray(#check if the size of subarray is less, if less than save the new indices
                    start=-1,
                    end=-1) or right - left < result.end - result.start:
                result = Subarray(start=left, end=right)
            pl = paragraph[left]
            if pl in keywords:# Keeps advancing left until keywords_to_cover does not contain all elements in the set
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:#so increase the cover only when it goes above zero
                    remaining_to_cover += 1  #since keywords_to_cover[pl] became > 0
            left += 1
    return result

#alternate, only difference in how we track the element in the set, see keywords_to_cover
#only works for distinct keywords
def find_smallest_subarray_covering_set_simple(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:

    # keywords_to_cover = collections.Counter(keywords)
    keywords_to_cover = {x: 0 for x in keywords} # here we update that element has covered when its count becomes 1
    result = Subarray(start=-1, end=-1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:#keyword is a set, lookup is O(1)
            # keywords_to_cover[p] -= 1
            keywords_to_cover[p] += 1#that specific element in the set can occur many times in the subarray
            if keywords_to_cover[p] == 1: ##only update remaining_to_cover when it reaches 1, stop doing when  > 1
                # so lower the cover count when it goes to zero,  if it is negative then no need
                remaining_to_cover -= 1 #if p is covered, then reduce the size

        # Keeps advancing left until keywords_to_cover does not contain all
        # keywords.
        #once all the elements are covered, start to reduce the size
        while remaining_to_cover == 0:
            if result == Subarray(#check if the size of subarray is less, if less than save the new indices
                    start=-1,
                    end=-1) or right - left < result.end - result.start:
                result = Subarray(start=left, end=right)
            pl = paragraph[left]
            # Keeps advancing left until keywords_to_cover does not contain all elements in the set
            if pl in keywords:
                keywords_to_cover[pl] -= 1
                if keywords_to_cover[pl] == 0:#so increase the cover only when it goes above zero
                    remaining_to_cover += 1
            left += 1
    return result

#this one tackles duplicates in the keywords, see leetcode 
# https://leetcode.com/problems/minimum-window-substring/submissions/
def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:

        # keywords_to_cover = collections.Counter(keywords)
        if len(paragraph) < len(keywords):
            return ""
        keywords_to_cover = {x: 0 for x in keywords} # here we update that element has covered when its count becomes 1
        KeyCountNeeded = collections.Counter(keywords) #desired count per character needed
        remaining_to_cover = len(keywords)
        keywords = set(keywords)
        result = Subarray(start=-1, end=-1)
        left = 0
        for right, p in enumerate(paragraph):
            if p in keywords:#keyword is a set, lookup is O(1)
                keywords_to_cover[p] += 1#that specific element in the set can occur many times in the subarray
                if keywords_to_cover[p] <= KeyCountNeeded[p]: #keep updating until desired count reached
                    remaining_to_cover -= 1 #if p is covered, then reduce the size

            # Keeps advancing left until keywords_to_cover does not contain all
            # keywords.
            #once all the elements are covered, start to reduce the size
            while remaining_to_cover == 0:
                #check if the size of subarray is less, if less than save the new indices
                if result == Subarray(
                        start=-1,
                        end=-1) or right - left < result.end - result.start:
                    result = Subarray(start=left, end=right)
                pl = paragraph[left]
                # Keeps advancing left until keywords_to_cover does not contain all elements in the set
                if pl in keywords:
                    keywords_to_cover[pl] -= 1
                    #so increase the cover only when it goes below deisred count
                    if keywords_to_cover[pl] < KeyCountNeeded[pl]:
                        remaining_to_cover += 1
                left += 1
        return result


# Variant 1
"""
Given an array A, find a shortest subarray A[i, j] such that each distinct value present in A is
also present in the subarray
Logic:
    Basically the keyword set consists of all the unique characters of A, then redo the first problem
    YOu need to create the keyword list from A itself
"""

# def find_shortest_subarray(A: List[str]):
def find_shortest_subarray(A: List[str]):
    Subarray = collections.namedtuple('Subarray', ('start', 'end'))
    keywords = set([x for x in A])
    print(keywords)
    keywords_to_cover = collections.Counter(keywords)
    result = Subarray(start=-1, end=-1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(A):
        if p in keywords:#keyword is a set, lookup is O(1)
            keywords_to_cover[p] -= 1
             ##this is very important, because same word can be encountered many times
            if keywords_to_cover[p] >= 0:
                # so lower the cover count when it goes to zero,  if it is negative then no need
                remaining_to_cover -= 1 #if p is covered, then reduce the size

        # Keeps advancing left until keywords_to_cover does not contain all
        # keywords.
        #once all the elements are covered, start to reduce the size
        while remaining_to_cover == 0:
            if result == Subarray(#check if the size of subarray is less, if less than save the new indices
                    start=-1,
                    end=-1) or right - left < result.end - result.start:
                result = Subarray(start=left, end=right)
            pl = A[left]
            # Keeps advancing left until keywords_to_cover does not contain all elements in the set
            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:#so increase the cover only when it goes above zero
                    remaining_to_cover += 1  #since keywords_to_cover[pl] became > 0
            left += 1
    return result

find_shortest_subarray('aaacbabcdbabddbddaba')

#variant 2: Unable to understand
"""
Given an Array A, rearrange the elements so that the shortest subarray containing all the distinct
values in A has maximum possible length.

http://talk.elementsofprogramminginterviews.com/t/variant-13-9-2-given-an-array-a-rearrange-the-elements-so-that-the-shortest-
subarray-containing-all-the-distinct-values-in-a-has-maximum-possible-length/311/4
The approach that was suggested is to put the least frequent item (and its duplicates) in one end,
 and the next less frequent item on the other end and so on. 
"""
def max_subarray_distinct(A):
    pass

max_subarray_distinct('abcbadcaeaabe')


#variant 3
# https://leetcode.com/problems/rearrange-string-k-distance-apart/
#https://www.geeksforgeeks.org/rearrange-a-string-so-that-all-same-characters-become-at-least-d-distance-away/
"""
https://www.geeksforgeeks.org/rearrange-a-string-so-that-all-same-characters-become-atleast-d-distance-away/
Given an array A and a positive integer k, rearrange the elements so that no two equal elements are k or less apart.
Expected time complexity is O(n) where n is length of input string.
Logic:
    https://leetcode.com/problems/rearrange-string-k-distance-apart/discuss/83222/Straightforward-Python-Solution-98
    The idea is simple: we only worry about the most frequent character(s).
    For example aaaabbbbcccddefg, a is the most frequent letter, so we start with a structure like
    a [] a [] a [] a []
    and we just pad other letters in between the a's. Only letters with the same highest frequency can go 
    in to the last []. and we don't care about any letters with lower frequencies, we just scatter them 
    among the paddings. So we end up with
    a [bcdf] a [bcdg] a [bce] a [b].
    If all the paddings (buckets) except the last one have length larger than k-1, then we
     have our answer; else we return ''.
    Solution below is modified, based on heap
    Type of Greedy algo
    Time complexity O(nlgm), m is the number of distinct letter. Since k can only be 26, 
    time complexity is O(n)
    Time: O(n), space O(26)
"""
def rearrangeString(string, k):
    if not string:
        return ''
    
    count = collections.Counter(string)

    # sort the letters according to the frequency, descending order
    max_heap = []
    for key, value in count.items():
        heapq.heappush(max_heap, (-value, key))
    
    count, char = heapq.heappop(max_heap)  # get most frequent character
    # count = -1 * count
    lst = [[char] for _ in range(-1 * count)] #this contains the  buckets

    # take care of the letters with same highest freq
    # while max_heap and max_heap[0][0] == count:
    #     # char, _ = stack.pop()
    #     _ , char = heapq.heappop(max_heap)
    #     for l in lst:
    #         l.append(char)
    chrCount = 0
    count = -1 * count
    while max_heap:
        charCount , char = heapq.heappop(max_heap)
        charCount = -1 * charCount
        #now start dispersing those characters, but fill the buckets evenly
        for _ in range(charCount):
            # special case, this char has the same count as max_count, so must spread it evently. Must use the last bucket.
            if charCount == count: #same as max count encountered
                lst[chrCount % count].append(char) #use all bucket
            else:
                # general case: don't use the last bucket; this way we maximize the chars between each 
                # two adjacent buckets. 
                # Reason we do this is becuse we need to make sure that 
                #spacing between character which has max count is k, we also pad the last bucket than 
                # previous bucket may not be completely filled and we lose the k distance for max 
                # count character
                lst[chrCount % (count - 1)].append(char) #omit last bucket
            #filling has to be sequential hence we cant use charCount, we use chrcount which keep on increasing
            chrCount += 1
    # all the characters left
    #res = ''.join((-1*n)*c for n, c in max_heap) #rest of the characters are joined in together like cccddefg, same belong together
    # padding or filling in
    # for i, r in enumerate(res):
    #     if 
    #     lst[i % (len(lst)-1)].append(r)

    for l in lst[:-1]:#each bucket should be of length k or more, except last one
        if len(l) < k:
            return ''

    return ''.join(''.join(l) for l in lst)

#this is better
#https://leetcode.com/problems/rearrange-string-k-distance-apart/discuss/347007/Python-heap-que-with-explanation
"""
Create a heapq orderd by frequency from big to small. The que length will be at most 26.
Create a cooldown dictionary, key being letter, value being remaining frequency, to hold 
letters in cool down state.

If k==0 or k==1, just return s. Otherwise,
Pop biggest frequency letter from que, add it to result.
Letter frequency -1, put it to the cool down dictionary.
For each iteration, pop letter that finished cooling down from the cool down dictionary, push it 
back to the frequency heap.
When it is impossible to make a valid result, the result array length must be shorter than input 
string. In such case we return "".
Time complexity O(nlgm), m is the number of distinct letter. Since k can only be 26, time complexity is O(n)
"""
def rearrangeString(s: str, k: int) -> str:
    if k<=1: 
        return s
    d = collections.Counter(s)

    freqs = [(-value, key) for key, value in d.items()]
    heapq.heapify(freqs)        
    cooling={}
    res=[]
    while freqs:
        freq, c = heapq.heappop(freqs)
        res.append(c)
        freq += 1
        if freq < 0:                
            cooling[c] = (freq, c)
        #only pop element that is k distance away, makes sure the high frequncy letter has 
        # to cool down at least k times
        #once the length reaches at least k , pull back the cooled element added k times ago
        if len(res) >= k and res[-k] in cooling:
            prevFreq, prevC = cooling.pop(res[-k])
            heapq.heappush(freqs,(prevFreq, prevC))        
    return ''.join(res) if len(res) == len(s) else ""

#subvariant 3, characters and their duplicates exactly d distance away
"""
https://www.geeksforgeeks.org/rearrange-a-string-so-that-all-same-characters-become-at-least-d-distance-away/
The approach to solving this problem is to count frequencies of all characters and consider the most frequent 
character first and place all occurrences of it as close as possible. After the most frequent character is 
placed, repeat the same process for the remaining characters.
Exactly d distance away
"""
import heapq
import collections
# O(n + mLog(MAX))
def spreadout_elements_k(A, k):
    max_heap = []
    element_counter = collections.Counter(A)
    result = [''] * len(A)
    #creating max_heap
    for key, value in element_counter.items():
        heapq.heappush(max_heap, (-value, key))
    print(max_heap, element_counter, result)

    # now start filling the result array
    index = 0
    while max_heap:
        item_count, item = heapq.heappop(max_heap)
        while result[index] != '':#find the next available index if current one occupied
            index = index + 1
        for i in range(-item_count):
            if index + i * k >= len(result):
                print(result)
                return "Cannot be rearranged"
            result[index + i * k] = item
        index = index + 1
    print(result)

spreadout_elements_k("aabbcc", 4)

#subvariant 4:
# https://leetcode.com/problems/reorganize-string/

#more simple answer is to alternate 
# https://leetcode.com/problems/reorganize-string/discuss/113457/Simple-python-solution-using-PriorityQueue
"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
The idea is to build a max heap with freq. count
a) At each step, we choose the element with highest freq (a, b) where b is the element, to append to result.
b) Now that b is chosen. We cant choose b for the next loop. So we dont add b with decremented value count 
immediately into the heap. Rather we store it in prev_a, prev_b variables.
c) Before we update our prev_a, prev_b variables as mentioned in step 2, we know that whatever prev_a, prev_b 
contains, has become eligible for next loop selection. so we add that back in the heap.

In essence,

at each step, we make the currently added one ineligible for next step, by not adding it to the heap
at each step, we make the previously added one eligible for next step, by adding it back to the heap

Basically we pick(pop) the highest frquecy letter, put it to result, then lower itsd frequency, 
move it to temp variable (cool down) then pop next element, then push the previously cool down element 
and then redo cooldown for popped element
"""
def reorganizeString(S):
    res, c = [], collections.Counter(S)
    pq = [(-value,key) for key,value in c.items()]
    heapq.heapify(pq)
    p_a, p_b = 0, ''
    cooldown = (0, "")
    while pq:
        freq, letter = heapq.heappop(pq)
        res += [letter]
        if cooldown[0] < 0:
            heapq.heappush(pq, cooldown)
        freq += 1
        cooldown = (freq, letter)
    res = ''.join(res)
    if len(res) != len(S): return ""
    return res

@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '12-06-smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
