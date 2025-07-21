# You are given a nums[] array which can contain positive, negative, zero etc. 
# You have to return the maximum sum of the subarray which contains elements continuously.

def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

nums = [1, -2, 3, 10, -4, 7, 2, -5]
print(maxSubArray(nums))
