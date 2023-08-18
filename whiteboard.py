# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
# constraints: 
# cannot use .count()

def solution(arr):
    result = 0

    for num in arr:
        result ^= num

    return result

def solution(nums):
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    for num in count:
        if count[num] % 2 != 0:
            return num
        

def solution(lst):
    empty_dict = {}
    for num in lst:
        if num in empty_dict:
            empty_dict[num] += 1
        else:
            empty_dict[num] = 1
    for k, v in empty_dict.items():
        if v % 2 != 0:
            return k