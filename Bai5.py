import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import butter, filtfilt
import tkinter as tk
from tkinter import ttk, messagebox

# Initialize the Tkinter window
root = tk.Tk()
root.title("Phần mềm hỗ trợ học tập môn xử lý tín hiệu số")
root.geometry("600x600")

### Các chức năng tạo tín hiệu ###
def generate_signal():
    try:
        freq = float(entry_freq.get())
        amplitude = float(entry_amplitude.get())
        t = np.linspace(0, 1, 500)  # Tạo trục thời gian từ 0 đến 1 giây, 500 mẫu

        # Chọn loại tín hiệu dựa trên người dùng chọn
        signal_type = signal_type_var.get()
        if signal_type == "Sin":
            signal = amplitude * np.sin(2 * np.pi * freq * t)
        elif signal_type == "Cos":
            signal = amplitude * np.cos(2 * np.pi * freq * t)
        elif signal_type == "Vuông":
            signal = amplitude * np.sign(np.sin(2 * np.pi * freq * t))
        else:
            signal = np.zeros(len(t))

        # Hiển thị đồ thị tín hiệu
        plt.figure()
        plt.plot(t, signal)
        plt.title(f"Tín hiệu {signal_type} với tần số {freq} Hz")
        plt.xlabel("Thời gian (s)")
        plt.ylabel("Biên độ")
        plt.grid(True)
        plt.show()

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập tần số và biên độ hợp lệ")

### Biến đổi Fourier liên tục ###
def continuous_fourier_transform():
    try:
        freq = float(entry_freq.get())
        amplitude = float(entry_amplitude.get())
        t = np.linspace(0, 1, 500)  # Tạo trục thời gian từ 0 đến 1 giây, 500 mẫu
        signal = amplitude * np.sin(2 * np.pi * freq * t)

        # Tính biến đổi Fourier liên tục
        signal_fft = fft(signal)
        N = len(signal)
        T = 1.0 / 500  # Khoảng cách mẫu
        xf = fftfreq(N, T)[:N//2]

        # Hiển thị phổ tần số của tín hiệu
        plt.figure()
        plt.plot(xf, 2.0/N * np.abs(signal_fft[:N//2]))
        plt.title(f"Phổ Fourier liên tục của tín hiệu {freq} Hz")
        plt.xlabel("Tần số (Hz)")
        plt.ylabel("Biên độ")
        plt.grid(True)
        plt.show()

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập tần số và biên độ hợp lệ")

### Lọc tín hiệu ###
def apply_filter():
    try:
        freq = float(entry_freq.get())
        amplitude = float(entry_amplitude.get())
        t = np.linspace(0, 1, 500)  # Tạo trục thời gian từ 0 đến 1 giây, 500 mẫu
        signal = amplitude * np.sin(2 * np.pi * freq * t)

        # Bộ lọc thông thấp
        cutoff_freq = 10  # Tần số cắt cho bộ lọc thông thấp
        b, a = butter(4, cutoff_freq, 'low', fs=500)  # Tạo bộ lọc Butterworth bậc 4
        filtered_signal = filtfilt(b, a, signal)

        # Hiển thị tín hiệu sau khi lọc
        plt.figure()
        plt.plot(t, signal, label="Tín hiệu gốc")
        plt.plot(t, filtered_signal, label="Tín hiệu sau khi lọc")
        plt.title("Lọc thông thấp")
        plt.xlabel("Thời gian (s)")
        plt.ylabel("Biên độ")
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập tần số và biên độ hợp lệ")

### Giao diện người dùng ###
label_title = tk.Label(root, text="Phần mềm xử lý tín hiệu số", font=("Helvetica", 16))
label_title.pack(pady=10)

# Khung tạo tín hiệu
signal_frame = tk.Frame(root)
signal_frame.pack(pady=10)

label_freq = tk.Label(signal_frame, text="Tần số tín hiệu (Hz):")
label_freq.grid(row=0, column=0, padx=5, pady=5)
entry_freq = tk.Entry(signal_frame)
entry_freq.grid(row=0, column=1, padx=5, pady=5)

label_amplitude = tk.Label(signal_frame, text="Biên độ tín hiệu:")
label_amplitude.grid(row=1, column=0, padx=5, pady=5)
entry_amplitude = tk.Entry(signal_frame)
entry_amplitude.grid(row=1, column=1, padx=5, pady=5)

# Loại tín hiệu
signal_type_var = tk.StringVar(value="Sin")
signal_type_label = tk.Label(signal_frame, text="Loại tín hiệu:")
signal_type_label.grid(row=2, column=0, padx=5, pady=5)
signal_type_menu = ttk.Combobox(signal_frame, textvariable=signal_type_var, values=["Sin", "Cos", "Vuông"])
signal_type_menu.grid(row=2, column=1, padx=5, pady=5)

# Nút tạo tín hiệu
generate_button = tk.Button(signal_frame, text="Tạo tín hiệu", command=generate_signal)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Nút biến đổi Fourier liên tục
cft_button = tk.Button(root, text="Biến đổi Fourier liên tục", command=continuous_fourier_transform)
cft_button.pack(pady=10)

# Nút áp dụng bộ lọc
filter_button = tk.Button(root, text="Lọc thông thấp", command=apply_filter)
filter_button.pack(pady=10)

# Chạy chương trình
root.mainloop()
