# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        balls={}
        colors={}
        res=[]
        for i,color in queries:
            if i in balls: 
                old_color=balls[i]
                if old_color!=color:
                    colors[old_color]-=1
                    
                    if colors[old_color]==0:
                        colors.pop(old_color)
                    balls[i]=color
                    colors[color]= colors.get(color,0)+1
            else:
                balls[i]=color
                colors[color]= colors.get(color,0)+1
            res.append(len(colors))
        return res

        
            

