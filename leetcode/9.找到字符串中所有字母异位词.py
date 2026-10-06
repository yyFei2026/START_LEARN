# 2026.9.29

def findAnagrams(s, p):
    from collections import Counter

    result = []
    window = Counter(s[:len(p)])

    if window == Counter(p):
        result.append(0)

    for right in range(len(p), len(s)):
        left = right - len(p)

        out_char = s[left]
        in_char = s[right]

        window[out_char] -= 1

        if window[out_char] == 0:
            del window[out_char]
        
        window[in_char] += 1

        if window == Counter(p):
            result.append(left + 1)

    return result