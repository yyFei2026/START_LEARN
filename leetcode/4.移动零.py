# 第一次做：2026.9.27

def moveZeros(nums):
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    nums[slow:] = [0] * (len(nums) - slow)
    return nums

nums = [0,1,0,3,12]
print(moveZeros(nums))