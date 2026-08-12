class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        save={}
        for item in nums:
            save[item]=save.get(item,0)+1
        sorted_dict = dict(sorted(save.items(), key=lambda item: item[1]))
        difference=len(sorted_dict)-k

        return list(sorted_dict.keys())[difference:]


        