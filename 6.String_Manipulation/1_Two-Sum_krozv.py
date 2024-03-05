# 07. 두 수의 합
'''
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴
'''
class Two_Sum:
    def twoSum(self, nums: [int], target: int) -> [int]:
        N = len(nums)
        for i in range(1<<N):
            set = []
            for j in range(N):
                if i & (1<<j):
                    set += [nums[j]]
            if len(set) == 2 and sum(set) == target:
                a = nums.index(set[0])
                nums.reverse()
                b = len(nums) - nums.index(set[1]) - 1
                return [a, b]

c = Two_Sum()
nums = [3, 3]
target = 6
print(c.twoSum(nums, target))