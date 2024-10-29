import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image  # Import thư viện Pillow

# Define kernels for smoothing
kernel_3x3 = np.ones((3, 3), np.float32) / 9.0
kernel_5x5 = np.ones((5, 5), np.float32) / 25.0


def apply_filter(kernel):
  global img
  if img is not None:
    output = cv2.filter2D(img, -1, kernel)
    cv2.imshow('Ảnh làm mịn', output)
  else:
    print("Vui lòng mở ảnh trước khi áp dụng bộ lọc.")


def open_image():
  global img
  file_path = filedialog.askopenfilename()

  try:
    # Mở ảnh bằng Pillow
    pil_image = Image.open(file_path)
    pil_image = pil_image.resize((700, 700))  # Thay đổi kích thước ảnh bằng Pillow

    # Chuyển ảnh từ Pillow sang OpenCV
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    cv2.imshow('Ảnh gốc', img)
  except Exception as e:
    print("Không thể mở tệp. Lỗi:", e)


def smooth_image_3x3():
  apply_filter(kernel_3x3)


def smooth_image_5x5():
  apply_filter(kernel_5x5)


# Initialize GUI
root = tk.Tk()
root.title("Ứng dụng Làm Mịn Ảnh")

btn_open = tk.Button(root, text="Mở Ảnh", command=open_image)
btn_open.pack(pady=10)

btn_smooth_3x3 = tk.Button(root, text="Làm mịn 3x3", command=smooth_image_3x3)
btn_smooth_3x3.pack(pady=5)

btn_smooth_5x5 = tk.Button(root, text="Làm mịn 5x5", command=smooth_image_5x5)
btn_smooth_5x5.pack(pady=5)

btn_quit = tk.Button(root, text="Thoát", command=root.quit)
btn_quit.pack(pady=10)

root.mainloop()
