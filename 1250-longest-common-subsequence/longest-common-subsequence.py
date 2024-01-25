class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mat=[[0 for x in range(len(text1)+1)] for x in range(len(text2)+1)]
        
        # print(mat)

        text1,text2='0'+text1,'0'+text2
        for i in range(1,len(text2)):
            for j in range(1,len(text1)):
                if text2[i] == text1[j]:
                    mat[i][j]=mat[i-1][j-1]+1
                else:
                    mat[i][j]=max(mat[i-1][j],mat[i][j-1])
        
        # for x in mat:
        #     for y in x:
        #         print(y,end=" ")
        #     print()
        
        return mat[-1][-1]