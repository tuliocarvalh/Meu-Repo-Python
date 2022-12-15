import pyautogui as pg
from time import sleep
import pyperclip as pc
import re
import os

page_repo = "https://github.com/tuliocarvalh?tab=repositories"
diretorio_repo = "cd c:/portfolio/python/"
git = "https://github.com/tuliocarvalh/"

def init() :
    os.system("start Chrome.exe")
    sleep(1)
    pg.hotkey('win', 'up')
    
def writing(self) :
    pg.write(self)

def new_hub(self) :
    sleep(5)
    pg.click(389, 51)
    sleep(0.5)
    pc.copy(page_repo)
    pg.hotkey('ctrl', 'v')
    sleep(2)
    pg.press('enter')
    sleep(4)
    pg.click(1241, 263) #new repo
    sleep(3)
    pg.click(567, 364) #name repo
    sleep(2)
    writing(self)
    sleep(2)
    pg.click(329, 698) #add readme
    sleep(2)
    pg.click(1135, 231) #aleatory
    sleep(0.5)
    pg.press('end')
    sleep(2)
    pg.click(394, 564) #create repo
    sleep(3)
    pg.click(916, 311) #code 1
    sleep(2)
    pg.click(918, 493) #code 2
    link_repo = pc.paste()
    obj = open('links.txt','a')
    obj.write(f"{self} - {link_repo} \n ")
    obj.close()
    
def enter_terminal() :
    pg.press('win')
    sleep(0.5)
    pg.write('anaconda')
    sleep(0.5)
    pg.press('enter')
    sleep(8)

def clone_repo(self) :
    repo_name = self.replace(" ", "-")
    writing(diretorio_repo + self)
    sleep(0.5)
    pg.press('enter')
    sleep(1)
    writing('git clone ' + git + repo_name + ".git")
    sleep(1)
    pg.press('enter')
    sleep(7)

def push_repo(self) :
    comand = "git add ."
    comand2 = 'git commit -m "First codes"'
    comand3 = "git push"
    user = "tuliocarvalh"
    token = "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"
    repo_name = self.replace(" ", "-")
    writing(diretorio_repo + self + "/" + repo_name)
    sleep(0.5)
    pg.press('enter')
    writing(comand)
    sleep(0.5)
    pg.press('enter')
    sleep(2)
    writing(comand2)
    sleep(0.5)
    pg.press('enter')
    sleep(2)
    writing(comand3)
    sleep(0.5)
    pg.press('enter')
    sleep(8)
    writing(user)
    sleep(0.5)
    pg.press('enter')
    sleep(3)
    writing(token)
    sleep(0.5)
    pg.press('enter')
    sleep(4)



