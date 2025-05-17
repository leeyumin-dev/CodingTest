'''
6단계 이내에서 서로 아는 사람으로 연결될 수 있다.
케빈 베이컨 게임은 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산하는 게임
케빈 베이컨은 미국 헐리우드 영화배우들 끼리 케빈 베이컨 게임을 했을때 나오는 단계의 총 합이 가장 "적은" 사람이라고 한다.
케빈 베이컨의 수가 가장 작은 사람을 찾으려고 한다. 케빈 베이컨 수는 모든 사람과 케빈 베이컨 게임을 했을 때, 나오는 단계의 합이다.

친구 관계를 양방향 그래프로 표현
a -> b로 가는 경로가 여러개여도 그 중 최소 경로를 골라야되니까 bfs
1과 3, 1과 4, 2와 3, 3과 4, 4와 5가 친구인 경우에
bfs를 쓰면 
    1 -> 5에서 1 -> 3 -> 4 -> 5, 1 -> 4 -> 5 2개의 경로가 있는데 bfs 쓰면 1 -> 4 -> 5 경로로 감감

목적: 케빈 베이컨의 수가 가장 작은 사람
    케빈 베이컨의 수 = 케빈 베이컨 수는 모든 사람과 케빈 베이컨 게임을 했을 때, 나오는 단계의 합
'''

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

step = 1000000000000 # 대충 큰 숫자 ㅋㅋ
result = N
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    queue = deque([(i, 0)])
    visited[i] = True
    sum_step = 0
    while queue:
        node, idx = queue.popleft()
        sum_step += idx
        for next_node in graph[node]:
            if not visited[next_node]:
                queue.append((next_node, idx + 1))
                visited[next_node] = True

    if step > sum_step:
        step = sum_step
        result = i
    elif step == sum_step:
        result = min(result, i) # 번호가 가장 작은 사람을 출력을 위함

print(result)
