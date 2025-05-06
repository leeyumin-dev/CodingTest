'''
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 인데, 순열이 오름차순이여야됨
15649 처럼 길이를 정해놓고 그 안에 숫자를 채우면 오름차순 조건 만족시킬 수 없음
1부터 N까지의 순서로 탐색하면 오름차순 순열이 자연스럽게 만들어짐
-> 첫째자리에 nums[i]넣거나 안넣거나 이진 트리로 생각하고 M개의 길이만큼 숫자를 추가하면 오른차순 순열 만들어짐짐
==> 1부터 N까지의 수 중에서 M개의 수를 고르는 조합
'''
def dfs(n, nums): # 현재 추가할 숫자, 순열열
    if n > N:
        if len(nums) == M:
            answer.append(nums)
        return
    
    dfs(n+1, nums + [n])
    dfs(n+1, nums)

N, M = map(int, input().split())
answer = []
dfs(1, [])
for a in answer:
    print(*a)