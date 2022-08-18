
def solution(dirs):
    command = {'U' : [0,1], 'D': [0,-1], 'R' : [1,0], 'L' : [-1,0]}
    road = set()
    x=y=0

    for d in dirs:
        next_x , next_y = command[d][0] + x, command[d][1] + y
        if -5 <= x <= 5 and -5 <= y <= 5:
            road

print(solution("ULURRDLLU"))