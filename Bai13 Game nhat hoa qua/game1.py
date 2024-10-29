import pygame, sys
from pygame.locals import *
import random
import time
from tkinter import messagebox, Tk

# Chiều dài và chiều cao cửa sổ
WINDOWWIDTH = 800
WINDOWHEIGHT = 500

pygame.init()
w = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

# Load hình ảnh nền và các vật thể
BG = pygame.image.load('background.png')
BG = pygame.transform.scale(BG, (WINDOWWIDTH, WINDOWHEIGHT))

tao = pygame.image.load('sword3.png')
tao = pygame.transform.scale(tao, (40, 50))
cam = pygame.image.load('sword1.png')
cam = pygame.transform.scale(cam, (40, 50))
xoai = pygame.image.load('sword2.png')
xoai = pygame.transform.scale(xoai, (40, 50))

shield1 = pygame.image.load('shield1.png')
shield1 = pygame.transform.scale(shield1, (40, 50))
shield2 = pygame.image.load('shield2.png')
shield2 = pygame.transform.scale(shield2, (40, 50))

# Load hình ảnh nút
pause_button = pygame.image.load('pause.png')
pause_button = pygame.transform.scale(pause_button, (50, 50))
exit_button = pygame.image.load('exit.png')
exit_button = pygame.transform.scale(exit_button, (50, 50))

FPS = 20
fpsClock = pygame.time.Clock()

diem = 0
time0 = time.time()
paused = False

# Tọa độ ban đầu và tốc độ của vật thể
xtao = 0
xcam = WINDOWWIDTH
xxoai = 0
x_shield1 = WINDOWWIDTH
x_shield2 = WINDOWWIDTH
y_tao = random.randint(0, WINDOWHEIGHT - 50)
y_cam = random.randint(0, WINDOWHEIGHT - 50)
y_xoai = random.randint(0, WINDOWHEIGHT - 50)
y_shield1 = random.randint(0, WINDOWHEIGHT - 50)
y_shield2 = random.randint(0, WINDOWHEIGHT - 50)

# Tốc độ di chuyển ban đầu
toc_do_tao = random.randint(5, 10)
toc_do_cam = random.randint(5, 10)
toc_do_xoai = random.randint(5, 10)
toc_do_shield1 = random.randint(5, 10)
toc_do_shield2 = random.randint(5, 10)

# Thời gian hồi của skill
freeze_cooldown = 10
destroy_cooldown = 20
last_freeze_time = -freeze_cooldown
last_destroy_time = -destroy_cooldown

# Trạng thái skill
frozen = False
freeze_duration = 3
freeze_start_time = 0

while True:
    current_time = time.time()
    for event in pygame.event.get():
        if event.type == QUIT:
            root = Tk()
            root.withdraw()  # Ẩn cửa sổ chính của Tkinter
            if messagebox.askyesno("Exit", "Bạn có muốn thoát không?"):
                pygame.quit()
                sys.exit()
            root.destroy()
        if event.type == pygame.MOUSEBUTTONDOWN:  # sự kiện bấm chuột
            if 750 < event.pos[0] < 800 and 0 < event.pos[1] < 50:  # Nút dừng
                paused = not paused
            if 700 < event.pos[0] < 750 and 0 < event.pos[1] < 50:  # Nút thoát
                root = Tk()
                root.withdraw()  # Ẩn cửa sổ chính của Tkinter
                if messagebox.askyesno("Exit", "Bạn có muốn thoát không?"):
                    pygame.quit()
                    sys.exit()
                root.destroy()
            if not paused:
                if xtao - 40 < event.pos[0] < xtao + 40 and y_tao < event.pos[1] < y_tao + 50:
                    diem += 5
                    xtao = 0
                    y_tao = random.randint(0, WINDOWHEIGHT - 50)
                    toc_do_tao = random.randint(5, 10)
                elif xcam - 40 < event.pos[0] < xcam + 40 and y_cam < event.pos[1] < y_cam + 50:
                    diem += 5
                    xcam = WINDOWWIDTH
                    y_cam = random.randint(0, WINDOWHEIGHT - 50)
                    toc_do_cam = random.randint(5, 10)
                elif xxoai - 40 < event.pos[0] < xxoai + 40 and y_xoai < event.pos[1] < y_xoai + 50:
                    diem += 5
                    xxoai = 0
                    y_xoai = random.randint(0, WINDOWHEIGHT - 50)
                    toc_do_xoai = random.randint(5, 10)
                elif x_shield1 - 40 < event.pos[0] < x_shield1 + 40 and y_shield1 < event.pos[1] < y_shield1 + 50:
                    diem += 5
                    x_shield1 = WINDOWWIDTH
                    y_shield1 = random.randint(0, WINDOWHEIGHT - 50)
                    toc_do_shield1 = random.randint(5, 10)
                elif x_shield2 - 40 < event.pos[0] < x_shield2 + 40 and y_shield2 < event.pos[1] < y_shield2 + 50:
                    diem += 5
                    x_shield2 = WINDOWWIDTH
                    y_shield2 = random.randint(0, WINDOWHEIGHT - 50)
                    toc_do_shield2 = random.randint(5, 10)
        if event.type == pygame.KEYDOWN and not paused:
            # Kích hoạt skill đóng băng
            if event.key == K_f and current_time - last_freeze_time >= freeze_cooldown:
                frozen = True
                freeze_start_time = current_time
                last_freeze_time = current_time
            # Kích hoạt skill phá hủy tất cả
            if event.key == K_d and current_time - last_destroy_time >= destroy_cooldown:
                diem += 25
                xtao = 0
                y_tao = random.randint(0, WINDOWHEIGHT - 50)
                xcam = WINDOWWIDTH
                y_cam = random.randint(0, WINDOWHEIGHT - 50)
                xxoai = 0
                y_xoai = random.randint(0, WINDOWHEIGHT - 50)
                x_shield1 = WINDOWWIDTH
                y_shield1 = random.randint(0, WINDOWHEIGHT - 50)
                x_shield2 = WINDOWWIDTH
                y_shield2 = random.randint(0, WINDOWHEIGHT - 50)
                last_destroy_time = current_time

    if not paused:
        # Kiểm tra thời gian đóng băng
        if frozen:
            if current_time - freeze_start_time > freeze_duration:
                frozen = False
        else:
            # Cập nhật tọa độ x của các vật thể khi không đóng băng
            xtao += toc_do_tao
            xcam -= toc_do_cam
            xxoai += toc_do_xoai
            x_shield1 -= toc_do_shield1
            x_shield2 -= toc_do_shield2

    # Vẽ nền và các vật thể
    w.blit(BG, (0, 0))
    w.blit(tao, (xtao, y_tao))
    w.blit(cam, (xcam, y_cam))
    w.blit(xoai, (xxoai, y_xoai))
    w.blit(shield1, (x_shield1, y_shield1))
    w.blit(shield2, (x_shield2, y_shield2))
    w.blit(pause_button, (750, 0))
    w.blit(exit_button, (700, 0))

    # Nếu vật thể đi ra khỏi cửa sổ, đặt lại vị trí và tốc độ
    if xtao > WINDOWWIDTH:
        xtao = 0
        y_tao = random.randint(0, WINDOWHEIGHT - 50)
        toc_do_tao = random.randint(5, 10) + diem // 10

    if xcam < 0:
        xcam = WINDOWWIDTH
        y_cam = random.randint(0, WINDOWHEIGHT - 50)
        toc_do_cam = random.randint(5, 10) + diem // 10

    if xxoai > WINDOWWIDTH:
        xxoai = 0
        y_xoai = random.randint(0, WINDOWHEIGHT - 50)
        toc_do_xoai = random.randint(5, 10) + diem // 10

    if x_shield1 < 0:
        x_shield1 = WINDOWWIDTH
        y_shield1 = random.randint(0, WINDOWHEIGHT - 50)
        toc_do_shield1 = random.randint(5, 10) + diem // 10

    if x_shield2 < 0:
        x_shield2 = WINDOWWIDTH
        y_shield2 = random.randint(0, WINDOWHEIGHT - 50)
        toc_do_shield2 = random.randint(5, 10) + diem // 10

    # Hiển thị điểm và thời gian chơi
    font = pygame.font.SysFont('Arial', 30)
    text = font.render('Tong diem: {}'.format(diem), True, (255, 0, 0))
    text1 = font.render('Thoi gian: {}'.format(int(current_time - time0)), True, (255, 0, 0))
    text2 = font.render('Skill Freeze (F) Cooldown: {:.1f}s'.format(max(0, freeze_cooldown - (current_time - last_freeze_time))), True, (0, 255, 0))
    text3 = font.render('Skill Destroy (D) Cooldown: {:.1f}s'.format(max(0, destroy_cooldown - (current_time - last_destroy_time))), True, (0, 255, 0))
    w.blit(text, (50, 50))
    w.blit(text1, (50, 80))
    w.blit(text2, (50, 110))
    w.blit(text3, (50, 140))

    # Cập nhật màn hình
    pygame.display.update()
    fpsClock.tick(FPS)
