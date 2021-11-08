nums = [2, 7, 11, 15]
target = 9

class Solution:
    def twoSum(self, nums, target):
        complementMap = dict()
        for i in range(len(nums)):
            num = nums[i]  # 7
            complement = target - num  # compliment = 2

            if num in complementMap:
                return [complementMap[num], i]
            else:
                complementMap[complement] = i  ##{7,0}

#     def bruteForceTwoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 sum = nums[i] + nums[j]
#                 if sum == target:
#                     return [i, j]





