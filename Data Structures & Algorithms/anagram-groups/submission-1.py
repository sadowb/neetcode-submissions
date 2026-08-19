class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for word in strs:
            sorted_words = ''.join(sorted(word))
            if sorted_words not in grouped :
                grouped[sorted_words] = []
            grouped[sorted_words].append(word)
            print(grouped)
        return list(grouped.values())
         