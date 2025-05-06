'''
행에 있는지 체크, 열에 있는지 체크, 오른대각선에 있는지 체크, 왼대각선에 있는지 체크
visited 3개 사용, 행 기준으로 움직일거니까 열 방문, 대각선2방문 체크에 사용
모든 방문 배열이 f면 놓고 아니면 백트래킹
'''            
def dfs(row):
    global answer
    if row == n:
        answer += 1
        return

    for i in range(n):
        if not visited1[i] and not visited2[row+i] and not visited3[row-i]:
            visited1[i] = visited2[row+i] = visited3[row-i] = True
            dfs(row + 1)
            visited1[i] = visited2[row+i] = visited3[row-i] = False
        
n = int(input())
answer = 0
visited1 = [False] * n
visited2 = [False] * (2 * n)
visited3 = [False] * (2 * n)
dfs(0)
print(answer)
    