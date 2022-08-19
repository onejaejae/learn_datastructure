def solution(cacheSize, cities):
    res = []
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        if city.upper() in res:
            answer += 1
            res.append(res.pop(res.index(city.upper())))
        else:
            if len(res) == cacheSize:
                res.pop(0)
                res.append(city.upper())
                answer += 5
            else:
                res.append(city.upper())
                answer += 5
    return answer

print(solution(	0, 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))