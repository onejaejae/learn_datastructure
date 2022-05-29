def factorial(num):
    if num > 1:
        return num * factorial(num-1)
    else:
        return num

def factorial2(num):
    if num <= 1:
        return num
    
    return num * factorial2(num-1)

for num in range(10):
    print(factorial(num)) 
