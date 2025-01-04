m=[list(map(int,input().split())) for _ in range(9)]
r=[1]*9
c=r[:]
s=r[:]
for i in range(9):
    for j in range(9):
        r[i]|=(1<<m[i][j])
        c[j]|=(1<<m[i][j])
        s[(i//3)*3+j//3]|=(1<<m[i][j])

t=(1<<10)-1
f=1
for i in range(9):
    if r[i]!=t or c[i]!=t or s[i]!=t:
        print("INVALID")
        exit()
print("VALID")


class Slot:
    def __init__(self, r, c):
        self.r = r
        self.c = c

def get_free_slot(m):
    for i in range(9):
        for j in range(9):
            if m[i][j] == 0:
                return Slot(i, j)
    return None

def is_safe_row(m, s, d):
    for i in range(9):
        if m[s.r][i] == d:
            return False
    return True

def is_safe_col(m, s, d):
    for i in range(9):
        if m[i][s.c] == d:
            return False
    return True

def is_safe_box(m, s, d):
    sr, sc = (s.r // 3) * 3, (s.c // 3) * 3
    for i in range(sr, sr + 3):
        for j in range(sc, sc + 3):
            if m[i][j] == d:
                return False
    return True

def solve(m):
    s = get_free_slot(m)
    if s is None:
        return True  # Puzzle solved

    for i in range(1, 10):
        if (is_safe_row(m, s, i) and is_safe_col(m, s, i) and is_safe_box(m, s, i)):
            m[s.r][s.c] = i  # Place number

            if solve(m):  # Recursive call
                return True  # Solution found

            # Backtrack
            m[s.r][s.c] = 0

    return False  # Trigger backtracking if no solution

def print_board(m):
    for row in m:
        print(" ".join(str(num) for num in row))

def main():
    m = []
    print("Enter the Sudoku grid (use 0 for empty cells):")
    for _ in range(9):
        row = list(map(int, input().split()))
        m.append(row)

    if solve(m):
        print("Solved Sudoku:")
        print_board(m)
    else:
        print("Not Solved")

if __name__ == "__main__":
    main()
