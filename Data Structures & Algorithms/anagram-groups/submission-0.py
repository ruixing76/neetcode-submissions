class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dict=defaultdict(list)
        for str in strs:
            sorted_str="".join(sorted(str))
            hash_dict[sorted_str].append(str)
        return list(hash_dict.values())