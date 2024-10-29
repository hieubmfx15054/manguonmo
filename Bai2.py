import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, integrate, limit, solve, Eq, dsolve, Function
from tkinter import *
from tkinter import messagebox
import sympy as sp

# Initialize Tkinter window
root = Tk()
root.title("Phần mềm hỗ trợ học tập môn Giải tích")
root.geometry("600x600")

x = symbols('x')

# Function to calculate derivative
def calculate_derivative():
    try:
        function_str = entry_function.get()
        func = sp.sympify(function_str)
        derivative = diff(func, x)
        result_label.config(text=f"Đạo hàm: {sp.simplify(derivative)}")
    except Exception as e:
        messagebox.showerror("Lỗi", "Vui lòng nhập hàm hợp lệ.")

# Function to calculate integral
def calculate_integral():
    try:
        function_str = entry_function.get()
        func = sp.sympify(function_str)
        integral = integrate(func, x)
        result_label.config(text=f"Tích phân: {sp.simplify(integral)}")
    except Exception as e:
        messagebox.showerror("Lỗi", "Vui lòng nhập hàm hợp lệ.")

# Function to calculate limit
def calculate_limit():
    try:
        function_str = entry_function.get()
        point = float(entry_point.get())
        func = sp.sympify(function_str)
        lim = limit(func, x, point)
        result_label.config(text=f"Giới hạn: {lim}")
    except Exception as e:
        messagebox.showerror("Lỗi", "Vui lòng nhập hàm và điểm hợp lệ.")

# Function to plot function
def plot_function():
    try:
        function_str = entry_function.get()
        func = sp.lambdify(x, sp.sympify(function_str), "numpy")
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)

        plt.figure()
        plt.plot(x_vals, y_vals)
        plt.title(f"Đồ thị của hàm {function_str}")
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Lỗi", "Vui lòng nhập hàm hợp lệ.")

# Function to solve differential equations
def solve_differential():
    try:
        y = Function('y')
        deq_str = entry_function.get()
        deq = sp.sympify(deq_str)
        solution = dsolve(Eq(deq, 0), y(x))
        result_label.config(text=f"Nghiệm phương trình: {solution}")
    except Exception as e:
        messagebox.showerror("Lỗi", "Vui lòng nhập phương trình vi phân hợp lệ.")

# UI for entering function
label_function = Label(root, text="Nhập hàm số/phương trình vi phân:")
label_function.pack(pady=5)
entry_function = Entry(root, width=50)
entry_function.pack(pady=5)

# UI for entering limit point
label_point = Label(root, text="Nhập điểm để tính giới hạn (nếu cần):")
label_point.pack(pady=5)
entry_point = Entry(root, width=20)
entry_point.pack(pady=5)

# Buttons for various functions
derivative_button = Button(root, text="Tính đạo hàm", command=calculate_derivative)
derivative_button.pack(pady=5)

integral_button = Button(root, text="Tính tích phân", command=calculate_integral)
integral_button.pack(pady=5)

limit_button = Button(root, text="Tính giới hạn", command=calculate_limit)
limit_button.pack(pady=5)

plot_button = Button(root, text="Vẽ đồ thị", command=plot_function)
plot_button.pack(pady=5)

differential_button = Button(root, text="Giải phương trình vi phân", command=solve_differential)
differential_button.pack(pady=5)

# Result display
result_label = Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

# Du lieu test
# Ham test: x**3 + 2*x**2 - 5*x + 1
# Ham test vi phan: Derivative(y(x), x) + y(x) - x**2
#     kq: y(x)= Eq(y(x), C1*exp(-x)+ x**2 - 2*x + 2)
