"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output "Fizz" instead of the number
and for multiples of five it should output "Buzz".
For numbers which are multiples of both three and five, output "FizzBuzz".
"""

# First Pass
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        for x in range(1, n + 1):
            if x % 3 == 0 and x % 5 == 0:
                output.append("FizzBuzz")
            elif x % 3 == 0:
                output.append("Fizz")
            elif x % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(x))
        return output

# Other Solutions
def fizzBuzz(n):
    return [str(i)
            if (i % 3 != 0 and i % 5 != 0)
            else (('Fizz'*(i % 3 == 0)) + ('Buzz'*(i % 5 == 0)))
            for i in range(1, n+1)]
