from collections import deque

R, C, K = map(int, input().split())

golem = [list(map(int, input().split())) for _ in range(K)]
exit_ = set()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

forest = [[1]+[0]*C+[1] for _ in range(R+3)]+[[1]*(C+2)]

def BFS(si, sj):
    queue = deque([(si, sj)])
    visited = [[0]*(C+2) for _ in range(R+4)]
    
    mx_i = 0   

    while queue:
        now = queue.popleft()
        visited[now[0]][now[1]] = 1

        mx_i = max(mx_i, now[0])

        for i in range(4):
            ni,nj = now[0] + dy[i], now[1] + dx[i]
            if visited[ni][nj] == 0 and (forest[now[0]][now[1]] == forest[ni][nj] or ((now[0], now[1]) in exit_ and forest[ni][nj] > 1)):
                queue.append((ni,nj))

    return mx_i - 2


ans = 0
num = 2
for cj, dr in golem:
    ci = 1

    while True:
        # 아래로 내려갈 수 있다면 아래로 한 칸 내려가기
        if forest[ci+1][cj-1]+forest[ci+2][cj]+forest[ci+1][cj+1] == 0:
            ci += 1

        # 왼쪽 회전 + 아래로 한 칸
        elif (forest[ci-1][cj-1]+forest[ci][cj-2]+forest[ci+1][cj-1]+forest[ci+1][cj-2]+forest[ci+2][cj-1]) == 0:
            ci += 1
            cj -=1
            dr = (dr-1) % 4
        
        # 오른쪽 회전 + 아래로 한 칸
        elif (forest[ci-1][cj+1]+forest[ci][cj+2]+forest[ci+1][cj+1]+forest[ci+1][cj+2]+forest[ci+2][cj+1]) == 0:
            ci += 1
            cj += 1
            dr = (dr+1) % 4
        
        # 이동 불가하면 종료
        else: 
            break
    
    # 범위 밖이면 새로 시작
    if ci < 4:
        forest = [[1]+[0]*C+[1] for _ in range(R+3)]+[[1]*(C+2)]
        num = 2
        exit_ = set()
    
    # 골렘 표시
    else:
        forest[ci+1][cj], forest[ci-1][cj] = num, num
        forest[ci][cj-1:cj+2] = num, num, num
        num += 1

        exit_.add((ci+dx[dr], cj+dy[dr]))
        ans += BFS(ci, cj)

print(ans)