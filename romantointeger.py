class Solution:
    def romanToInt(self, s):
        def value(c):
            if c == "I": return 1
            if c == "V": return 5
            if c == "X": return 10
            if c == "L": return 50
            if c == "C": return 100
            if c == "D": return 500
            if c == "M": return 1000
            return 0
        total = 0
        n = len(s)
        for i in range(n):
            v = value(s[i])
            if i < n - 1 and v < value(s[i + 1]):
                total -= v
            else:
                total += v
        return total
