'''
순서대로 K번째 사람을 제거, 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속 반복
원을 따라 반복한다? 앞에서 빼고 뒤로 넣고를 생각하면서 K번까지 앞에 있는 값을 뒤로 넣어줌 K번째가 되면 삭제
1, 2, 3, 4, 5, 6, 7 이고 K=3 일 때 예시
3 제거 후 큐 = 4, 5, 6, 7, 1, 2
6 제거 후 큐 = 7, 1, 2, 4, 5
2 제거 후 큐 = 4, 5, 7, 1
7 제거 후 큐 =  1, 4, 5
5 제거 후 큐 = 1, 4
큐가 빌떄까지 반복
'''
from collections import deque

N, K = map(int, input().split())

queue = deque(list(map(str, range(1, N+1))))

result = []
while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    # k 번째 값 삭제
    result.append(queue.popleft())

if queue:
    result += queue
print(f"<{', '.join(result)}>")