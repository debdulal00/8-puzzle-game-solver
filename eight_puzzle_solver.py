#!/usr/bin/env python3
"""
Optimized 8 Puzzle Game Solver
------------------------------------
- A* Search (Manhattan distance)
- BFS option
- Clean structure, fast, readable
- Tracks directions (UP/DOWN/LEFT/RIGHT)
"""

from collections import deque
import heapq


GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)


NEIGHBORS = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7],
}


def direction(from_idx, to_idx):
    """Return swipe direction for visualization."""
    fx, fy = divmod(from_idx, 3)
    tx, ty = divmod(to_idx, 3)

    if fx == tx and fy + 1 == ty:
        return "RIGHT"
    if fx == tx and fy - 1 == ty:
        return "LEFT"
    if fy == ty and fx + 1 == tx:
        return "DOWN"
    if fy == ty and fx - 1 == tx:
        return "UP"
    return "MOVE"


# ---------- Utility Functions ----------

def is_solvable(state):
    arr = [x for x in state if x != 0]
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions % 2 == 0


def print_state(state):
    """Display the board."""
    for i in range(0, 9, 3):
        row = state[i:i+3]
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()


def reconstruct_path(parent, start, goal):
    moves = []
    state = goal

    while state != start:
        prev_state, tile, move_dir = parent[state]
        moves.append((tile, move_dir))
        state = prev_state

    moves.reverse()
    return moves


# ---------- Manhattan Distance ----------

def manhattan(state):
    dist = 0
    for idx, val in enumerate(state):
        if val == 0:
            continue
        goal_idx = GOAL_STATE.index(val)
        x1, y1 = divmod(idx, 3)
        x2, y2 = divmod(goal_idx, 3)
        dist += abs(x1 - x2) + abs(y1 - y2)
    return dist


# ---------- BFS Solver ----------

def bfs(start):
    if start == GOAL_STATE:
        return []

    if not is_solvable(start):
        return None

    queue = deque([start])
    parent = {start: (None, None, None)}

    while queue:
        state = queue.popleft()

        if state == GOAL_STATE:
            return reconstruct_path(parent, start, GOAL_STATE)

        zero_idx = state.index(0)
        for nb in NEIGHBORS[zero_idx]:
            new_state = list(state)
            new_state[zero_idx], new_state[nb] = new_state[nb], new_state[zero_idx]
            new_state = tuple(new_state)
            tile = state[nb]
            move_dir = direction(nb, zero_idx)

            if new_state not in parent:
                parent[new_state] = (state, tile, move_dir)
                queue.append(new_state)

    return None


# ---------- A* Solver ----------

def astar(start):
    if start == GOAL_STATE:
        return []

    if not is_solvable(start):
        return None

    heap = []
    g_cost = {start: 0}
    parent = {start: (None, None, None)}

    heapq.heappush(heap, (manhattan(start), start))
    closed = set()

    while heap:
        _f, state = heapq.heappop(heap)

        if state in closed:
            continue

        if state == GOAL_STATE:
            return reconstruct_path(parent, start, GOAL_STATE)

        closed.add(state)
        zero_idx = state.index(0)

        for nb in NEIGHBORS[zero_idx]:
            new_state = list(state)
            new_state[zero_idx], new_state[nb] = new_state[nb], new_state[zero_idx]
            new_state = tuple(new_state)

            tile = state[nb]
            move_dir = direction(nb, zero_idx)

            new_g = g_cost[state] + 1

            if new_state not in g_cost or new_g < g_cost[new_state]:
                g_cost[new_state] = new_g
                f = new_g + manhattan(new_state)
                parent[new_state] = (state, tile, move_dir)
                heapq.heappush(heap, (f, new_state))

    return None


# ---------- Main CLI ----------

def parse_state(s):
    nums = list(map(int, s.split()))
    if len(nums) != 9 or sorted(nums) != list(range(9)):
        raise ValueError("Enter exactly 9 numbers from 0-8 once.")
    return tuple(nums)


def main():
    print("=== 8 Puzzle Game Solver (Optimized) ===")
    print("Goal state:")
    print_state(GOAL_STATE)

    inp = input("Enter 9 numbers (0=blank): ").strip()
    try:
        start = parse_state(inp)
    except ValueError as e:
        print(e)
        return

    print("\nChoose Algorithm:\n1. BFS\n2. A* (Recommended)")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        solution = bfs(start)
    else:
        solution = astar(start)

    if solution is None:
        print("UNSOLVABLE configuration.")
        return

    if not solution:
        print("Already solved!")
        return

    print(f"\nSolved in {len(solution)} moves.")
    print("\nMoves:")
    for i, (tile, move_dir) in enumerate(solution, 1):
        print(f"{i}. Move tile {tile} ({move_dir})")

    show = input("\nShow all board states? (y/n): ").strip().lower()
    if show == "y":
        state = start
        print("\nStep 0:")
        print_state(state)

        for step, (tile, move_dir) in enumerate(solution, 1):
            zero_idx = state.index(0)

            # find matching state
            for nb in NEIGHBORS[zero_idx]:
                new_state = list(state)
                new_state[zero_idx], new_state[nb] = new_state[nb], new_state[zero_idx]
                new_state = tuple(new_state)
                if state[nb] == tile:
                    state = new_state
                    break

            print(f"Step {step}: move {tile} ({move_dir})")
            print_state(state)


if __name__ == "__main__":
    main()
