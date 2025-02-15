# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        count = Counter(answers)
        min_num=0
        for likely, rabbit in count.items():
            if rabbit<=likely+1:
                min_num+= likely+1
            elif rabbit > likely+1 and rabbit % (likely+1)==0:
                # print("added "+str(rabbit)+" case "+ str(likely))
                min_num+= rabbit
            elif rabbit > likely+1 and rabbit % (likely+1)!=0:
                # print("added "+str( (rabbit- rabbit % (likely+1)) + likely+1)+" case "+ str(likely))
                min_num+= (rabbit - rabbit % (likely+1)) +likely+1
        return min_num

