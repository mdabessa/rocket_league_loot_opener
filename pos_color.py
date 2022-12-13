# Screen pixel color
import pyautogui

a = (1920, 1080)
b = (90,305)
color = pyautogui.pixel(*b)

print("relative:", b[0] / a[0], b[1] / a[1])
print("color:", color)
