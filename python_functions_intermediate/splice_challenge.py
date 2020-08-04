def splice(list_, start, delete_count=None, *items):
    if start >= len(list_):
        start = len(list_) - 1
    if len(list_) + start < 0:
        start = 0
    if delete_count is None: #or delete_count >= len(list_) - start:
        delete_count = len(list_) - start
    removed_elements = list_[start:start + delete_count]
    list_[start:start + delete_count] = items

    return list_, removed_elements


# remove 1 element
nums = [1, 2, 3]
nums, deleted = splice(nums, 0, 1);
print(nums);  # should be [2,3]

# add 1 element
nums = [1, 2, 3]
nums, deleted = splice(nums, 0, 0, 0);
print(nums);  # should be [0,1,2,3]

# add 2 elements
nums = [1, 2, 3]
nums, deleted = splice(nums, 0, 0, -1, 0);
print(nums);  # should be [-1,0,1,2,3]

# replace 1 element
nums = [1, 2, 3]
nums, deleted = splice(nums, 1, 1, 55);
print(nums);  # should be [1,55,3]

# delete all elements from index to end
nums = [1, 2, 3, 4, 5]
nums, deleted = splice(nums, 1);
print(nums);  # should be [1]

# returns list of deleted elements as the second parameter
nums = [1, 2, 3]
nums, deleted = splice(nums, 1);
print(deleted);  # should be [2,3]

# returns an list of the deleted element (1 element)
nums = [1, 2, 3]
nums, deleted = splice(nums, 1, 1);
print(deleted);  # should be [2]

# returns an empty list when no elements are deleted
nums = [1, 2, 3]
nums, deleted = splice(nums, 1, 0, 5);
print(deleted);  # should be []

# delete all but 2 last ones
nums = [1, 2, 3, 4]
nums, deleted = splice(nums, -2);
print(deleted);  # should be [3,4]
