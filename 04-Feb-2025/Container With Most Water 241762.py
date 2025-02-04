# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        output=0
        left, right = 0,len(height)-1
        while left < right:
            
            max_area= (right-left)* min(height[right],height[left])
            output = max(output,max_area)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
            
        return output