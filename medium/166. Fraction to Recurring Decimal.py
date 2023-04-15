"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
 

Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0
"""

class Solution:

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator == 0:

            return '0'

        res = []

        if numerator * denominator < 0:

            res.append('-')

        numerator = abs(numerator)

        denominator = abs(denominator)

        res.append(str(numerator // denominator))

        remainder = numerator % denominator

        if remainder == 0:

            return ''.join(res)

        res.append('.')

        remainder_map = {}

        # 1/3 = 0.(3)
        # 1/6 = 0.1(6)
        while remainder != 0:

            if remainder in remainder_map:

                res.insert(remainder_map[remainder], '(')

                res.append(')')

                break

            remainder_map[remainder] = len(res)

            remainder *= 10

            res.append(str(remainder // denominator))

            remainder %= denominator

            print (res)

        return ''.join(res)

s = Solution()

print(s.fractionToDecimal(1, 3))

print(s.fractionToDecimal(1, 6))

print(s.fractionToDecimal(1, 2))

print(s.fractionToDecimal(2, 1))
