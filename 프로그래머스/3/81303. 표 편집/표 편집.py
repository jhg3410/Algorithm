fronts = dict()
backs = dict()
# 본인의 앞 번호, 뒷 번호가 들어감
deleted = []
empty = 10 ** 10


def solution(n, k, cmd):
    for i in range(n):
        fronts[i] = i - 1
        backs[i] = i + 1

    fronts[0] = empty
    backs[n - 1] = empty

    select_number = k

    for commands in cmd:
        command = commands.split()
        # 삭제
        if command[0] == "C":
            front, back = fronts[select_number], backs[select_number]
            fronts[select_number] = empty
            backs[select_number] = empty
            deleted.append([select_number, front, back])

            if front != empty:
                backs[front] = back
            if back != empty:
                fronts[back] = front

            if back == empty:
                select_number = front
            else:
                select_number = back

        # 복구
        elif command[0] == "Z":
            number, front, back = deleted.pop()
            fronts[number] = front
            backs[number] = back

            backs[front] = number
            fronts[back] = number

        # 선택을 앞로
        elif command[0] == "U":
            offset = int(command[1])
            for _ in range(offset):
                select_number = fronts[select_number]

        # 선택을 뒤로
        else:
            offset = int(command[1])
            for _ in range(offset):
                select_number = backs[select_number]

    # print(select_number)
    # print(fronts)
    # print(backs)
    answer = ""
    for i in range(n):
        if fronts[i] == backs[i]:
            answer += "X"
        else:
            answer += "O"
    return answer


if __name__ == '__main__':
    print(solution(n=8, k=2, cmd=["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
