class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case: If two strs not equal length, return false
        if len(s) != len(t):
            return False

        # Create dict (hashmap) for O(1) insertion
        # Add all chars from both s and t as keys
        # Each entry value represents total count of the char
        # Return true if all values are even

        s_count_dict = {}
        t_count_dict = {}
        
        # Helper function to create count dict for each str
        # Key: chars in str; Value: # of appearances in str
        def process_dict(current_str, count_dict):
            for c in current_str:
                if c in count_dict:
                    count_dict[c] += 1
                else:
                    count_dict[c] = 1

        process_dict(s, s_count_dict)
        process_dict(t, t_count_dict)   

        # Total runtime: O(n + m)
        return s_count_dict == t_count_dict