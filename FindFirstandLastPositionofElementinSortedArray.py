'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums_target = []
        nums_empty = []
        if target not in nums:
            return([-1,-1])

        for i in nums:
            if i == target:
                register = nums.index(i)
                nums_target.append(register)
                nums.pop(register)
                nums.insert(register, 'x')

        if len(nums_target) == 1:
            return([nums_target[0], nums_target[0]])

        return([nums_target[0], nums_target[-1]])
