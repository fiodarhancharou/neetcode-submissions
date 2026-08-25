class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_storage = {}
        for word in strs:
            
            bucket = [0]*26
            for l in word:
                bucket[ord(l) - ord('a')] += 1
            index = tuple(bucket)

            if not index in anagram_storage:
                anagram_storage[index] = [word]
            else:
                anagram_storage[index].append(word)
        return list(anagram_storage.values())