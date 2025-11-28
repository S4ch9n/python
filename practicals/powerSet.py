# ------------------------------------------------------------
# Practical 8:
# Power set using recursion
# a) Keep only groups with even sum
# b) Arrange groups so the smallest groups come last
# ------------------------------------------------------------

# Recursive function to generate power set
def power_set_recursive(nums, index=0):
    # Base case: when index reaches end
    if index == len(nums):
        return [[]]

    # Recursive call for remaining elements
    subsets = power_set_recursive(nums, index + 1)

    # Add current element to each subset generated
    element = nums[index]
    new_subsets = []

    for subset in subsets:
        new_subsets.append([element] + subset)

    return subsets + new_subsets


# -----------------------------
# Main Program
# -----------------------------
numbers = list(map(int, input("Enter integers separated by space: ").split()))

# Generate power set
power_set = power_set_recursive(numbers)

# (a) Keep only subsets with even sum
even_sum_subsets = [subset for subset in power_set if sum(subset) % 2 == 0]

# (b) Arrange groups so that smallest groups come LAST
# Largest length first → smallest last
sorted_subsets = sorted(even_sum_subsets, key=lambda x: len(x), reverse=True)

# Output
print("\nPower Set (Recursively Generated):")
print(power_set)

print("\nSubsets with Even Sum:")
print(even_sum_subsets)

print("\nFinal Ordered Subsets (Smallest Last):")
print(sorted_subsets)
