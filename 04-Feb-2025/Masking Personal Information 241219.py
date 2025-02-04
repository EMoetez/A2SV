# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        if "@" in s:
            lower1=s.split("@")[0].lower()  
            lower2= s.split("@")[1].lower()
            return lower1[0]+"*****"+lower1[-1]+"@"+lower2
        
        else:
            nums=[]
            for char in s:
                if char.isnumeric():
                    nums.append(char)
            rest=(len(nums)-4)%3
            div= (len(nums)-4)//3

            if len(nums)==10:
                return "***-" * div + ''.join(nums[-4:])
            elif rest!=0:
                return "+"+"*" * rest +"-" + "***-" * div + ''.join(nums[-4:])
            else:
                return "+" + "***-" * div + ''.join(nums[-4:])


            


        



            
            
