class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        aws = ""
        for i in range(len(s)-1):
            l = i-1
            r = i+1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l-=1
                r+=1
            if len(s[l+1:r]) > len(aws):
                aws = s[l+1:r]
            l = i
            r = i+1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l-=1
                r+=1
            if len(s[l+1:r]) > len(aws):
                aws = s[l+1:r]
        if aws == "" and s != "":
            aws = s[0]
        
        return aws