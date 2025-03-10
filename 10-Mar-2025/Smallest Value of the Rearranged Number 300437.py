# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        nums=[]
        if num<10 and num >-10:
            return num
        if num>0:
            for i in str(num):
                nums.append(int(i))
            nums.sort()
            if nums[0]==0:
                i=0
                while nums[i]==0:
                    i+=1
                nums[0],nums[i]=nums[i],nums[0]
            return int("".join(map(str,nums)))
        else:
            for i in (str(num))[1:]:
                nums.append(int(i))
            nums.sort(reverse=True)
            return -int("".join(map(str,nums)))

