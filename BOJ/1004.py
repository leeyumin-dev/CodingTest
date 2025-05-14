'''
행성계 간의 이동을 최대한 피해서 여행
빨간 실선은 어린 왕자가 출발점에서 도착점까지 도달하는데 있어서 필요한 행성계 진입/이탈 횟수를 최소화하는 경로
원은 행성계의 경계
목표: 최소의 행성계 진입/이탈 횟수

행성계에 진입/이탈을 하려면 현재 위치가 원의 내부에 있으면됨
출~도까지 중간에 있는 원은 우주선이 알아서 피해가니까 필수로 진입/이탈하는 경우는 출, 도착점만 계산
출발점과 도착점이 각 원의 내부에 있는지 체크
    출, 도착점과 원의 중심까지 거리가 반지름보다 작으면 내부에 있는 것임
    점과 점사이를 구하는 공식 이용 -> sqrt((x2 - x1)^2 + (y2 - y1)^2)
    만약 출, 도착점이 모두 하나의 원 내부에 있다면 진입/이탈은 없음 => 출발이나 도착 중 한 점만 원 안에 있을 경우 카운트
'''

import math

def check_inside(circles, sx, sy, ex, ey):
    count = 0
    for circle in circles:
        cx, cy, r = circle
        # 출~원 중심까지 거리 계산
        s_dist = math.sqrt((cx - sx)**2 + (cy - sy)**2)
        e_dist = math.sqrt((cx - ex)**2 + (cy - ey)**2)

        if s_dist <= r and e_dist > r:
            count += 1
        elif e_dist <= r and s_dist > r:
            count += 1
    return count

                          
T = int(input())
res = []
for t in range(T):
    sx, sy, ex, ey = map(int, input().split())
    circles = [list(map(int, input().split())) for _ in range(int(input()))]
    count = check_inside(circles, sx, sy, ex, ey)
    res.append(count)

for i in res:
    print(i)