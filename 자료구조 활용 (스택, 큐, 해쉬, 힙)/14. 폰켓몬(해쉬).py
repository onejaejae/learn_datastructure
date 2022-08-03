def solution(nums):
    answer = 0
    length = len(nums) // 2

    nums = set(nums)
    if len(nums) >= length:
        answer = length
    else:
        answer = len(nums)

    return answer

print(solution([3,1,2,3]))