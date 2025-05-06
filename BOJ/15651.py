'''
같은 수를 여러 번 골라도 된다. ==> 방문 처리할 필요가 없음
'''
def dfs(n, nums):
    if n == M:
        answer.append(nums)
        return
    
    for i in range(1, N + 1):
        dfs(n + 1, nums + [i ])

N, M = map(int, input().split())
answer = []
dfs(0, [])
for a in answer:
    print(*a)