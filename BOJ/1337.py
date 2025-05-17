'''
정렬 시 5개가 연속
투포인터로 연속된 숫자를 만들 수 있는 구간 찾기 
-> 5개 연속이니까 작은값(시작) - 큰값(끝) == 4
-> 끝-시작 <= 4: 가능, 추가할 값 카운트
최소 개수를 구해야되니까 모든 원소에 대해서 구간찾고 카운트 반복해서 min 갱신
목표: 추가할 원소의 최소 개수
'''
N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

result = float('inf')
for i in range(N):
    s, e = i, N - 1
    while True:
        if nums[e] - nums[s] >= 5:
            e -= 1
        elif nums[e] - nums[s] <= 4:
            result = min(result, 5 - len(nums[s: e+1]))
            break
print(result)