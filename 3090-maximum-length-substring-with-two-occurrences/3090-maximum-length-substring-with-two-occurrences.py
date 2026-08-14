class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        start=0
        lst=[]
        save={}
        maxm=0

        for end in range(start,len(s)):
            save[s[end]]=save.get(s[end],0)+1

            while save[s[end]]>2:
                lst.append(s[start:end])
                save[s[start]]-=1
                start+=1

            maxm=max(maxm,end-start+1)

        return maxm

