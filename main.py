import pyautogui
import os
import webbrowser
import win32gui
import win32con

rep = input('Repo name? : ')
url = f'https://github.com/username/{rep}.git'

def createRepo(name):
	webbrowser.open('https://github.com/new')
	pyautogui.sleep(3)
	handle = win32gui.GetForegroundWindow()
	win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)
	pyautogui.moveTo(622,447)
	pyautogui.click()
	pyautogui.write(name, interval=0.2)
	pyautogui.PAUSE = 1
	pyautogui.keyDown('enter')

createRepo(rep)

commands = ['init', f'echo ##{rep} > Readme.md', 'add .', 'commit -m "initial"', 'branch -M main',f'remote add origin {url}','push -u origin main']
try:
	for command in commands:
		if 'echo' in command:
			os.system(command)
		else:
			os.system(f'git {command}')
except KeyboardInterrupt:
	print('LOL cancelling!')


print('Done!')

os.system('subl .')

url = url.strip('.git')
webbrowser.open(url)
