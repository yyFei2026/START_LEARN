# 2026.9.28

def lengthOfLongestSubstring(s):
    left = 0
    ans = 0
    last_index = {}

    for right, char in enumerate(s):
        if char in last_index:
            left = max(left, last_index[char] + 1)

        last_index[char] = right

        ans = max(ans, right - left + 1)
    return ans