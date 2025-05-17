'''
이번 해가 얼마나 지났는지
목표: 오늘 날짜가 주어지고 이번 해가 몇% 지났는지, 퍼센트!!
평년마다 달의 일 수가 다름
윤년의 2월: 29일
윤년: 연도 % 400 == 0 or (연도 % 4 == 0 and 연도 % 100 != 0)
평년인지 윤년인지 체크 -> 윤년: 연도 % 400 
다 같은 단위로 변환 !!!!, 모두 분으로 변환
연도 -> 일 수 * 24 * 60
월 -> (5월 10일이면, 1~4월 + 10일) * 24 * 60
시간 -> * 60
분 -> + 분
위 결과들 합 / 분으로 변환한 연도도
'''

month, day, year, time = input().split()

all_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
all_month = {i: idx for idx, i in enumerate(all_month)}

year = int(year)
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0): # 2월이 29일까지있음 -> 1년: 366일
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year2min = 366 * 24 * 60
else:
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year2min = 365 * 24 * 60

sum_days = 0
for i in range(12):
    if i == all_month[month]:
        break
    sum_days += days[i]
sum_days += int(day.replace(',', '')) - 1 # , 제거

day2min = sum_days * 24 * 60

h, m = map(int, time.split(':'))
h2min = h * 60

elapsed = day2min + h2min + m
print(elapsed / year2min * 100)

