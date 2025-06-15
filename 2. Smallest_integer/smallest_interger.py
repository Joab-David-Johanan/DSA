"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

"""


class Solution(object):
    def smallest_positive_number(self, A):
        n = len(A)
        # cleaning the array
        for i in range(n):
            if A[i] <= 0 or A[i] > n:
                A[i] = n + 1

        # marking the presence of elements from [1...n] with -ve sign
        for i in range(n):
            val = abs(A[i])
            if 1 <= val <= n:
                A[val - 1] = -abs(A[val - 1])

        # returning the first positive number we find

        for i in range(n):
            if A[i] > 0:
                return i + 1

        # if we have all elements from [1...n] as -ve values then the only solution is n+1 so we return it
        return n + 1

    def smallest_non_negative_number(self, A):
        n = len(A)

        # Replace negative numbers and numbers greater than n with n+1
        for i in range(n):
            if A[i] < 0 or A[i] > n:
                A[i] = n + 1

        # Mark the presence of values in [0..n]
        for i in range(n):
            val = abs(A[i])
            if 1 <= val <= n:
                A[val - 1] = -abs(A[val - 1])

        # Check if 0 is missing before we check for positive numbers
        if 0 not in A:
            return 0

        # Now look for first positive index -> missing number
        for i in range(n):
            if A[i] > 0:
                return i + 1

        # All numbers from 0..n are present
        return n + 1

    def set_implementation(self, A):
        s = set(A)
        i = 1
        while i in s:
            i += 1
        return i

    def set_another_version(self, A):
        s = set(A)
        i = 0
        while i in s:
            i += 1
        return i


obj = Solution()
result = obj.smallest_positive_number([0, -1, 10, 2, 3, 4])
result1 = obj.smallest_non_negative_number([-1, 1, 2, 3, 4, 5, -10])
result2 = obj.set_implementation([0, -1, 10, 2, 3, 4])
result3 = obj.set_another_version([-1, 1, 2, 3, 4, 5])
print(result, result1, result2, result3, sep='\n')
