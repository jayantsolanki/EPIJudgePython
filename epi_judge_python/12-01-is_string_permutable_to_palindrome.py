from gc import collect
from test_framework import generic_test
import collections

#check if a string can have a pallindrome
#Time O(n), space O(c), c is distinct characters
def can_form_palindrome_ori(s: str) -> bool:
    #so if strings is of size n is even, than count of all character occurrence should be even
    if len(s) == 0:
        return True
    elif len(s) % 2 == 0:
        #check if any odds are present, so return false
        return len([v for v in  collections.Counter(s).values() if v % 2 == 1]) == 0
    else:
        # so if strings is of size n is odd , than count of all characters occurrence except one should be even
        return len([v for v in  collections.Counter(s).values() if v % 2 == 1]) == 1


    #book answer, just see the sum of  [0,0,0,0,1,0,0,0] something like this, at most one odd count only
    #return sum([v % 2 for v in  collections.Counter(s).values() ]) <= 1, two odds will make a even sum

#alternate method, we keep on canceling the pairs encountered
#Any methods that use map or set should have space complexity O(1) as the char number should be less than 256 as the assumption in the O(128) or O(256)
def can_form_palindrome(s: str) -> bool: 
    #keep deleting the pairs
    palin = {}
    count = 0
    for char in s:
        count += 1
        if char not in palin:
            palin[char] = 1
        else:
            del palin[char]
    if count % 2 == 0:
        return len(palin) == 0
    else:
        return len(palin) == 1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '12-01-is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
