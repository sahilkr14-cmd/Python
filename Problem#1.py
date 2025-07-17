# Leetcode #1
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def twosum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]
        num_map[num] = i
    return[]

nums = [2, 7, 11, 15]
target = 18
print(twosum(nums, target))  # Output: [0, 1]
