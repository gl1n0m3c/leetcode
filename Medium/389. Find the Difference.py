# гинеальный способ через сумму ascii
def findTheDifference(self, s: str, t: str) -> str:
        s1 = s2 = 0

        for el in s:
            s1 += ord(el)
        
        for el in t:
            s2 += ord(el)

        return chr(s2 - s1)
