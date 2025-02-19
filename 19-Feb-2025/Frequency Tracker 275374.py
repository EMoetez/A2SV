# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker(object):
    
    def __init__(self):
        self.freq={}
        self.numbers={}
        
    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number in self.numbers:
            freq=self.numbers[number]
            self.freq[freq]-=1
            if self.freq[freq]==0:
                del self.freq[freq]
            self.numbers[number]=freq+1   
        else:
            self.numbers[number]=1
        self.freq[self.numbers[number]]=self.freq.get(self.numbers[number],0)+1

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number in self.numbers:
            freq=self.numbers[number]
            self.freq[freq] -=1
            if self.freq[freq]==0:
                del self.freq[freq]
            if freq>1:
                self.numbers[number] =freq - 1
                self.freq[freq-1]=self.freq.get(freq-1,0)+1
            else:
                del self.numbers[number]
                

        
    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """    
        return frequency in self.freq   
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)


