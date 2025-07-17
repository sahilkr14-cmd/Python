def twosum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [diff, num]
        num_map[num] = i
    return[]

nums = [2, 7, 11, 15]
target = 18
print(twosum(nums, target))