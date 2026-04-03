class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt={}
        for i,v in enumerate(strs):
            new_sorted_srt=tuple(sorted(v))
            if new_sorted_srt in dictt:
                dictt[new_sorted_srt].append(v)
            else:
                dictt[new_sorted_srt]=[v]
        return list(dictt.values())            
        