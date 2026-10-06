# 2026.9.30

# 前缀和：从数组开头，一直加到当前位置的总和
def subarraySum(nums, k):
    prefix_sum = 0
    result = 0
    count = {0 : 1}

    for i in range(len(nums)):
        prefix_sum += nums[i]
        need = prefix_sum - k

        if need in count:
            result += count[need]

        count[prefix_sum] = count.get(prefix_sum, 0) + 1

    return result