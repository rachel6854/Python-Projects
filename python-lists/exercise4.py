nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4]
print(len(nums))
num_to_remove = 4
flag=0
if num_to_remove in nums:
    if nums.count(num_to_remove) > 1:
        for index, num in enumerate(nums):
            if num == num_to_remove:
                if flag == 0:
                    flag = 1
                else:
                    nums.pop(index)
                    break
print(nums)
print(len(nums))
