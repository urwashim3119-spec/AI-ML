import tkinter as tk
from tkinter import messagebox
from collections import deque


# ---------------------------------------------------------
# BFS Algorithm for Water Jug Problem
# ---------------------------------------------------------
def water_jug_bfs(capacity_a, capacity_b, target):
    # Initial state: both jugs are empty
    start = (0, 0)

    # Queue for BFS
    queue = deque([start])

    # To remember visited states
    visited = {start}

    # To store parent state and action
    parent = {start: None}
    action = {start: "Start"}

    while queue:
        current = queue.popleft()
        a, b = current

        # Check goal condition
        if a == target or b == target:
            path = []

            while current is not None:
                path.append((current, action[current]))
                current = parent[current]

            path.reverse()
            return path

        # -------------------------------------------------
        # Generate all possible next states
        # -------------------------------------------------

        next_states = []

        # 1. Fill Jug A
        next_states.append(((capacity_a, b), "Fill Jug A"))

        # 2. Fill Jug B
        next_states.append(((a, capacity_b), "Fill Jug B"))

        # 3. Empty Jug A
        next_states.append(((0, b), "Empty Jug A"))

        # 4. Empty Jug B
        next_states.append(((a, 0), "Empty Jug B"))

        # 5. Pour Jug A into Jug B
        amount = min(a, capacity_b - b)
        next_states.append(
            ((a - amount, b + amount), "Pour Jug A → Jug B")
        )

        # 6. Pour Jug B into Jug A
        amount = min(b, capacity_a - a)
        next_states.append(
            ((a + amount, b - amount), "Pour Jug B → Jug A")
        )

        # Add new states to queue
        for new_state, act in next_states:

            if new_state not in visited:
                visited.add(new_state)
                parent[new_state] = current
                action[new_state] = act
                queue.append(new_state)

    return None


# ---------------------------------------------------------
# GUI Function
# ---------------------------------------------------------
def solve_problem():

    try:
        capacity_a = int(jug_a_entry.get())
        capacity_b = int(jug_b_entry.get())
        target = int(target_entry.get())

        if capacity_a <= 0 or capacity_b <= 0:
            messagebox.showerror(
                "Error",
                "Jug capacities must be greater than 0."
            )
            return

        if target <= 0:
            messagebox.showerror(
                "Error",
                "Target must be greater than 0."
            )
            return

        if target > max(capacity_a, capacity_b):
            messagebox.showerror(
                "Error",
                "Target cannot be greater than the largest jug."
            )
            return

        # Clear previous output
        result_text.delete("1.0", tk.END)

        # Run BFS
        solution = water_jug_bfs(
            capacity_a,
            capacity_b,
            target
        )

        if solution is None:
            result_text.insert(
                tk.END,
                "No solution exists for the given problem."
            )
            return

        # Display solution
        result_text.insert(
            tk.END,
            "WATER JUG PROBLEM SOLUTION\n"
        )

        result_text.insert(
            tk.END,
            "====================================\n\n"
        )

        result_text.insert(
            tk.END,
            f"Jug A Capacity : {capacity_a} litres\n"
        )

        result_text.insert(
            tk.END,
            f"Jug B Capacity : {capacity_b} litres\n"
        )

        result_text.insert(
            tk.END,
            f"Target         : {target} litres\n\n"
        )

        result_text.insert(
            tk.END,
            "Steps:\n"
        )

        result_text.insert(
            tk.END,
            "------------------------------------\n"
        )

        for i, (state, act) in enumerate(solution):
            a, b = state

            result_text.insert(
                tk.END,
                f"Step {i}: {act}\n"
            )

            result_text.insert(
                tk.END,
                f"        Jug A = {a} L, "
                f"Jug B = {b} L\n\n"
            )

        result_text.insert(
            tk.END,
            "Goal Reached Successfully!\n"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid integer values."
        )


# ---------------------------------------------------------
# Clear Function
# ---------------------------------------------------------
def clear_fields():
    jug_a_entry.delete(0, tk.END)
    jug_b_entry.delete(0, tk.END)
    target_entry.delete(0, tk.END)
    result_text.delete("1.0", tk.END)

    jug_a_entry.insert(0, "4")
    jug_b_entry.insert(0, "3")
    target_entry.insert(0, "2")


# ---------------------------------------------------------
# Create Main Window
# ---------------------------------------------------------
root = tk.Tk()

root.title("Water Jug Problem - BFS")
root.geometry("700x650")

# ---------------------------------------------------------
# Heading
# ---------------------------------------------------------
title_label = tk.Label(
    root,
    text="WATER JUG PROBLEM",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=15)


subtitle_label = tk.Label(
    root,
    text="State Space Search using Breadth First Search (BFS)",
    font=("Arial", 12)
)

subtitle_label.pack(pady=5)


# ---------------------------------------------------------
# Input Frame
# ---------------------------------------------------------
input_frame = tk.Frame(root)

input_frame.pack(pady=20)


# Jug A
tk.Label(
    input_frame,
    text="Jug A Capacity:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10, pady=10)

jug_a_entry = tk.Entry(
    input_frame,
    width=15,
    font=("Arial", 12)
)

jug_a_entry.grid(row=0, column=1, padx=10, pady=10)

jug_a_entry.insert(0, "4")


# Jug B
tk.Label(
    input_frame,
    text="Jug B Capacity:",
    font=("Arial", 12)
).grid(row=1, column=0, padx=10, pady=10)

jug_b_entry = tk.Entry(
    input_frame,
    width=15,
    font=("Arial", 12)
)

jug_b_entry.grid(row=1, column=1, padx=10, pady=10)

jug_b_entry.insert(0, "3")


# Target
tk.Label(
    input_frame,
    text="Target Amount:",
    font=("Arial", 12)
).grid(row=2, column=0, padx=10, pady=10)

target_entry = tk.Entry(
    input_frame,
    width=15,
    font=("Arial", 12)
)

target_entry.grid(row=2, column=1, padx=10, pady=10)

target_entry.insert(0, "2")


# ---------------------------------------------------------
# Buttons
# ---------------------------------------------------------
button_frame = tk.Frame(root)

button_frame.pack(pady=10)


solve_button = tk.Button(
    button_frame,
    text="SOLVE USING BFS",
    font=("Arial", 12, "bold"),
    command=solve_problem
)

solve_button.grid(
    row=0,
    column=0,
    padx=10
)


clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 12, "bold"),
    command=clear_fields
)

clear_button.grid(
    row=0,
    column=1,
    padx=10
)


# ---------------------------------------------------------
# Result Area
# ---------------------------------------------------------
result_text = tk.Text(
    root,
    width=70,
    height=22,
    font=("Courier New", 11)
)

result_text.pack(
    padx=20,
    pady=15
)


# ---------------------------------------------------------
# Start GUI
# ---------------------------------------------------------
root.mainloop()