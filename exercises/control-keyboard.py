import pyautogui

pyautogui.click(100, 100)
pyautogui.typewrite('Hello world', interval=0.2)
print(pyautogui.KEYBOARD_KEYS)
pyautogui.hotkey('ctrl', 'o')