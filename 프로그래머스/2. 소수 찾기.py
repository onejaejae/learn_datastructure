from itertools import permutations
import math

# https://dev-note-97.tistory.com/99
# https://school.programmers.co.kr/learn/courses/4008/lessons/12836

def solution(numbers):
    nums = [n for n in numbers]
    per = []
    answer = []

    for i in range(1, len(numbers) + 1):
        per += list(permutations(nums, i))

    new_nums = [int(("").join(p)) for p in per] 
    new_nums = list(set(new_nums))

    for n in new_nums:
        if n < 2:
            continue
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                break
        else:
            answer.append(n)

    return len(answer)


print(solution("011"))