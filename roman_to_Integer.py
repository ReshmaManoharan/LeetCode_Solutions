class Solution:
    def romanToInt(self, s: str) -> int:
        index = 1
        symbol_map = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        num = symbol_map[s[0]]
        #import pdb;pdb.set_trace()
        while index < len(s):
            if s[index-1] == "I" and (s[index] == "V"  or s[index] == "X"):
                num = num + symbol_map[s[index]] - 2
            elif s[index-1] == "X" and (s[index] == "L"  or s[index] == "C"):
                num = num + symbol_map[s[index]] - 20
            elif s[index-1] == "C" and (s[index] == "D"  or s[index] == "M"):
                num = num + symbol_map[s[index]] - 200
            else:
                num += symbol_map[s[index]]
            index += 1
        return num
    
s = Solution()
print(s.romanToInt("MMMCDXC"))
