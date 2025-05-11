'''
값이 쌀 때 사서 비쌀 때 팔아야됨
for i in N에서 다음날 값이 현재보다 싸면 최소주문 갱신, 비싸면 팔고 최대이익보다 크면 갱신신
'''
N = int(input())
prices = list(map(int, input().split()))

min_price = prices[0]
max_profit = 0

for i in range(1, N):
    if prices[i] < min_price:
        min_price = prices[i]
    elif prices[i] > min_price:
        max_profit = max(max_profit, prices[i] - min_price)

print(max_profit)