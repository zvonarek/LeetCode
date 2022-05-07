class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [];
        for i in range(n):
            div3 = ((i+1)%3==0)
            div5 = ((i+1)%5==0)
            
            if (div3 and div5): 
                answer.append("FizzBuzz")
            elif (div3):
                answer.append("Fizz")
            elif (div5):
                answer.append("Buzz")
            else:
                answer.append(str(i+1))
        return answer 