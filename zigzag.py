class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0:
            return ""
        elif len(s) <= numRows or numRows == 1:
            aws = ''
            for i in s:
                aws = aws + i
            return aws
        len_arr = numRows*2 - 2
        aws = []
        total = len(s) // len_arr
        for i in range(total):
            aws.append([s[j] for j in range(i*len_arr,i*len_arr+len_arr)])
        aws.append([s[j] for j in range(total*len_arr, len(s))])
        for _ in range(len(aws[len(aws)-1]),len_arr):
            aws[len(aws)-1].append(0)
        output = ''
        if len_arr %2 == 0:
            for j in range(len_arr//2 + 1):
                if  j == 0 or j == len_arr//2:
                    for x in range(len(aws)):
                        output = output + str(aws[x][j])
                else:
                    for x in range(len(aws)):
                        output = output + str(aws[x][j])
                        output = output + str(aws[x][len_arr - j])
        else:
            for j in range(len_arr//2 + 2):
                if  j == 0 or j == len_arr//2:
                    for x in range(len(aws)):
                        output = output + str(aws[x][j])
                else:
                    for x in range(len(aws)):
                        output = output + str(aws[x][j])
                        output = output + str(aws[x][len_arr - j])
        real_output = ''
        for i in output:    
            if i.isdigit() == False:
                real_output = real_output + i
        return real_output