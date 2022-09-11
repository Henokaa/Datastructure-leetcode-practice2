class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        weak  = 0
        INF = 10 ** 20
        
        properties.sort(key = lambda x: (-x[0], x[1]))
        print(properties)
        mx = - INF
        for attack, defense in properties:
            if defense < mx:
                weak += 1
            mx = max(defense, mx)
            print(mx)
        return weak