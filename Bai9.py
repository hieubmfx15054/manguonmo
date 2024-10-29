import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def open_image():
    global img
    file_path = filedialog.askopenfilename()
    try:
        # Mở ảnh bằng Pillow
        pil_image = Image.open(file_path)
        pil_image = pil_image.resize((700, 700))

        # Chuyển đổi từ Pillow sang OpenCV
        img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
        cv2.imshow('Ảnh gốc', img)
    except Exception as e:
        print("Không thể mở tệp. Lỗi:", e)

def edge_detection():
    global img
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Chuyển ảnh sang thang độ xám
        edges = cv2.Canny(gray, 100, 200)  # Áp dụng bộ lọc Canny
        cv2.imshow('Ảnh tách biên', edges)
    else:
        print("Vui lòng mở ảnh trước khi áp dụng tách biên.")

# Thiết lập giao diện
root = tk.Tk()
root.title("Ứng dụng Tách Biên Ảnh")

btn_open = tk.Button(root, text="Mở Ảnh", command=open_image)
btn_open.pack(pady=10)

btn_edge_detection = tk.Button(root, text="Tách Biên", command=edge_detection)
btn_edge_detection.pack(pady=5)

btn_quit = tk.Button(root, text="Thoát", command=root.quit)
btn_quit.pack(pady=10)

root.mainloop()
