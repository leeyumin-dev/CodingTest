N, S = map(int, input().split())
lst = list(map(int, input().split()))

def dfs(n, sm, cnt):
    global answer
    if n == N:
        if sm == S and cnt > 0: # 크기가 양수인 부분 수열을 원하니까 무조건 1개 이상 있어야됨
            answer += 1
        return
    
    dfs(n + 1, sm + lst[n], cnt + 1) # 숫자를 포함하는 dfs
    dfs(n + 1, sm, cnt) # 포함하지 않는 dfs

answer = 0           
dfs(0, 0, 0)
print(answer)