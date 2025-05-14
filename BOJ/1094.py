'''
원래 가지고 있던 막대(64cm)를 자르고 붙여서 최종 X 길이로 만들기
자르는 방법:
    1. 갖고 있는 막대 길이 모두 sum
        sum > X -> 
            가장 짧은 것을 절반으로 자르기
            절반 중 하나를 버리고 남은 막대 길이 sum >= X -> 절반 버림
    2. 남은 모든 막대 붙여서 X 만들기
목표: 몇 개의 막대를 풀로 붙여서 Xcm를 만들 수 있는지
x = 23
64 -> 32, 32 -> 32 > 23, 버리고 남은 막대: 32 -> 16, 16 -> 16 < 23 안버리고 남은 막대: 16, 16 -> 8, 8, 16 -> 8+16 > 23 -> 버리고 남은 막대: 8, 16 -> 반복
'''

X = int(input())
total = []
sum_stick, cur_stick = 64, 64
if X == 64:
    print(1)
else:
    while True:
        if sum_stick > X:
            cur_stick /= 2
            # 절반 중 하나를 버리고: sum_stick - cur_stick
            if sum_stick - cur_stick >= X:
                if sum_stick - cur_stick == X:
                    total.append(cur_stick)
                    break
                sum_stick -= cur_stick
            else:
                total.append(cur_stick)
    print(len(total))

