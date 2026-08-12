class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        save={}
        for word in strs:
            sorted_word= tuple(sorted(word))
            if sorted_word in save:
                save[sorted_word].append(word)
            else:
                save[sorted_word]=[word]
        return list(save.values())
        