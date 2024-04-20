class Solution:
    def longestCommonPrefix(self, strs) -> str:
        d_len = {len(word) : index for index, word in enumerate(strs)}
        smallest = strs[d_len[min(d_len.keys())]]
        index = 0
        subs = ""
        while index < len(smallest):
            for word in strs:
                if not smallest[index] == word[index]:
                    return subs
            subs += smallest[index]
            index+= 1
        return subs

s  = Solution()
print(s.longestCommonPrefix(["ab", "a"]))
