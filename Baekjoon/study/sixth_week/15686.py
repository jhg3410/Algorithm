from itertools import combinations

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]

chicken = []
home = []

for i in range(n):
    for j in range(n):
        if lst[i][j] == 2:
            chicken.append([i,j])
        elif lst[i][j] == 1:
            home.append([i,j])

city_dist = 10000000
for ch in combinations(chicken, m):
    dist = 0
    for j in home:
        home_x, home_y = j[0],j[1]
        # 치킨집과 집의 거리
        dist += min([abs(i[0] - home_x)+abs(i[1] - home_y) for i in ch])
        # tmp_lst = []
        # for i in ch:
        #     tmp_lst.append(abs(i[0] - home_x) + abs(i[1] - home_y))
        # dist += min(tmp_lst)
        if dist >= city_dist: break 
    if dist < city_dist : city_dist = dist


print(city_dist)