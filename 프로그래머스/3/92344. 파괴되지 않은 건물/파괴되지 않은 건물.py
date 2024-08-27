def solution(board, skills):
    answer = 0

    n, m = len(board), len(board[0])

    tmp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for skill_type, r1, c1, r2, c2, degree in skills:
        real_degree = degree if skill_type == 2 else -degree
        tmp[r1][c1] += real_degree
        tmp[r1][c2 + 1] -= real_degree
        tmp[r2 + 1][c1] -= real_degree
        tmp[r2 + 1][c2 + 1] += real_degree

    for x in range(n + 1):
        for y in range(1, m + 1):
            tmp[x][y] += tmp[x][y - 1]

    for y in range(m + 1):
        for x in range(1, n + 1):
            tmp[x][y] += tmp[x - 1][y]

    for x in range(n):
        for y in range(m):
            if board[x][y] + tmp[x][y] >= 1:
                answer += 1

    return answer


if __name__ == '__main__':
    print(solution(board=[[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
             skills=[[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
