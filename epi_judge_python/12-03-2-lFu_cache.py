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
        self.min_freq = 1 #stores the min freq
        

    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1
        freq = self.key_to_freq[key]#we need to update the frequency when a key is accessed, hence get that
        self.key_to_freq[key] = freq + 1
        value = self.freq_to_key[freq][key]
        del self.freq_to_key[freq][key]#need to delete that key from ordereddictioanry, because it doesnt belong to that orderedlist anymore
        #,insrted in a higher frequency orderedList it will be LIFO
        self.freq_to_key[freq+1][key] = value #note reinsertion has  freq + 1
        if self.min_freq == freq and not self.freq_to_key[freq]: #update min freq only if min_freq was initially == freq and 
            #only if self.freq_to_key entry for freq doesnt existed, if existed then we dont need to update the min_freq
            self.min_freq += 1
        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_freq: #update if already there
            self.get(key) #this updates the frequency
            #now update the value
            self.freq_to_key[self.key_to_freq[key]][key] = value # self.key_to_freq[key] get the frequency, this line updaes with new value
        else:#else new key
            self.capacity -= 1
            self.key_to_freq[key] = 1
            self.freq_to_key[1][key] = value
            if self.capacity < 0:#now delete the LRU key
                self.capacity += 1
                k, v = self.freq_to_key[self.min_freq].popitem(False) #deletes from back
                del self.key_to_freq[k] #now delete from key-freq dictionary
            self.min_freq = 1 #important #1 because it the new key