'''
1 ~ N 중 중복 없이 M개 고르기
0개를 고르는 경우 1개를 고르는 경우 2개를 고르는 경우 ... M-1개를 고르는 경우 탐색
종료조건: 수열길이 == M
==> 1부터 N까지의 수로 이루어진 길이 M의 순열
'''
def dfs(n, nums): # 길이, 순열
    if n == M:
        answer.append(nums)
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            dfs(n+1, nums + [i])
            visited[i] = False

N, M = map(int, input().split())
visited = [False] * (N + 1)
answer = []
dfs(0, [])
for a in answer:
    print(*a)