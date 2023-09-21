def lengthOfLongestSubstring(s: str) -> int:
    ans = l = 0
    alp = {}

    for i in range(97, 123):
        alp[chr(i)] = 0

    for i in range(32, 91):
        alp[chr(i)] = 0


    for i in range(len(s)):
        l += 1
        if alp[s[i]] != 0:
            n = alp[s[i]]
            for key in alp:
                if alp[key] <= n:
                    alp[key] = 0
                else:
                    alp[key] -= n

            l -= n
            alp[s[i]] = l


        
        ans = max(ans, l)
        alp[s[i]] = l


    return ans




print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))
print(lengthOfLongestSubstring("aabaab!bb"))
print(lengthOfLongestSubstring("cbarabcfa"))