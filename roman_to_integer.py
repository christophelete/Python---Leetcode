class Solution:
    def romanToInt(self, s: str) -> int:
        summer = 0
            
        roman = {'I': 1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M' : 1000}

        for idx, num in enumerate(s):
            if num == 'I' and idx < len(s)-1:
                if s[idx+1] == 'V' or s[idx+1] == 'X':
                    summer -= roman[num]
                else:
                    summer += roman[num]

            elif num == 'X' and idx < len(s)-1:
                if s[idx+1] == 'L' or s[idx+1] == 'C':
                    summer -= roman[num]

                else:
                    summer += roman[num]

            elif num == 'C' and idx < len(s)-1:
                if s[idx+1] == 'D' or s[idx+1] == 'M':
                    summer -= roman[num]

                else:
                    summer += roman[num]

            else:
                summer += roman[num]
        return summer
