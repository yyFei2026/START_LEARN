# 第一次做：2026.9.27

def maxArea(height):
    left = 0
    right = len(height) - 1
    Area_initial = 0

    while left < right:
        Area = max((min(height[left], height[right]) * (right - left)), Area_initial)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        Area_initial = Area

    return Area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))