'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''将目标减去其中一个加数，再判断剩下一个数是否等于差值'''
        for i in range(len(nums)):
            temp = target -nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == temp:
                    return [i,j]
        return 'no matched nums'
