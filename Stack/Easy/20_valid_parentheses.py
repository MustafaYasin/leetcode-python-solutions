class Solution:
    def isValid(self, s: str) -> bool:
       if len(s) % 2 != 0: return False
       stack = []
       colse_to_open = {')':'(', ']':'[', '}':'{'}

       for c in s:
           if c in colse_to_open:
                if stack and stack[-1] == colse_to_open[c]:
                    stack.pop()
                else:
                    return False
           else:
                stack.append(c)
        
       return True if not stack else False
