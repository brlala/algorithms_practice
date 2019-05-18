# Maximum continuous subarray sum
data = [4, 6, 100, -2000, 3, 8]  # this should return 106

# O(n) time, O(n) space
def max_continuous_subarray_sum(nums):
    '''
    1. Kadine's algorithm
    the previous is the total of continuous sum,
    :param nums:
    :return:
    '''
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)


print(max_continuous_subarray_sum(data))
