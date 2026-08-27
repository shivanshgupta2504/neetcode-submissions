class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in hashmap:
                hashmap[tuple(count)] = [s]
            else:
                hashmap[tuple(count)].append(s)
        return [value for value in hashmap.values()]