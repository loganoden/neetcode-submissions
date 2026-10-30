class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Index Tuple, [Anagrams]
        sorted_and_anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1
            
            sorted_and_anagrams[tuple(count)].append(s)
        
        return list(sorted_and_anagrams.values())