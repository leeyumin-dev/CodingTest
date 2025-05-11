dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cctv = [[], [1], [1, 3], [0, 1], [0, 1, 3], [0, 1, 2, 3]]

def cal(tlst):
    v = [[0] * (M + 2) for _ in range(N + 2)]

    # 모든 cctv 처리
    for i in range(cctv_cnt):
        si, sj = lst[i]
        rot = tlst[i]           # 0 ~ 3
        type = grid[si][sj]     # 1 ~ 5

        for dr in cctv[type]:
            dr = (dr + rot) % 4
            ci, cj = si, sj
            while True:
                ci, cj = ci + dx[dr], cj + dy[dr]
                if grid[ci][cj] == 6:
                    break
                v[ci][cj] = 1
    # 사각지대 개수 카운트
    cnt = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if grid[i][j] == 0 and v[i][j] == 0:
                cnt += 1

    return cnt

def dfs(n, tlst): # cctv index, 기본 회전 정보
    global ans
    if n == cctv_cnt: # 모든 방향 탐색 완료
        ans = min(ans, cal(tlst))
        return
    
    dfs(n+1, tlst + [0])
    dfs(n+1, tlst + [1])
    dfs(n+1, tlst + [2])
    dfs(n+1, tlst + [3])

N, M = map(int, input().split())
grid = [[6]* (M + 2)] + [[6] + list(map(int, input().split())) + [6] for _ in range(N)] + [[6]* (M + 2)] # 범위 밖 조건을 고려하지 않기 위해 주변을 벽으로 둘러쌓음

lst = []
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if 1 <= grid[i][j] < 6:
            lst.append((i, j))

cctv_cnt = len(lst)
ans = N * M # 최댓값으로 초기화
dfs(0, [])
print(ans)