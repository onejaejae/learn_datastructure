def solution(strings, n):
    return sorted(strings, key=lambda s:(s[n], s))

print(solution(["sun", "bed", "car"], 1))