class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        encoded_str = ""
        for s in strs:
            len_of_s = len(s)
            encoded_str += str(len_of_s) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        n = len(s)
        i = 0
        prev = 0
        while i < n:
            if s[i] == "#":
                number = int(s[prev:i])
                word = s[i+1:i+1+number]
                strs.append(word)
                i = i+1+number
                prev = i
            i += 1
        return strs
