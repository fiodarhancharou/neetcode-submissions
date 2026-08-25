class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_storage = {}
        for word in strs:
            index = "".join(sorted(word))
            if not index in anagram_storage:
                anagram_storage[index] = [word]
            else:
                anagram_storage[index].append(word)
        return list(anagram_storage.values())