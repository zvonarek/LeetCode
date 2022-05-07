class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while (num > 0 ): 
            if (num % 2 == 0): 
                count += 1
                num *= 0.5
            elif (num % 2 != 0):
                count +=1 
                num -= 1
        return count