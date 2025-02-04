# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        great=max(candies)
        output=[]
        for i in range(len(candies)):
            output.append(candies[i]+extraCandies>=great)
            
        return output
                