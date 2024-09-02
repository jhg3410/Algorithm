from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

node_info = []
answer = [[], []]


class Node:
    def __init__(self, number, left=None, right=None):
        self.number = number
        self.left = left
        self.right = right


def make_tree(nodes):
    if not nodes: return
    # 루트 찾기(y, idx, number)
    root = (-1, -1, -1)
    for idx, (x, y, number) in enumerate(nodes):
        if y > root[0]:
            root = (y, idx, number)
    root_idx = root[1]
    root_number = root[2]

    # 루트 왼쪽, 오른쪽 분리
    lefts, rights = nodes[:root_idx], nodes[root_idx + 1:]

    return Node(root_number, left=make_tree(lefts), right=make_tree(rights))


def preorder(root_node: Node):
    if root_node is None: return
    answer[0].append(root_node.number)
    preorder(root_node.left)
    preorder(root_node.right)


def postorder(root_node: Node):
    if root_node is None: return
    postorder(root_node.left)
    postorder(root_node.right)
    answer[1].append(root_node.number)


def solution(_nodeinfo):
    global node_info
    node_info = sorted([[x, y, number + 1] for number, (x, y) in enumerate(_nodeinfo)])
    root_node = make_tree(node_info)

    preorder(root_node=root_node)
    postorder(root_node=root_node)
    return answer


if __name__ == '__main__':
    print(solution(_nodeinfo=[[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
