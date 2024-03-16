from typing import List

def TreeOfLife(H: int, W: int, N: int, tree: List[str]) -> List[str]:

    year = 0
    tree_zero = []
    for i in range(H):
        tree_w = []
        for j in range(W):
            if tree[i][j] == '.':
                tree_w.append(0)
            if tree[i][j] == '+':
                tree_w.append(1)
        tree_zero.append(tree_w)

    while year < N: 
        tree_zero = aging(H, W, tree_zero)
        year += 1
        if year % 2 == 0:
            tree_zero = destruction(H, W, tree_zero)
        
    old_tree = []
    for i in range(H):
        tree_w = ''
        for j in range(W):
            if tree_zero[i][j] == 0:
                tree_w += '.'
            if tree_zero[i][j] > 0:
                tree_w += '+'
        old_tree.append(tree_w)

    return old_tree

def aging(H: int, W: int, tree_zero: List[str]) -> List[str]:

    for i in range(H):
        for j in range(W):
            tree_zero[i][j] += 1

    return tree_zero

def destruction(H: int, W: int, tree_zero: List[str]) -> List[str]:

    for i in range(H):
        for j in range(W):
            if tree_zero[i][j] >= 3:
                if j > 0 and tree_zero[i][j - 1] < 3:
                    tree_zero[i][j - 1] = 0
                if j + 1 < W and tree_zero[i][j + 1] < 3:
                    tree_zero[i][j + 1] = 0
                if i > 0 and tree_zero[i - 1][j] < 3:
                    tree_zero[i - 1][j] = 0
                if i + 1 < H and tree_zero[i + 1][j] < 3:
                    tree_zero[i + 1][j] = 0

                if j > 0 and tree_zero[i][j - 1] >= 3:
                    tree_zero[i][j - 1] = -1
                if j + 1 < W and tree_zero[i][j + 1] >= 3:
                    tree_zero[i][j + 1] = -1
                if i > 0 and tree_zero[i - 1][j] >= 3:
                    tree_zero[i - 1][j] = -1
                if i + 1 < H and tree_zero[i + 1][j] >= 3:
                    tree_zero[i + 1][j] = -1
                tree_zero[i][j] = 0

            if tree_zero[i][j] < 0:
                if j > 0 and tree_zero[i][j - 1] < 3 and tree_zero[i][j - 1] > 0:
                    tree_zero[i][j - 1] = 0
                if j + 1 < W and tree_zero[i][j + 1] < 3 and tree_zero[i][j + 1] > 0:
                    tree_zero[i][j + 1] = 0
                if i > 0 and tree_zero[i - 1][j] < 3 and tree_zero[i - 1][j] > 0:
                    tree_zero[i - 1][j] = 0
                if i + 1 < H and tree_zero[i + 1][j] < 3 and tree_zero[i + 1][j] > 0:
                    tree_zero[i + 1][j] = 0

                if j > 0 and tree_zero[i][j - 1] >= 3:
                    tree_zero[i][j - 1] = -1
                if j + 1 < W and tree_zero[i][j + 1] >= 3:
                    tree_zero[i][j + 1] = -1
                if i > 0 and tree_zero[i - 1][j] >= 3:
                    tree_zero[i - 1][j] = -1
                if i + 1 < H and tree_zero[i + 1][j] >= 3:
                    tree_zero[i + 1][j] = -1
                tree_zero[i][j] = 0

    for i in range(H):
        for j in range(W):
            if tree_zero[i][j] == -1:
                tree_zero[i][j] = 0

    return tree_zero