import queue
import random


class QueenBoard:
    def __init__(self, n, state=None):
        self.n = n
        if state is None:
            self.state = [random.randint(0, n - 1) for _ in range(n)]
        else:
            self.state = state

    def heuristic_cost(self):
        cost = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.state[i] == self.state[j]:
                    cost += 1
                elif abs(self.state[i] - self.state[j]) == j - i:
                    cost += 1
        return cost

    def is_valid(self):
        return self.heuristic_cost() == 0

    def get_successors(self):
        successors = []
        for col in range(self.n):
            for row in range(self.n):
                if self.state[col] != row:
                    successor_state = list(self.state)
                    successor_state[col] = row
                    successors.append(QueenBoard(self.n, successor_state))
        return successors

    def __lt__(self, other):
        return self.heuristic_cost() < other.heuristic_cost()


def solve_n_queens(n):
    start_state = QueenBoard(n)
    Q_priority_queue = queue.PriorityQueue()
    Q_priority_queue.put(start_state)

    while not Q_priority_queue.empty():
        current_board = Q_priority_queue.get()
        if current_board.is_valid():
            return current_board.state
        for successor in current_board.get_successors():
            Q_priority_queue.put(successor)

    return None


if __name__ == '__main__':
    solution = solve_n_queens(8)
    if solution is not None:
        print(solution)
    else:
        print("No solution found")
