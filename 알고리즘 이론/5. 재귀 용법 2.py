import random
import string

def multiple(num):
    return_value = 1
    for index in range(1, num+1):
        return_value = return_value * index
    return return_value

def multiple2(num):
    if num <= 1:
        return num
    return num * multiple2(num -1)

def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_list(data[1:])

data = random.sample(range(100), 10)
print(data)
print(sum_list(data))

# 회문은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함
# 회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만드세요
def palindrome(str):
    for i in range(len(str)):
        if str[i] != str[-i+-1]:
            return False
    
    return True

def palindrome2(str):
    if len(str) <= 1:
        return True
    
    if str[0] == str[-1]:
        return palindrome2(str[1:-1])
    else:
        return False


print(palindrome('levedl'))