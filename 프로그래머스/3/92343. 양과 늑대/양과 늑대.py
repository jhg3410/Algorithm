max_sheep = 0
infos = []
relations = []


def solution(info, edges):
    global infos, relations
    infos = info
    relations = [[] for _ in range(len(info))]
    for parent, child in edges:
        relations[parent].append(child)

    search(visited=[0], sheep_count=1, wolf_count=0)
    return max_sheep


def search(visited, sheep_count, wolf_count):
    global max_sheep
    max_sheep = max(max_sheep, sheep_count)
    if wolf_count >= sheep_count:
        return
    
    for node in visited:
        for child in relations[node]:
            if child in visited: continue
            visited.append(child)
            is_sheep = infos[child] == 0
            search(visited=visited, sheep_count=sheep_count + is_sheep, wolf_count=wolf_count + (not is_sheep))
            visited.pop()


if __name__ == '__main__':
    print(solution(info=[0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
                   edges=[[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
