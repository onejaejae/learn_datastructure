# https://variety82p.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%EC%B2%B4%EC%9C%A1%EB%B3%B5-%ED%8C%8C%EC%9D%B4%EC%8D%ACpython
# 예외 case
# n = 5
# lost = [2, 4], reserve = [3, 1]

# 정상적인 상황이라면 1번 학생이 2번에게 3번 학생이 4번에게 빌려 줄 수 있으나, 
# 정렬을 하지 않는다면 3번이 2번에게 빌려주어 4번 학생은 빌릴 수가 없게되므로 처음에 reserve를 정렬하는 과정이 필요하다

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    _reserve.sort()
    _lost.sort()
    for r in _reserve:
        f = r-1
        b = r+1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)

    return n - len(_lost)

print(solution(5, [2], [1,3,5]))