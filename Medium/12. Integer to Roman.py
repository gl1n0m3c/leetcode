def intToRoman(num: int) -> str:
    ans = ''
    s = str(num)
    rez = [
        ['I', 'V', 'X'],
        ['X', 'L', 'C'],
        ['C', 'D', 'M'],
        ['M'] 
        ]
    
    for i in range(len(s)):
        el = int(s[-i - 1])

        if 0 <= el <= 3:
            ans = rez[i][0]*el + ans
        elif el == 4:
            ans = rez[i][0] + rez[i][1] + ans
        elif el == 5:
            ans = rez[i][1] + ans
        elif 6 <= el <= 8:
            ans = rez[i][1] + rez[i][0]*(el - 5) + ans
        elif el == 9:
            ans = rez[i][0] + rez[i][2] + ans

    return ans

print(intToRoman(1994))
print(intToRoman(58))
print(intToRoman(3))
