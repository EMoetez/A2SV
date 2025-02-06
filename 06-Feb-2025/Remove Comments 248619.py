# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        final_output = []              
        current_line = []              
        in_block_comment = False       
      
        for line in source:
            index, line_length = 0, len(line)
          
            while index < line_length:
                if in_block_comment:
                    if index + 1 < line_length and line[index:index + 2] == "*/":
                        in_block_comment = False  
                        index += 1               
                else:
                    
                    if index + 1 < line_length and line[index:index + 2] == "/*":
                        in_block_comment = True   
                        index += 1               
                    elif index + 1 < line_length and line[index:index + 2] == "//":
                        break                   
                    else:
                        current_line.append(line[index])  
                index += 1  
          
            
            if not in_block_comment and current_line:
                final_output.append("".join(current_line))
                current_line=[] 

        return final_output