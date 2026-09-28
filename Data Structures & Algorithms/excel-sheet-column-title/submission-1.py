class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret = ""

        while(columnNumber > 0):
            columnNumber -= 1
            rem = columnNumber % 26
            ret += chr(ord('A') + rem)
            columnNumber //= 26

        return ret[::-1]