class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dict=defaultdict(list)
        for str in strs:
            count=[0]*26
            for c in str:
                count[ord(c)-ord('a')]+=1
            hash_dict[tuple(count)].append(str)
        return list(hash_dict.values())