from collections import Counter


class Board:
    def __init__(self, rows):
        self.board_size = len(rows[0])
        vals = [val for row in rows for val in row]
        indices = [
            (row_idx, col_idx)
            for row_idx, row_val in enumerate(rows)
            for col_idx in range(len(row_val))
        ]
        self.val_to_indices = {val: index for val, index in zip(vals, indices)}
        self.marks = []

    def mark(self, value):
        if value in self.val_to_indices:
            # We have a mark!
            self.marks.append(self.val_to_indices[value])

    def has_won(self):
        # Check for all across:
        if not self.marks:
            return False
        rows, cols = zip(*self.marks)
        row_counts, col_counts = Counter(rows), Counter(cols)
        if any(v >= self.board_size for v in row_counts.values()) or any(
            v >= self.board_size for v in col_counts.values()
        ):
            return True
        else:
            return False

    def unmarked_sum(self):
        return sum(
            val for val, index in self.val_to_indices.items() if index not in self.marks
        )


def load_input(filename):
    with open(filename, "r") as f:
        draws = [int(x) for x in f.readline().rstrip("\n").split(",")]
        boards = []
        board = None
        for line in f.readlines():
            line = line.rstrip("\n")
            if not line:
                if board is not None:
                    # new board
                    boards.append(Board(board))
                board = []
            else:
                board.append([int(x) for x in line.split()])
        boards.append(Board(board))
    return draws, boards


draws, boards = load_input("input.txt")

winner = None
for draw in draws:
    for board in boards:
        board.mark(draw)
        if board.has_won():
            print("We have a winner!")
            winner = board
            break
    if winner is not None:
        break

if winner is None:
    raise RuntimeError("We never found a winner :(")

print("Part 1:")
print(f"Winning score = {winner.unmarked_sum() * draw}")


draws, boards = load_input("input.txt")

not_winners = set(range(len(boards)))
last_winner = None
for draw in draws:
    for idx in list(not_winners):
        board = boards[idx]
        board.mark(draw)
        if board.has_won():
            not_winners.discard(idx)
            if len(not_winners) == 0:
                # This was the last winner!
                print("We have a last winner!")
                last_winner = idx
                last_winner_score = boards[last_winner].unmarked_sum() * draw

if last_winner is None:
    raise RuntimeError("We never found a last winner :(")

print("Part 2:")
print(f"Last winner score = {last_winner_score}")
