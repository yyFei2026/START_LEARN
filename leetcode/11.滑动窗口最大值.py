# 2026.9.30

'''
单调队列
'''


def maxSlidingWindow(nums, k):
    from collections import deque
    queue = deque()  # 存下标；对应的 nums 值从队首到队尾递减
    result = []

    for right in range(len(nums)):
# 队列两条规则；
# 如果新数字进来前，删除队伍中所有比他小或相等的数字
# 如果队首的下标不在窗口范围了，删除队首

        # 新元素 nums[right] 更大时，
        # 队尾较小元素以后不可能成为窗口最大值，删除它们
        while queue and nums[queue[-1]] <= nums[right]:
            queue.pop()

        # 加入当前元素的下标
        queue.append(right)

        # 当前窗口左边界
        left = right - k + 1

        # 队首下标已经离开窗口，则删除
        if queue[0] < left:
            queue.popleft()

        # 只有窗口长度达到 k 时，才记录答案
        if right >= k - 1:
            result.append(nums[queue[0]])

    return result

'''
def maxSlidingWindow(nums, k):
    result = []
    window = nums[:k]
    result.append(max(window))

    for i in range(k, len(nums)):
        
        window.append(nums[i])
        window.pop(0)

        result.append(max(window))

    return result
'''

nums = [1]
k = 1
print(maxSlidingWindow(nums, k))