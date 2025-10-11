class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0], x[1]))
        result = []
        for h, k in people:
            result.insert(k, [h,k])
            
        return result
