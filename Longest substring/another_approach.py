"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def longest_substring(s):
        sub = {}
        cur_sub_start = 0
        cur_len = 0
        longest = 0

        for index, letter in enumerate(s):

            if letter in sub and sub[letter] >= cur_sub_start:
                cur_sub_start = sub[letter] + 1
                cur_len = index - sub[letter]
                sub[letter] = index

            else:
                sub[letter] = index
                cur_len += 1
                if cur_len > longest:
                    longest = cur_len
        return longest


obj = Solution()
value = obj.longest_substring("abcdecfgh")
print(value)
