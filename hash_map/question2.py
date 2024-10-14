def subarray_sum(nums, target):
    hash = {}
    for idx, x in enumerate(nums):
        result = x
        for j in range(idx + 1, len(nums)):
            result = result + j
            if result > target:
                pass
            if result == target:
                return [idx, j]
            if result < target:
                break

    print(hash)


nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))

# nums = [-1, 2, 3, -4, 5]
# target = 0
# print(subarray_sum(nums, target))
#
# nums = [2, 3, 4, 5, 6]
# target = 3
# print(subarray_sum(nums, target))
#
# nums = []
# target = 0
# print(subarray_sum(nums, target))
