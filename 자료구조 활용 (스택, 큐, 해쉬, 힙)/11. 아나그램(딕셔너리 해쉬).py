import sys
sys.stdin = open("C:\workspaces\자료구조\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

# dic1 = dict()
# dic2 = dict()

# string1 = input()
# string2 = input()

# for s in string1:
#     dic1[s] = 0

# for s in string2:
#     dic2[s] = 0

# for s in string1:
#     dic1[s] += 1
# for s in string2:
#     dic2[s] += 1

# dic1 = sorted(dic1.items())
# dic2 = sorted(dic2.items())

# for i in range(len(dic1)):
#     if dic1[i][1] != dic2[i][1]:
#         print("NO")
#         break
# else:
#     print("YES")

# 해설 풀이
dic1 = dict()
dic2 = dict()

string1 = input()
string2 = input()

for s in string1:
    dic1[s] = dic1.get(s, 0) + 1
for s in string2:
    dic2[s] = dic2.get(s, 0) + 1

for i in dic1.keys():
    if i in dic2.keys():
        if dic1[i] != dic2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")