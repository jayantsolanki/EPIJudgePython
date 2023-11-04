from typing import List
import re
from test_framework import generic_test

"""
Leetcode: 93. Restore IP Addresses
https://leetcode.com/problems/restore-ip-addresses/

Write a program that determine where to add periods to a decimal string so that the resulting string
is a valid IP address. There may be more than one valid addresses. Print all possibilities.
Logic:
    Use string decomposition using recursion, or use three nested for loops and take care to identify empty string and 00,000
Time: Constant O(2^32)
Space: O(n) * Valid ips
"""
def get_valid_ip_addresss(s: str) -> List[str]:
    result = []
    ip_length = len(s) 
    parts = [""] * 4
    def is_valid(part):
        #assuming first digit wont be zero
        # '00', '000', '01', etc. are not valid, but '0' is valid.
        #THIS CHECKS 0-9 OR 1 TO 255
        #first condition makes sure that not empty string
        # return len(part) != 0 and (len(part) == 1 or (part[0] != '0' and int(part) <= 255))
        # using regex
        # 0-9 or 10-99 or 100-199 or 200 - 249 or 250 - 255
        return bool(re.search("^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$", part))
    for i in range(min(4, ip_length)):#0000 or 1111, so dot will be only placed at 1.111, 11.11, 111.1 for first dot
        if is_valid(s[: i + 1]):
            parts[0] = s[: i + 1]
            for j in range(i + 1, min(i + 4, ip_length)):
                if is_valid(s[i + 1: j + 1]):
                    parts[1] = s[i + 1: j + 1]
                    for k in range(j + 1, min(j + 4, ip_length)):
                        if is_valid(s[j + 1: k + 1]):
                            parts[2] = s[j + 1: k + 1]
                            if is_valid(s[k + 1:]):
                                parts[3] = s[k + 1: ]
                                result.append('.'.join(parts))
    return result
# get_valid_ip_address('255255255255')  
# get_valid_ip_address('11000')
# get_valid_ip_address('19216811')

#using recursion, my fav, using string decomposition techinque
def get_valid_ip_address_rec(s: str) -> List[str]:
    result = []
    ip_length = len(s) 
    def backtrack(i, ip, dot_count):
        if i == ip_length and dot_count == 4:
            result.append(".".join(ip))
        else:
            for j in range(i + 1, ip_length + 1):
                if dot_count > 3:#prune
                    break
                elif int(s[i: j]) == 0:# #just move for one digit and dont move further, 0, not 00, or 000
                    backtrack(j, ip + [s[i: j]], dot_count + 1)
                    break
                elif 1 <= int(s[i: j]) <= 255:#it works because previous if condition took care of digits beginning with 0
                    backtrack(j, ip + [s[i: j]], dot_count + 1)
                else:#prunning
                    break
            return
    backtrack(0, [], 0)
    return result
#simpler recursion, a bit slightly slow
def get_valid_ip_address(s: str) -> List[str]:
    result = []
    ip_length = len(s) 
    def is_valid_part(s):
        # '00', '000', '01', etc. are not valid, but '0' is valid.
        return len(s) == 1 or (s[0] != '0' and int(s) <= 255)
    def backtrack(i, ip, dot_count):
        if i == ip_length and dot_count == 4:
            result.append(".".join(ip))
        else:
            for j in range(i + 1, ip_length + 1):
                if dot_count > 3:#prune
                    break
                elif is_valid_part(s[i: j]):
                    backtrack(j, ip + [s[i: j]], dot_count + 1)
                else:
                    break
            return
    backtrack(0, [], 0)
    return result

def get_valid_ip_address_ori(s: str) -> List[str]:
    def is_valid_part(s):
        # '00', '000', '01', etc. are not valid, but '0' is valid.
        return len(s) == 1 or (s[0] != '0' and int(s) <= 255)

    result, parts = [], [''] * 4
    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]
        if is_valid_part(parts[0]):
            for j in range(1, min(len(s) - i, 4)):
                parts[1] = s[i:i + j]
                if is_valid_part(parts[1]):
                    for k in range(1, min(len(s) - i - j, 4)):
                        parts[2], parts[3] = s[i + j:i + j + k], s[i + j + k:]
                        if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                            result.append('.'.join(parts))
                            
    return result




def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('6-09-valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
