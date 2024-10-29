import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Initialize the Tkinter window
root = tk.Tk()
root.title("Phần mềm hỗ trợ học tập môn Hình học")
root.geometry("600x600")

# Create a Notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

### Tab for 2D Shapes ###
tab_2d = ttk.Frame(notebook)
notebook.add(tab_2d, text="Hình học 2D")

### Tab for 3D Shapes ###
tab_3d = ttk.Frame(notebook)
notebook.add(tab_3d, text="Hình học 3D")


### Functions for 2D Shapes ###

# Function to calculate area and perimeter of a rectangle
def calculate_rectangle():
  try:
    width = float(entry_width.get())
    height = float(entry_height.get())
    if width <= 0 or height <= 0:
      raise ValueError("Chiều rộng và chiều cao phải lớn hơn 0.")

    # Tính diện tích và chu vi
    area = width * height
    perimeter = 2 * (width + height)

    # Hiển thị kết quả
    result_label_2d.config(text=f"Diện tích: {area:.2f}\nChu vi: {perimeter:.2f}")

    # Vẽ hình chữ nhật
    rectangle = plt.Rectangle((0, 0), width, height, fill=None, edgecolor='r')
    plt.figure()
    plt.gca().add_patch(rectangle)
    plt.xlim(-1, width + 1)
    plt.ylim(-1, height + 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Hình chữ nhật: {width} x {height}")
    plt.show()

  except ValueError as e:
    messagebox.showerror("Lỗi", f"Vui lòng nhập giá trị hợp lệ: {str(e)}")


# Function to calculate area and perimeter of a circle
def calculate_circle():
  try:
    radius = float(entry_radius.get())
    if radius <= 0:
      raise ValueError("Bán kính phải lớn hơn 0.")

    # Tính diện tích và chu vi
    area = np.pi * radius ** 2
    perimeter = 2 * np.pi * radius

    # Hiển thị kết quả
    result_label_2d.config(text=f"Diện tích: {area:.2f}\nChu vi: {perimeter:.2f}")

    # Vẽ hình tròn
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    plt.figure()
    plt.plot(x, y)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Hình tròn với bán kính {radius}")
    plt.show()

  except ValueError as e:
    messagebox.showerror("Lỗi", f"Vui lòng nhập giá trị hợp lệ: {str(e)}")


### Functions for 3D Shapes ###

# Function to calculate volume and surface area of a cylinder
def calculate_cylinder():
  try:
    radius = float(entry_cylinder_radius.get())
    height = float(entry_cylinder_height.get())
    if radius <= 0 or height <= 0:
      raise ValueError("Bán kính và chiều cao phải lớn hơn 0.")

    # Tính thể tích và diện tích mặt trụ
    volume = np.pi * radius ** 2 * height
    surface_area = 2 * np.pi * radius * (radius + height)

    # Hiển thị kết quả
    result_label_3d.config(text=f"Thể tích: {volume:.2f}\nDiện tích mặt trụ: {surface_area:.2f}")

    # Vẽ hình trụ
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    z = np.linspace(0, height, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = radius * np.cos(theta_grid)
    y_grid = radius * np.sin(theta_grid)
    ax.plot_surface(x_grid, y_grid, z_grid, color='b', alpha=0.6)
    plt.title(f"Hình trụ: Bán kính {radius}, Cao {height}")
    plt.show()

  except ValueError as e:
    messagebox.showerror("Lỗi", f"Vui lòng nhập giá trị hợp lệ: {str(e)}")


# Function to calculate volume and surface area of a sphere
def calculate_sphere():
  try:
    radius = float(entry_sphere_radius.get())
    if radius <= 0:
      raise ValueError("Bán kính phải lớn hơn 0.")

    # Tính thể tích và diện tích mặt cầu
    volume = (4 / 3) * np.pi * radius ** 3
    surface_area = 4 * np.pi * radius ** 2

    # Hiển thị kết quả
    result_label_3d.config(text=f"Thể tích: {volume:.2f}\nDiện tích mặt cầu: {surface_area:.2f}")

    # Vẽ hình cầu
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    phi, theta = np.mgrid[0.0:np.pi:100j, 0.0:2.0 * np.pi:100j]
    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)
    ax.plot_surface(x, y, z, color='r', alpha=0.6)
    plt.title(f"Hình cầu: Bán kính {radius}")
    plt.show()

  except ValueError as e:
    messagebox.showerror("Lỗi", f"Vui lòng nhập giá trị hợp lệ: {str(e)}")


### UI for 2D Shapes ###
label_title_2d = tk.Label(tab_2d, text="Tính toán hình học 2D", font=("Helvetica", 16))
label_title_2d.pack(pady=10)

# UI for Rectangle calculations
rectangle_frame = tk.Frame(tab_2d)
rectangle_frame.pack(pady=10)

label_width = tk.Label(rectangle_frame, text="Chiều rộng hình chữ nhật:")
label_width.grid(row=0, column=0, padx=5, pady=5)
entry_width = tk.Entry(rectangle_frame)
entry_width.grid(row=0, column=1, padx=5, pady=5)

label_height = tk.Label(rectangle_frame, text="Chiều cao hình chữ nhật:")
label_height.grid(row=1, column=0, padx=5, pady=5)
entry_height = tk.Entry(rectangle_frame)
entry_height.grid(row=1, column=1, padx=5, pady=5)

rectangle_button = tk.Button(rectangle_frame, text="Tính hình chữ nhật", command=calculate_rectangle)
rectangle_button.grid(row=2, column=0, columnspan=2, pady=10)

# UI for Circle calculations
circle_frame = tk.Frame(tab_2d)
circle_frame.pack(pady=10)

label_radius = tk.Label(circle_frame, text="Bán kính hình tròn:")
label_radius.grid(row=0, column=0, padx=5, pady=5)
entry_radius = tk.Entry(circle_frame)
entry_radius.grid(row=0, column=1, padx=5, pady=5)

circle_button = tk.Button(circle_frame, text="Tính hình tròn", command=calculate_circle)
circle_button.grid(row=1, column=0, columnspan=2, pady=10)

# Result label for 2D Shapes
result_label_2d = tk.Label(tab_2d, text="", font=("Helvetica", 14))
result_label_2d.pack(pady=20)

### UI for 3D Shapes ###
label_title_3d = tk.Label(tab_3d, text="Tính toán hình học 3D", font=("Helvetica", 16))
label_title_3d.pack(pady=10)

# UI for Sphere calculations
sphere_frame = tk.Frame(tab_3d)
sphere_frame.pack(pady=10)

label_sphere_radius = tk.Label(sphere_frame, text="Bán kính hình cầu:")
label_sphere_radius.grid(row=0, column=0, padx=5, pady=5)
entry_sphere_radius = tk.Entry(sphere_frame)
entry_sphere_radius.grid(row=0, column=1, padx=5, pady=5)

sphere_button = tk.Button(sphere_frame, text="Tính hình cầu", command=calculate_sphere)
sphere_button.grid(row=1, column=0, columnspan=2, pady=10)

# UI for Cylinder calculations
cylinder_frame = tk.Frame(tab_3d)
cylinder_frame.pack(pady=10)

label_cylinder_radius = tk.Label(cylinder_frame, text="Bán kính đáy hình trụ:")
label_cylinder_radius.grid(row=0, column=0, padx=5, pady=5)
entry_cylinder_radius = tk.Entry(cylinder_frame)
entry_cylinder_radius.grid(row=0, column=1, padx=5, pady=5)

label_cylinder_height = tk.Label(cylinder_frame, text="Chiều cao hình trụ:")
label_cylinder_height.grid(row=1, column=0, padx=5, pady=5)
entry_cylinder_height = tk.Entry(cylinder_frame)
entry_cylinder_height.grid(row=1, column=1, padx=5, pady=5)

cylinder_button = tk.Button(cylinder_frame, text="Tính hình trụ", command=calculate_cylinder)
cylinder_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result label for 3D Shapes
result_label_3d = tk.Label(tab_3d, text="", font=("Helvetica", 14))
result_label_3d.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

