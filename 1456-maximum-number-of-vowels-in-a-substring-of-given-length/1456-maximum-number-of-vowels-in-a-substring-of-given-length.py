class Solution:
    """
    leetcode, ans=2
    iteration1, [r=l,l=l], NO NO move
    iteration2, [r=e, l=l], hsh2={e:1}, No
    iteration3, [r=e, l=l],hsh2={e:2}, yes, so now maxcount=max(0,2)=2, hsh2={e:1}
    iteration4, [r=t, l=e], move
    iteration5, [r=c, l=e], move
    iteration6, [r=o, l=e], hsh2={o:1, e:1}, maxcount=(max(2,2)=2, hsh2={o:1}
    iteration7, [r=d, l=e], move
    iteration8, [r=e, l=e], hsh2={o:1, e:2}

    """
    def maxVowels(self, s: str, k: int) -> int:
        hsh={"a", "e", "i", "o", "u"}
        maxcount=0
        left=0
        hsh2={}
        for right in range(len(s)):
            if s[right] in hsh:
                hsh2[s[right]]=hsh2.get(s[right],0)+1
            if right-left+1==k:
                maxcount=max(maxcount, sum(hsh2.values()))
                if s[left] in hsh:
                    hsh2[s[left]]=hsh2.get(s[left],0)-1
                    if hsh2[s[left]]==0:
                        del hsh2[s[left]]
                left+=1
        return maxcount

            
        