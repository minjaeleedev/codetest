class Solution:
    def countValidWords(self, sentence: str) -> int:
        ls = sentence.split()
        ans = 0
        for i in ls:
            if(len(i)>0):
                flag = 0
                punc = 0
                hyphen=0
                hyphenindex=0
                ind =0
                for j in i:
                    if(j=='-'):
                        hyphen+=1
                        hyphenindex=ind
                    if(j in "!.,"):
                        punc+=1
                    if(j in "0123456789"):
                        flag=1
                    ind+=1
                if(punc==1):
                    v  = i[-1]
                    if(v not in "!.,"):
                        flag=1
                if(hyphen==1):
                    v  = i[0]
                    vv = i[-1]
                    if(v=='-' or vv=='-'):
                        flag=1
                    if(hyphenindex >0 and (i[hyphenindex-1]<'a' or i[hyphenindex-1]>'z')):
                        flag=1
                    if(hyphenindex<len(i)-1 and (i[hyphenindex+1]<'a' or i[hyphenindex+1]>'z')):
                        flag=1
                if(hyphen<=1 and punc<=1 and flag==0):
                    ans+=1
        return ans
