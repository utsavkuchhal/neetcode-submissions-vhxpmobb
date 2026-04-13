class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        num1, num2, num3 = target
        ans1, ans2, ans3 = -1, -1, -1
        for index in range(n):
            curr1, curr2, curr3 = triplets[index]
            if curr1 <= num1 and curr2 <= num2 and curr3 <= num3:
                ans1 = max(ans1, curr1)
                ans2 = max(ans2, curr2)
                ans3 = max(ans3, curr3)
        
        return (ans1, ans2, ans3) == tuple(target)


            