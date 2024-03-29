import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure


"""
Fixed capacity 
146. LRU Cache
https://leetcode.com/problems/lru-cache/ This is based on using two dicts and a double linked list
1756. Design Most Recently Used Queue https://leetcode.com/problems/design-most-recently-used-queue/

Create a cache for looking up prices of books identified by their ISBN. You implement lookup, insert, and remove methods. 
Use the Least Recently Used (LRU) policy for cache eviction. If an ISBN is already present, insert should not change the price, 
but it should update that entry to be the most recently used entry. Lookup should also update 
that entry to be the most recently used entry.

Logic:
    Use Hash table for quickly looking up books using ISBN as key. For each key we store price and timestamp, which is 
    count corresponding to when that isbn was most recently looked up
    Use Queue to implement LRU or MRU, with least one at the end and most recently one at the start. Use linked list for this
    because we may need to find the isbn in the middle of queue and need to bring it to front
    In case cache is full or deletion is required for inserting new one, we just remove entry from the end of Queue and also
    delete that entry from hashtable

    Using OrderedDict to achieve above requirements
    # If you insert a new item into an existing ordered dictionary, then the item is added to the 
    # end of the dictionary
    # If you delete an item from an existing ordered dictionary and insert that same item again, 
    # then the new instance of the item is placed at the end of the dictionary
    If an item is overwritten in the OrderedDict, it’s position is maintained.
    Just remember all these functions (popitem(last=False), which returns LRU (first item) if False is applied, pop(key) removes the
    element with key
Time: O(1) for lookup, update and queue, overall O(1)
"""
class LruCache:
    def __init__(self, capacity: int) -> None:
        #ordereddict is a dictionary based Queue
        # remembers the order of items, which is defined by the insertion order of keys
        #  The primary goal was to have efficient maintenance of order even for severe workloads such as that 
        # imposed by the lru_cache which frequently alters order without touching the underlying dict
        # If you insert a new item into an existing ordered dictionary, then the item is added to the 
        # end of the dictionary
        # If you delete an item from an existing ordered dictionary and insert that same item again, 
        # then the new instance of the item is placed at the end of the dictionary
        # https://realpython.com/python-ordereddict/
        # self._isbn_price_table: collections.OrderedDict[
        #     int, int] = collections.OrderedDict()
        # OrderedDict
        # If an item is overwritten in the OrderedDict, it’s position is maintained.
        # If an item is deleted and added again, then it moves to the last.
        # OrderedDict popitem removes the items in FIFO order. It accepts a boolean argument last, 
        # if it’s set to True then items are returned in LIFO order.
        self._isbn_price_table = collections.OrderedDict()

        self._capacity = capacity

    def lookup(self, isbn: int) -> int:#when looking up, move the item to the start (most recently used)

        if isbn not in self._isbn_price_table:
            return -1
        #popping is one way of deleting the key
        price = self._isbn_price_table.pop(isbn)#popping makes sure that item is moved to top when inserting in the second line
        self._isbn_price_table[isbn] = price
        return price

    def insert(self, isbn: int, price: int) -> None:
        # below we check two thing, first if key exists then delete it and read it back to move the key to MRU, also do not use the price pa
        #parameter, since we need to preserve older price
        #else if isbn not exists and capacity reached then deleted last item (LRU) using popitem false
        #finally add the key
        # We add the value for key only if key is not present - we don't update
        # existing values.
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn) #delete first, insert should not change the price
        elif len(self._isbn_price_table) == self._capacity:
            #remove least recently used, popitemn False, so removes the item at the beginning, popleft
            self._isbn_price_table.popitem(last=False) 
        #moving to last entry (most recently used), note ORderedDict is LIFO, so most recently used is at end
        self._isbn_price_table[isbn] = price

    def erase(self, isbn: int) -> bool:
        if isbn in self._isbn_price_table:
            self._isbn_price_table.pop(isbn)
            return True
        else:
            False
        #above same as below
        # return self._isbn_price_table.pop(isbn, None) is not None


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('12-03-lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
