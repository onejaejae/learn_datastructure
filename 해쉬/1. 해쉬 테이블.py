# 간단한 해쉬 테이블 만들기
hash_table = list([0 for i in range(10)])
print(hash_table)

# 간단한 해쉬 함수 만들기
def hash_func(key):
    return key%5

# 해쉬 테이블에 데이터 저장
data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

# ord(): 문자의 ASCII(아스키) 코드 리턴
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))

# 해쉬 테이블에 값 저장
def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

# 해쉬 테이블에서 특정 주소의 데이터를 가져오는 함수 만들기
storage_data('Andy','01055553333')
storage_data('Dave','01055554444') 
storage_data('Trump','01055552222')

# 실제 데이터를 저장하고, 읽기
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data('Andy'))