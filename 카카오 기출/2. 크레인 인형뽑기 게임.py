from collections import defaultdict

def solution(board, moves):
    answer = 0
    result = defaultdict(list)
    bucket = []

    for i in range(len(board)):
        for j in range(len(board)):
            result[j].append(board[i][j]) 

    result = list(result.values())
    print(result)
   
    for m in moves:
        for j in range(len(result[m-1])): 
            if result[m-1][j] != 0:
                if bucket and bucket[-1] == result[m-1][j]:
                    result[m-1][j]=0
                    bucket.pop()
                    answer+=2
                    break
                bucket.append(result[m-1][j])
                result[m-1][j]=0
                break
        
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))