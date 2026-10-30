class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sorted Key, [Anagrams]
        sorted_and_anagrams = defaultdict(list)

        for s in strs:
            sorted_key = "".join(sorted(s))
            sorted_and_anagrams[sorted_key].append(s)
        
        return list(sorted_and_anagrams.values())

                