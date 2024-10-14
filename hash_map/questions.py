# def two_sum(lst, target):
#     hash = {}
#
#     final_lst = []
#     for idx, value in enumerate(lst):
#         hash[value] = idx
#     print(hash)
#     for y in lst:
#         rem = target - y
#         if rem >= 0 and rem in lst and hash[y] != hash[rem]:
#             final_lst.append(hash[y])
#             final_lst.append(hash[rem])
#             break
#
#     return final_lst


def two_sum(nums, target):
    new_num = {}
    for idx, value in enumerate(nums):
        rem = target - value
        if rem in new_num:
            return [new_num[rem], idx]
        new_num[value] = idx
    return []

print(two_sum([5, 1, 5, 2, 9, 3], 10))
print(two_sum([4, 2, 11, 7, 6, 3], 9))
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
print(two_sum([1, 3, 5, 7, 9], 10))
print(two_sum([1, 2, 3, 4, 5], 10))
print(two_sum([1, 2, 3, 4, 5], 7))
print(two_sum([1, 2, 3, 4, 5], 3))
print(two_sum([], 0))
