import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from functools import partial

# Define kernels
kernel_sharpen_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
kernel_sharpen_2 = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]])
kernel_sharpen_3 = np.array(
  [[-1, -1, -1, -1, -1], [-1, 2, 2, 2, -1], [-1, 2, 8, 2, -1], [-1, 2, 2, 2, -1], [-1, -1, -1, -1, -1]]) / 8.0


def open_image():
  global img
  global original_img
  file_path = filedialog.askopenfilename()

  try:
    # Sử dụng Pillow để mở ảnh
    pil_image = Image.open(file_path)
    pil_image = pil_image.resize((500, 500))  # Thay đổi kích thước thành 500x500

    # Chuyển đổi ảnh Pillow sang định dạng OpenCV
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    original_img = img.copy()  # Lưu ảnh gốc

    cv2.imshow('Original Image', original_img)  # Hiển thị ảnh gốc
  except Exception as e:
    print("Không thể mở tệp. Lỗi:", e)


def update_sharpness_and_brightness(kernel):
  global img
  if img is None:
    print("Chưa mở ảnh. Vui lòng chọn ảnh trước.")
    return
  sharpness = sharpness_var.get()
  brightness = brightness_var.get()
  sharpened = cv2.filter2D(img, -1, kernel * sharpness)
  adjusted_brightness = cv2.convertScaleAbs(sharpened, alpha=brightness, beta=0)
  cv2.imshow('Sharpened and Brightened Image', adjusted_brightness)


root = tk.Tk()
root.title("Ứng dụng Tăng cường Sắc nét và Độ Sáng Ảnh")

btn_open = tk.Button(root, text="Chọn Ảnh", command=open_image)
btn_open.pack(pady=10)

sharpness_var = tk.DoubleVar()
sharpness_slider = ttk.Scale(root, from_=0.1, to=5.0, variable=sharpness_var, orient="horizontal", length=200)
sharpness_slider.pack(pady=10)
sharpness_slider.set(1.0)

brightness_var = tk.DoubleVar()
brightness_slider = ttk.Scale(root, from_=0.1, to=5.0, variable=brightness_var, orient="horizontal", length=200)
brightness_slider.pack(pady=10)
brightness_slider.set(1.0)

btn_sharpen_1 = tk.Button(root, text="Kernel 1", command=lambda: update_sharpness_and_brightness(kernel_sharpen_1))
btn_sharpen_1.pack(pady=5)

btn_sharpen_2 = tk.Button(root, text="Kernel 2", command=lambda: update_sharpness_and_brightness(kernel_sharpen_2))
btn_sharpen_2.pack(pady=5)

btn_sharpen_3 = tk.Button(root, text="Kernel 3", command=lambda: update_sharpness_and_brightness(kernel_sharpen_3))
btn_sharpen_3.pack(pady=5)

root.mainloop()
