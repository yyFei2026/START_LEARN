# 第一次做：2026.9.26

def twoSum(nums, target):
    storage = {}

    for i, num in enumerate(nums):
        if target - num in storage:
            return [storage[target - num], i]
        else:
            storage[num] = i

nums = [1,3,4,6,10]
target = 4
print(twoSum(nums, target))