class ThreeSum:
    def three_sum(self, nums: []) -> [[int]]:
        zero_sum = []
        nums.sort()
        sum_dict = {}
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                two_sum = nums[i] + nums[j]
                if two_sum in sum_dict:
                    if [nums[i], nums[j]] not in sum_dict[two_sum]:
                        sum_dict[two_sum].append([nums[i], nums[j]])
                else:
                    sum_dict[two_sum] = [[nums[i], nums[j]]]
        print(sum_dict)

c = ThreeSum()
nums = [-2, 0, 1, 1, 2, 3]
print(c.three_sum(nums))