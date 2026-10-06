# 第一次做：2026.9.27

def longestConsecutive(nums):
    set_nums = set(nums)
    longest = 0

    for num in set_nums:
        if num - 1 not in set_nums:
            current = num
            length = 1

            while current + 1 in set_nums:
                current += 1
                length += 1

            longest = max(longest, length)
    
    return longest

nums = [0, -1]
print(longestConsecutive(nums))