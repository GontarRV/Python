from typing import List

def ConquestCampaign(N: int, M: int, L: int, battalion: List[int]):

    squares = []
    for i in range(N):
        row = []

        for j in range(M):
            row.append(0)

        squares.append(row)

    for i in range(L * 2):
        if i % 2 == 0:
            squares[battalion[i] - 1][battalion[i + 1] - 1] = 1

    day = 1

    for i in range(N):
        for j in range(M):
            while squares[i][j] == 0:
                day += 1

                for n in range(N):
                    for m in range(M):
                        if squares[n][m] == 1:
                            squares[n][m] = 2
                
                for n in range(N):
                    for m in range(M):
                        if squares[n][m] == 2:
                            if m > 0 and squares[n][m-1] == 0:
                                squares[n][m-1] = 1
                            if m + 1 < M and squares[n][m+1] == 0:
                                squares[n][m+1] = 1
                            if n > 0 and squares[n - 1][m] == 0:
                                squares[n - 1][m] = 1
                            if n + 1 < N and squares[n+1][m] == 0:
                                squares[n+1][m] = 1

    return day

