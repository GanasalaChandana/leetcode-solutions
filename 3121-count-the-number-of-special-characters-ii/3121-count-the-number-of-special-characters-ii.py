class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper = [float('inf')] * 26  # first occurence of uppercase
        last_lower = [-1] * 26 # last occurence of lowercase

        for i,c in enumerate(word):
            if c.islower():
                last_lower[ord(c)-ord('a')] = i
            else:
                idx = ord(c) - ord('A')
                first_upper[idx] = min(first_upper[idx],i)
        count = 0
        for i in range(26):
            if(last_lower[i] != -1 
               and first_upper[i] != float('inf') 
               and last_lower[i] < first_upper[i]):
                count += 1
        return count

