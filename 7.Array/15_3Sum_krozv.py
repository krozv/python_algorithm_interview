# 세 수의 합 - Exhaustive Search(완전 검색)
"""
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트 출력
"""
class ThreeSum:
    def three_sum(self, nums: []) -> [[int]]:
        zero_sum = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                print(nums[i], nums[j])
                key = nums[i] + nums[j]
                try:
                    last = nums.index(-key, j+1)
                    output = [nums[i], nums[j], -key]
                    output.sort()
                    if output not in zero_sum:
                        zero_sum.append(output)
                except ValueError:
                    pass
        return zero_sum


c = ThreeSum()
nums = [-1, 0, 1, 2, -1, -4]
print(c.three_sum(nums))