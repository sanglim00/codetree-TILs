import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N)]
cnt = [1 for _ in range(N)]

dp_ = [0 for _ in range(N)]
cnt_ = [1 for _ in range(N)]

for i in range(N):
    dp[i], dp_[i] = lst[i], lst[i]
    if dp[i] < dp[i-1]+lst[i]:
        dp[i] = dp[i-1]+lst[i]
        cnt[i] = cnt[i-1]+1
    if dp_[i] > dp_[i-1]+lst[i]:
        dp_[i] = dp_[i-1]+lst[i]
        cnt_[i] = cnt_[i-1]+1


ans = 0
for i in range(N):
    if cnt[i] >= K:
        ans = max(ans, dp[i])

ans_ = float("INF")
for i in range(N):
    if cnt_[i] == K:
        ans_ = min(ans_, dp_[i])


if ans: print(ans)
else: print(ans_)