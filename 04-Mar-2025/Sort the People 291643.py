# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            min_index=i
            for j in range(i+1,len(heights)):
                if heights[j]>=heights[min_index]:
                    min_index=j
            heights[i],heights[min_index]=heights[min_index],heights[i]
            names[i],names[min_index]=names[min_index],names[i]
        return names

