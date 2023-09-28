def longestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s
    
    ans   = ""
    ans_l = 0
    alp = {}
    for i in range(32, 127):
        alp[chr(i)] = []

    for i in range(len(s)):
        if alp[s[i]] != []:
            for j in alp[s[i]]:
                string = s[j:i+1]
                if (string == string[::-1]) and (ans_l < len(string)):
                    ans_l = len(string)
                    ans = string


        alp[s[i]].append(i)
    
    if ans == "":
        ans = s[0]

    return ans


print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
# print(longestPalindrome("babad"))