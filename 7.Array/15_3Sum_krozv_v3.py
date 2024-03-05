# 시간 초과 해결이 관건

class ThreeSum:
    def three_sum(self, nums: []) -> [[int]]:
        zero_sum = []
        nums.sort()
        negative = []
        positive = []
        zero_cnt = 0
        num_dict = {}
        # 음수 양수 분리
        for i in range(len(nums)):
            if nums[i] < 0:
                negative.append(nums[i])
                num_dict[nums[i]] = i
            elif nums[i] == 0:
                zero_cnt += 1
            else:
                positive.append(nums[i])
                num_dict[nums[i]] = i

        for i in range(len(negative) - 1):
            for j in range(i + 1, len(negative)):
                key = negative[i] + negative[j]
                if -key in num_dict:
                    zero_sum.append([negative[i], negative[j], -key])
        for i in range(len(positive) - 1):
            for j in range(i + 1, len(positive)):
                key = positive[i] + positive[j]
                if -key in num_dict:
                    zero_sum.append([-key, positive[i], positive[j]])
        # 0이 존재할 때
        if zero_cnt:
            # 0 개수가 1개
            for i in range(len(negative)):
                if -negative[i] in positive:
                    zero_sum.append([negative[i], 0, -negative[i]])
            # 0 개수가 3개 이상
            if zero_cnt >= 3:
                zero_sum.append([0, 0, 0])
        # 중복 제거
        zero = []
        for elem in zero_sum:
            if elem not in zero:
                zero.append(elem)
        return zero


c = ThreeSum()
nums = [-2, 0, 1, 1, 2]
print(c.three_sum(nums))