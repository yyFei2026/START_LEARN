# 第一次做：2026.9.26

def groupAnagrams(strs):
    groups = {}
    result = []

    for word in strs:
        key = tuple(sorted(word))
        if key not in groups:
            groups[key] =  []

        groups[key].append(word)

    return list(groups.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs = strs))
