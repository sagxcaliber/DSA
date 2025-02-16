def find_is_it_common(list1, list2):
    hash = {}
    for x in list1:
        hash[x] = True

    for x in list2:
        if hash.get(x):
            return True

    return False


l = [1, 3, 5]
l2 = [2, 4, 5]


# print(find_is_it_common(l, l2))
def find_duplicates(list1):
    hash = {}
    for x in list1:
        if x not in hash:
            hash[x] = False
        else:
            hash[x] = True

    return [key for key, value in hash.items() if value == True]


# print(find_duplicates([1, 2, 3, 4, 5]))
# print(find_duplicates([1, 1, 2, 2, 3]))
# print(find_duplicates([1, 1, 1, 1, 1]))
# print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
# print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
# print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
# print(find_duplicates([]))
def first_non_repeating_char(st):
    hash = {}

    for x in st:
        if x not in hash:
            hash[x] = False
        else:
            hash[x] = True
    print(hash)
    for key, value in hash.items():
        if value is False:
            return key


# print(first_non_repeating_char('leetcode'))
#
# print(first_non_repeating_char('hhello'))
#
# print(first_non_repeating_char('aabbcc'))
def group_anagrams(lst):
    obj = []
    for x in range(len(lst)):  # [eat,tea]
        obj1 = []
        new_v = ""
        # {'e': True, 'a': True, 't': True}
        if x not in obj1:
            hash = {x: True for x in lst[x]}
            for j in lst[x]:
                if j in hash:
                    new_v = new_v + j
                else:
                    print('@@@ its breaking with ', j)
                    break
            print(new_v)
            obj1.append(new_v)
    print('here i am')
    obj.append(obj1)


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# print("\n2nd set:")
# print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))
#
# print("\n3rd set:")
# print(group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))
