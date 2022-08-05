# 만약에 어떤 번호가 다른 번호의 접두어라면 이 둘은 정렬했을 때 앞뒤에 위치하게 된다.
# 예를 들어 ["1235", "123", "12348", "012"]을 입력으로 받으면, 
# sorted(["1235", "123", "12348", "012"])는 ["012", "123", "12348", "1235"]가 된다.

def solution(phone_book):
    phone_book.sort() # 문자 정렬은 ["119", "1195524421", "97674223"]와 같이 숫자 크기대로 되는 것이 아님.
    print(phone_book)
    for i in range(len(phone_book)):
        if i == len(phone_book)-1:
            break

        # 정렬을 했기 때문에 두 글자만 비교함
        prefix = phone_book[i]
        other_num = phone_book[i+1]
        print(other_num, other_num.index('119'))

        # 접두어가 비교하는 전화번호 맨 앞에 존재할 때
        if prefix in other_num and other_num.index(prefix) == 0:
            return False

    return True

print(solution(["119", "97674223", "1195524421"]))