class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        v = collections.Counter(arr)
        print(collections.Counter(v.values()))
        return len(collections.Counter(v.values())) == len(v)
        