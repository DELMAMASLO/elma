import_pyautogui, sleep
time.sleep(5)
f = open("beemovie", 'r')
for word in f:
 pyautogui.typewrite(word)
 pyautogui.press("enter")
