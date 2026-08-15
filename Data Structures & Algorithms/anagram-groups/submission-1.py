class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Complexity, if each word has average length k and there are n words:
        # sorting each word: O(k log k)
        # across all words: O(n k log k)
        # space: O(nk) for the grouped strings/keys

        groups = {}

        for word in strs:
            key = ''.join(sorted(word))
            
            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)

        return list(groups.values())

