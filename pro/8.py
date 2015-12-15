class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip().replace(' ', '')
        if str == '':
            return 0

        flag = '+'
        i = 0
        if str[0] == '-':
            i += 1
            flag = '-'
        elif str[0] == '+':
            i += 1
        result = 0
        while i < len(str):
            if '0' <= str[i] <= '9':
                result = result * 10 + (ord(str[i]) - 48)
            else:
                return 0
            i += 1

        MAX_INT = 1 << 31 - 1
        MIN_INT = -1 * (1 << 31)
        if result > MAX_INT:
            return MAX_INT
        if result < MIN_INT:
            return MIN_INT
        if flag == '-':
            return -1 * result

        return result

s = Solution()
print s.myAtoi('+')