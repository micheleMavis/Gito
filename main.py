import pyautogui
import os
import webbrowser
import win32gui
import win32con
import platform
import subprocess

# Constants
GITHUB_NEW_REPO_URL = 'https://github.com/new'
PAUSE_DURATION = 1

def get_github_username():
    return input('GitHub username? : ')

def get_repo_name():
    return input('Repo name? : ')

def construct_repo_url(username, repo_name):
    return f'https://github.com/{username}/{repo_name}.git'

def open_github_new_repo_page():
    webbrowser.open(GITHUB_NEW_REPO_URL)
    pyautogui.sleep(3)
    handle = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)

def create_repo_on_github(repo_name):
    open_github_new_repo_page()
    pyautogui.sleep(3)
    
    # Use image recognition instead of coordinates
    if not safe_click('repo_name_box.png'):
        return
    
    pyautogui.write(repo_name, interval=0.2)
    pyautogui.PAUSE = PAUSE_DURATION
    pyautogui.press('enter')
    pyautogui.press('enter')

def execute_git_commands(repo_name, repo_url):
    commands = [
        'init',
        f'echo ## {repo_name} > Readme.md',
        'add .',
        'commit -m "initial"',
        'branch -M main',
        f'remote add origin {repo_url}',
        'push -u origin main'
    ]
    try:
        for command in commands:
            result = os.system(f'git {command}')
            if result != 0:
                raise Exception(f'Error executing: git {command}')
    except Exception as e:
        print(f"Failed to execute git command: {e}")

def open_repo_in_editor():
    try:
        if platform.system() == 'Windows':
            os.system('subl .')
        else:
            subprocess.run(['code', '.'])  # Use VSCode on other platforms
    except Exception as e:
        print(f"Failed to open editor: {e}")

def open_repo_in_browser(repo_url):
    webbrowser.open(repo_url[:-4])

def main():
    username = get_github_username()
    repo_name = get_repo_name()
    repo_url = construct_repo_url(username, repo_name)
    create_repo_on_github(repo_name)
    execute_git_commands(repo_name, repo_url)
    print('Done!')
    open_repo_in_editor()
    open_repo_in_browser(repo_url)

if __name__ == "__main__":
    main()
