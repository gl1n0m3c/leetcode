class Solution:
    ans = []

    def recursion(self, digits: str, s: str, flag: bool = False):
        if len(digits) == 0:
            return None
        
        arr = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        for i in range(len(arr[int(digits[0]) - 2])):
            if flag:
                s = arr[int(digits[0]) - 2][i]
                val = ""
            else: 
                val = arr[int(digits[0]) - 2][i]

            if len(digits) > 1:
                self.recursion(digits[1:], s + val)
            else:
                Solution.ans.append(s + val)


    def letterCombinations(self, digits: str) -> list[str]:
        self.recursion(digits, "", True)
        rez = Solution.ans
        Solution.ans = []
        return rez
