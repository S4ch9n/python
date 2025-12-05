from itertools import combinations


def odd_sum_subsets(nums):
    power_set = []

    # generate all subsets
    for r in range(len(nums) + 1):
        for combo in combinations(nums, r):
            if sum(combo) % 2 == 1:  # keep only odd-sum subsets
                power_set.append(list(combo))

    return power_set


# Example
nums = [1, 2, 3]
result = odd_sum_subsets(nums)
print(result)
