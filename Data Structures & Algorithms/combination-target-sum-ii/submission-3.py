class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def solve(candidates, target, start, path):
            if target == 0:
                result.append(path.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                solve(candidates, target - candidates[i], i + 1, path)
                path.pop()

        solve(candidates, target, 0, [])
        return result