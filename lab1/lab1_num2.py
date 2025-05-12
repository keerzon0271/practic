def combination_sum2(candidates, target):
    candidates.sort()
    results = []

    def dfs(start, target, path):
        if target == 0:
            results.append(path)
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            dfs(i + 1, target - candidates[i], path + [candidates[i]])

    dfs(0, target, [])
    return results

candidates1 = [2,5,2,1,2]
target1 = 5
print(combination_sum2(candidates1, target1))

candidates2 = [10,1,2,7,6,1,5]
target2 = 8
print(combination_sum2(candidates2, target2))

