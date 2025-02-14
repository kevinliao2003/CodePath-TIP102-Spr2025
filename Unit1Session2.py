# Standard Problem Set Version 1 - Problem 7: Good Things Come in Threes
"""
U - Understand
- can the array be empty? can the integers be + and -?
- is there a limit on the number of operations?
- all elements must be divisible by 3

P - Plan
variables
- total count

iterate though the array
    if curr num divisible by 3, do nothing
    otherwise
        find the nearest element divisible by 3 less than curr num
        find the nearest element divisible by 3 greater than curr num

        compare the absolute value and see which one needs fewer operations
        add to total count that absolute value
return total count

I - Implement
- see code below
"""

def make_divisible_by_3(nums):
    count = 0
    for num in nums:
        if num % 3 != 0:
            left_num = num - 1
            while left_num % 3 != 0:
                left_num -= 1

            right_num = num + 1
            while right_num % 3 != 0:
                right_num += 1

            left_diff = abs(left_num - num)
            right_diff = abs(right_num - num)
            count += min(left_diff, right_diff)

    return count

# nums = [1, 2, 3, 4]
# res = make_divisible_by_3(nums)
# print(res == 3)

# nums = [3, 6, 9]
# res = make_divisible_by_3(nums)
# print(res == 0)

# Standard Problem Set Version 2 - Problem 3: Secret Identity