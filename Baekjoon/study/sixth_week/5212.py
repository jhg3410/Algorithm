R, C = map(int,input().split())

lst = [list(input()) for _ in range(R)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

coord_lst = []

for i in range(R):
    for j in range(C):
        if lst[i][j] == 'X':
            cnt = 0
            for k in range(4):
                x = i+dx[k]
                y = j+dy[k]
                if 0 <= x < R  and 0 <= y < C:
                    if lst[x][y] == '.':
                        cnt += 1
                else:
                    cnt += 1
            if cnt >=3:
                coord_lst.append([i,j])

for coord in coord_lst:
    x, y = coord[0], coord[1]
    lst[x][y] = '.'


start_row = 0
end_row = 0
for i in range(R):
    if 'X' in lst[i]:
        start_row = i
        break

for i in range(R-1,-1,-1):
    if 'X' in lst[i]:
        end_row = i
        break

start_col = C-1
end_col = 0

for i in range(start_row,end_row+1):
    index_lst = [index for index, value in enumerate(lst[i]) if value == 'X']
    # index_lst = []
    # for index, value in enumerate(lst[i]):
    #     if value == 'X':
    #         index_lst.append(index)
    if not index_lst:
        continue
    min_index = index_lst[0]
    max_index = index_lst[-1]
    start_col = min(min_index,start_col)
    end_col = max(max_index,end_col)

for i in range(start_row,end_row+1):
    for j in range(start_col,end_col+1):
        print(lst[i][j], end= '')
    print()