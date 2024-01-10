import sys
from typing import List


class Ocean:
    state: List[List[int]]

    def __init__(self, init_state: List[List[int]]):
        self.state = init_state

    def __str__(self) -> str:
        return "\n".join([" ".join(str(el) for el in row) for row in self.state])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.state!r})"

    def gen_next_quantum(self) -> "Ocean":
        next_state = []
        fsh = 2
        shrmp = 3

        for i in range(len(self.state)):
            next_row = []
            for j in range(len(self.state[i])):
                if self.state[i][j] == 1:
                    next_row.append(1)
                else:
                    nf = 0
                    ns = 0
                    near = [
                        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                        (i, j - 1), (i, j + 1),
                        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1),
                    ]
                    for ni, nj in near:
                        if ni < 0 or nj < 0 or ni >= len(self.state) or nj >= len(self.state[i]): continue
                        if self.state[ni][nj] == fsh:
                            nf += 1
                        elif self.state[ni][nj] == shrmp:
                            ns += 1

                    if self.state[i][j] == fsh:
                        if nf < 2 or nf > 3:
                            next_row.append(0)
                        else:
                            next_row.append(2)

                    elif self.state[i][j] == shrmp:
                        if ns < 2 or ns > 3:
                            next_row.append(0)
                        else:
                            next_row.append(3)

                    elif nf == fsh and ns == shrmp:
                        next_row.append(2)
                    elif nf == 3:
                        next_row.append(2)
                    else:
                        next_row.append(0)
                        
            next_state.append(next_row)

        return Ocean(init_state=next_state)


if __name__ == "__main__":
    n_quantums = int(sys.stdin.readline())
    n_rows, n_clms = (int(i) for i in sys.stdin.readline().split())
    init_state = []
    for i in range(n_rows):
        line = [int(i) for i in sys.stdin.readline().split()]
        init_state.append(line)

    ocean = Ocean(init_state=init_state)
    for _ in range(n_quantums):
        ocean = ocean.gen_next_quantum()
    print(ocean) 

