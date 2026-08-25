class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_storage = {}
        for word in strs:
            
            bucket = {}
            for l in word:
                bucket[l] = bucket.get(l,0) + 1 
            index = tuple(sorted(bucket.items()))

            if not index in anagram_storage:
                anagram_storage[index] = [word]
            else:
                anagram_storage[index].append(word)
        return list(anagram_storage.values())