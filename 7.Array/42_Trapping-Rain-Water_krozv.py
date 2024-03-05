# 08. 빗물 트래핑
'''
높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라
'''
class Trapping_Rain_Water:
    def trap(self, height: [int]) -> int:
        start = 0
        end = len(height)-1
        water = 0
        line = 0
        while start < end:
            print(start, end)
            for i in range(start, end+1):
                if i == end:
                    start = end
                elif height[i] <= line:
                    continue
                else:
                    start = i
                    break
            for i in range(end, start-1, -1):
                if height[i] <= line:
                    continue
                else:
                    end = i
                    break
            line = min(height[start], height[end])
            for i in range(start, end):
                if height[i] < line:
                    water += line - height[i]
                    height[i] = line
        return water


c = Trapping_Rain_Water()
# arr = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
arr2 = [2, 0, 2]
print(c.trap(arr2))