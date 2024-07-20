# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# n, m, k = map(int, input().split())
# directions = dict()
# priorities = dict()
# # 플레이어의 위치
# position_board = []
# # 계약자의 정보
# contract_board = []
# # 계약 기간의 정보
# contract_count_board = []
# turn = 0
#
#
# def start_game():
#     global turn
#
#     while not is_end():
#         turn += 1
#         run_turn()
#
#     print(turn if turn < 1000 else -1)
#
#
# def is_in(x: int, y: int):
#     return x in range(n) and y in range(n)
#
#
# def is_end():
#     if turn >= 1000:
#         return True
#
#     for x in range(n):
#         for y in range(n):
#             if position_board[x][y] > 1:
#                 return False
#
#     return True
#
#
# def run_turn():
#     move()
#     decrease_contract()
#     apply_contract()
#
#
# def move():
#     new_positions = dict()
#     for x in range(n):
#         for y in range(n):
#             # 플레이어 있는 곳만
#             if position_board[x][y] == 0: continue
#             number = position_board[x][y]
#             c_dir = directions[number]
#             p_dir = priorities[number][c_dir]
#             # 계약이 없는 칸에 먼저
#             for i in range(4):
#                 nx = x + dx[p_dir[i]]
#                 ny = y + dy[p_dir[i]]
#                 if not is_in(nx, ny): continue
#                 if contract_board[nx][ny] == 0:
#                     new_positions[number] = [nx, ny]
#                     directions[number] = p_dir[i]
#                     break
#             # 계약이 가능한 칸이 없다면 본인이 계약한 땅에
#             if number not in new_positions:
#                 for i in range(4):
#                     nx = x + dx[p_dir[i]]
#                     ny = y + dy[p_dir[i]]
#                     if not is_in(nx, ny): continue
#                     if contract_board[nx][ny] == number:
#                         new_positions[number] = [nx, ny]
#                         directions[number] = p_dir[i]
#                         break
#             position_board[x][y] = 0
#     for key, value in new_positions.items():
#         x = value[0]
#         y = value[1]
#         if position_board[x][y] == 0:
#             position_board[x][y] = key
#         else:
#             if key < position_board[x][y]:
#                 position_board[x][y] = key
#
#
# def apply_contract():
#     for x in range(n):
#         for y in range(n):
#             # 플레이어가 있는 곳은 계약 또는 재계약
#             if position_board[x][y] != 0:
#                 contract_board[x][y] = position_board[x][y]
#                 contract_count_board[x][y] = k
#
#
# def decrease_contract():
#     for x in range(n):
#         for y in range(n):
#             # 계약 기간이 1 남았다면
#             if contract_count_board[x][y] == 1:
#                 contract_board[x][y] = 0
#             # 모두 하나씩 줄인다.
#             contract_count_board[x][y] = max(contract_count_board[x][y] - 1, 0)
#
#
# if __name__ == '__main__':
#     for _ in range(n):
#         row = list(map(int, input().split()))
#         position_board.append(row)
#         contract_board.append(row.copy())
#         contract_count_board.append(list(map(lambda x: k if x > 0 else 0, row)))
#
#     _dir = list(map(int, input().split()))
#     for idx, d in enumerate(_dir, start=1):
#         directions[idx] = d - 1
#
#     for z in range(m):
#         up = list(map(lambda x: int(x) - 1, input().split()))
#         down = list(map(lambda x: int(x) - 1, input().split()))
#         left = list(map(lambda x: int(x) - 1, input().split()))
#         right = list(map(lambda x: int(x) - 1, input().split()))
#         priorities[z + 1] = [up, down, left, right]
#
#     start_game()


a = [[1,2,3], [4,4,5]]
b= a[0].copy()
a[0][0] = 1231
print(b)