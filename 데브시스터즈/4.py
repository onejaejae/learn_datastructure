def solution(join_date, resign_date, holidays):
    leap_year = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11:30, 12:31}

    join_date_year, join_date_month, join_date = join_date.split("/")
    join_date_day, join_date_date = join_date.split(" ")

    resign_date_year, resign_date_month, resign_date_day = resign_date.split("/")
    

solution("2019/12/01 SUN", "2019/12/31", ["12/25"])