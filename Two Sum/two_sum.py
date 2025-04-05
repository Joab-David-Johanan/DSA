"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""


class Solution(object):
    def two_sum_optimized(self, nums, target):
        hashmap = {}
        for index, element in enumerate(nums):
            complement = target - element
            if complement in hashmap:
                return [index, hashmap[complement]]
            hashmap[element] = index

    def two_sum_brute_force(self, nums, target):
        length = len(nums)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    obj = Solution()
    result1 = obj.two_sum_optimized([2, 3, 4, 7], 9)
    print(result1)
    result2 = obj.two_sum_brute_force([2, 3, 4, 7], 9)
    print(result2)
