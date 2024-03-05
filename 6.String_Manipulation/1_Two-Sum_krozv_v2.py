# 1. Two Sum

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        N = len(nums)
        for i in range(N-1):
            for j in range(i+1, N):
                if nums[i] + nums[j] == target:
                    return [i, j]


nums = [2,7,11,15]
target = 9
c = Solution()
print(c.twoSum(nums, target))