import pyautogui, pyperclip, time, random
print("\nSPAM ZALO MESS BY PHẠM ĐÔ")
msg = input("Nhập từ spam: ").split(" , ")
n = int(input("Số lần muốn Spam: "))
m = float(input("Delay: "))


#Chuẩn bị
print("\nChuan bi")
for i in range(5,0,-1):
    print(i,end=" ",flush=True)
    time.sleep(1)
print("\nBat dau")
#Spam
for j in range(n):
    pyperclip.copy(random.choice(msg))
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(m) #Delay