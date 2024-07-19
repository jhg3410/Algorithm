from dataclasses import dataclass


@dataclass
class Atom:
    def __init__(self, x, y, m, s, d):
        self.x = x
        self.y = y
        self.m = m
        self.s = s
        self.d = d


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
atoms = dict()
board = [[[] for _ in range(n)] for _ in range(n)]
# auto increase
atom_key = 1
for _ in range(m):
    _x, _y, _m, _s, _d = map(int, input().split())
    _atom = Atom(x=_x - 1, y=_y - 1, m=_m, s=_s, d=_d)
    atoms[atom_key] = _atom
    atom_key += 1


def print_info():
    for key, atom in atoms.items():
        print(f'{key}, {atom.__dict__}')
    for row in board:
        print(row)
    print("-------------------")


def experiment():
    move()
    fusion()


def move():
    for key, atom in atoms.items():
        nx = (atom.x + (dx[atom.d] * atom.s)) % n
        ny = (atom.y + (dy[atom.d] * atom.s)) % n

        new_atom = atom
        new_atom.x = nx
        new_atom.y = ny

        atoms[key] = new_atom
        board[nx][ny].append(key)


def fusion():
    global atom_key
    for x in range(n):
        for y in range(n):
            if len(board[x][y]) < 2:
                board[x][y].clear()
                continue
            atom_keys = board[x][y]
            local_atoms = list(map(lambda q: atoms[q], atom_keys))

            atoms_size = len(local_atoms)
            directions = list(map(lambda q: q.d, local_atoms))
            masses = sum(list(map(lambda q: q.m, local_atoms)))
            speeds = sum(list(map(lambda q: q.s, local_atoms)))
            per_mass = masses // 5
            per_speed = speeds // atoms_size

            for key in atom_keys:
                atoms.pop(key)
            board[x][y].clear()

            if per_mass == 0: continue
            # 상하좌우
            if len(list(filter(lambda z: z % 2 == 0, directions))) in (0, atoms_size):
                for i in range(0, 8, 2):
                    atoms[atom_key] = Atom(x=x, y=y, m=per_mass, s=per_speed, d=i)
                    atom_key += 1
            # 대각선
            else:
                for i in range(1, 8, 2):
                    atoms[atom_key] = Atom(x=x, y=y, m=per_mass, s=per_speed, d=i)
                    atom_key += 1


if __name__ == '__main__':
    # print_info()
    for _ in range(k):
        experiment()
    # print_info()
    print(sum(map(lambda x: x.m, atoms.values())))
