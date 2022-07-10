from lib2to3.pgen2.token import RPAR
import sys
sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

def solution(participant, completion):
    dic = {}
    result = ""

    for part in participant:
        # 이름이 중복일 경우
        if part in dic.keys():
            dic[part] += 1
        else:
            dic[part] = 1

    for comp in completion:
        if comp in dic.keys():
            dic[comp] -= 1
    
    for key, value in dic.items():
        if value != 0:
            result = key
            break
    
    return result

participant = input().split()
completion = input().split()
print(solution(participant, completion))

