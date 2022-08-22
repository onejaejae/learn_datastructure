from collections import defaultdict


score = {8:1, 17:1, 20:1, 31:1, 37:1, 39:1, 44:1, 49:1, 60:1, 63:1, 
2:2, 6:2, 10:2, 19:2, 23:2, 25:2, 27:2, 43:2,
13:3, 33:3, 41:3, 52:3, 53:3, 54:3,
55:5, 64:5, 
3:0,4:0,5:0,7:0,9:0,11:0,12:0,14:0,15:0,16:0,18:0,21:0,22:0,24:0,26:0,28:0,29:0,30:0,32:0,34:0,35:0,36:0,38:0,42:0,40:0,
45:0,46:0,47:0,48:0,50:0,51:0,56:0,57:0,58:0,59:0,61:0,62:0
}

def DFS(L, pos, sum):
    global Max
    if pos > m:
        return
    if L == n:
        if pos == m:
            if Max < sum:
                Max = sum
                dic[Max] += res
    else:
        if pos == 12:
            DFS(L+1, 17,sum + score[17])
        elif pos == 32:
            DFS(L+1, 37,sum + score[37])
        elif pos == 39:
            DFS(L+1, 41,sum + score[41])
        elif pos == 49:
            DFS(L+1, 52,sum + score[52])
            DFS(L+1, 56,sum + score[56])
        
        for i in range(1,6+1):
            res[L] = (i, score[pos+i])
            DFS(L+1, pos+i, sum + score[pos+i])

if __name__ == "__main__":
    Max = -216000
    n, m = map(int, input().split())
    res = [0] * n
    dic = defaultdict(list)
    DFS(0,1, 0)
    print(Max)

    start = 1
    end = 1
    for key, value in dic[Max]:

        end += key
        print("Moved from %d to %d (dice = %d, lucci = %d)" %(start,end, key, value))
        start+=key
        