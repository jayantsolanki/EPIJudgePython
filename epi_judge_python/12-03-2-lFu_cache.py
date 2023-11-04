from collections import defaultdict, OrderedDict
class LFUCache:
    """
    Idea here is to have two dictionary primary, first dictionary maintains key to freq mapping
    Second dictionary maps keys with same frequencies, all those keys with same frequencies are store in a third
    dictionary called OrderedDict, if we need to delete any key with minimum frequency (LFU), we need this orderedDictionary
    to break the tie, orderd dictionary will help us to get least used key
    Note, each frequency val will have their own copy of OrderedDictionary  
    
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq_to_key = defaultdict(lambda : OrderedDict())#all those keys with same frequencies are store in a third
        #dictionary called OrderedDict. OrderedDictionary also stores the value for the key
        self.key_to_freq = defaultdict(int) #maps key to their most updated frequencies
        self.min_freq = 1 #stores the min freq, to track for deleting in case capacity reached
        

    """
    search for the key, if not found return -1 else do following:
    get the current frequency, add one to it, and save it back
    using same current frequency, find the position of the key in freq_to_key dict, get the value from key:value in the orderedDict, 
    now delete that key from the orderedDict
    check if the currentfreq == min_freq, if yes, you need to update the min_freq if no other key present in freq_to+key dict of current freq
    return the value
    """
    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1
        freq = self.key_to_freq[key]#we need to update the frequency when a key is accessed, hence get that
        self.key_to_freq[key] = freq + 1
        value = self.freq_to_key[freq][key]
        del self.freq_to_key[freq][key]#need to delete that key from ordereddictioanry, because it doesnt belong to that orderedlist anymore
        #,insrted in a higher frequency orderedList it will be LIFO
        self.freq_to_key[freq+1][key] = value #note reinsertion has  freq + 1
        #now check if min_freq needs to be updated
        # if self.min_freq == freq and not self.freq_to_key[freq]: #update min freq only if min_freq was initially == freq and 
        #above or below
        if self.min_freq == freq and len(self.freq_to_key[freq]) == 0: #update min freq only if min_freq was initially == freq and 
            #only if self.freq_to_key entry for freq doesnt existed, if existed then we dont need to update the min_freq
            self.min_freq += 1
        return value
        
    """
    Remember updating a key increases its frequencey, inserting a new key sets minfreq = 1
    use self.get to update the frequency
    """
    def put(self, key: int, value: int) -> None:
        if key in self.key_to_freq: #update if already there
            self.get(key) #this updates the frequency
            #now update the value
            self.freq_to_key[self.key_to_freq[key]][key] = value # self.key_to_freq[key] get the frequency, this line updaes with new value
        else:#else new key
            self.capacity -= 1
            self.key_to_freq[key] = 1
            self.freq_to_key[1][key] = value
            #dont update the min_freq untill capacity taken care of
            if self.capacity < 0:#now delete the LRU key
                self.capacity += 1
                k, v = self.freq_to_key[self.min_freq].popitem(False) #deletes from front, that is least recently used/added
                del self.key_to_freq[k] #now delete from key-freq dictionary
            self.min_freq = 1 #important #1 because it the new key