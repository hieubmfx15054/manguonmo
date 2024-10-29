import numpy as np
import tkinter as tk
from tkinter import messagebox

# Initialize the Tkinter window
root = tk.Tk()
root.title("Giải hệ phương trình tuyến tính")
root.geometry("500x500")

# Function to solve the system of equations
def solve_equations():
    try:
        n = int(entry_n.get())  # Get the size of the system
        coefficients = []
        results = []

        # Get matrix coefficients
        for i in range(n):
            row = []
            for j in range(n):
                value = float(entries_matrix[i][j].get())
                row.append(value)
            coefficients.append(row)

        # Get result vector
        for i in range(n):
            result_value = float(entries_result[i].get())
            results.append(result_value)

        # Convert to NumPy arrays
        A = np.array(coefficients)
        B = np.array(results)

        # Solve the system of equations
        solution = np.linalg.solve(A, B)

        # Display the solution
        result_str = "\n".join([f"x{i+1} = {sol:.2f}" for i, sol in enumerate(solution)])
        messagebox.showinfo("Kết quả", result_str)
    except np.linalg.LinAlgError:
        messagebox.showerror("Lỗi", "Hệ phương trình không có nghiệm hoặc vô số nghiệm.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã có lỗi xảy ra: {str(e)}")

# Function to generate the input fields for matrix and results
def generate_fields():
    global entries_matrix, entries_result
    try:
        n = int(entry_n.get())  # Get the size of the system

        # Clear previous entries if any
        for widget in matrix_frame.winfo_children():
            widget.destroy()

        entries_matrix = []
        entries_result = []

        # Create matrix entry fields
        for i in range(n):
            row_entries = []
            for j in range(n):
                entry = tk.Entry(matrix_frame, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            entries_matrix.append(row_entries)

        # Create result vector entry fields
        for i in range(n):
            entry = tk.Entry(matrix_frame, width=5)
            entry.grid(row=i, column=n+1, padx=5, pady=5)
            entries_result.append(entry)

    except ValueError:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập một số nguyên hợp lệ cho n.")

# UI components
label_n = tk.Label(root, text="Nhập số phương trình (n):")
label_n.pack(pady=10)

entry_n = tk.Entry(root)
entry_n.pack(pady=10)

generate_button = tk.Button(root, text="Tạo ma trận", command=generate_fields)
generate_button.pack(pady=10)

matrix_frame = tk.Frame(root)
matrix_frame.pack(pady=10)

solve_button = tk.Button(root, text="Giải hệ phương trình", command=solve_equations)
solve_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
