class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sort_costs = self.counting_sort(costs)
        result = 0
        for cost in sort_costs:
            if coins < cost:
                break

            coins -= cost
            result += 1
            
        return result
    
    def counting_sort(self, arr:List[int])->List[int]:
        count = [0]*(max(arr)+1)
        result = [0]*len(arr)
        for i in arr:
            count[i] += 1
        
        for i in range(1, len(count)):
            count[i] += count[i-1]
        
        for i in range(len(arr)-1, -1, -1):
            num = arr[i]
            idx = count[num]
            result[idx-1] = num
            count[num] -= 1
        
        return result