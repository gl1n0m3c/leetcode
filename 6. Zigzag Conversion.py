def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    
    numCol = 0
    step = 2*(numRows - 1)
    ans = ""

    for i in range(0, len(s), step):
        ans += s[i]

    i = 1
    delta = step - 2
    while i < numRows - 1:
        j = i
        while j < len(s):   
            ans += s[j]
            if j + delta < len(s):
                ans += s[j + delta]
            j += step

        delta -= 2
        i += 1

    for i in range(numRows - 1, len(s), step):
        ans += s[i]

    return ans



print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 4))