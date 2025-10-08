def find_pairs(arr, target):
    pairs = []
    seen = set()
    for num in arr:
        diff = target - num
        if diff in seen:
            pairs.append((num, diff))
        seen.add(num)
    return pairs

nums = [1, 3, 2, 2, 4, 5, 0]
target = 4
print(find_pairs(nums, target))
# Output: [(3, 1), (2, 2), (4, 0)]
