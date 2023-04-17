import tkinter
import urllib.request
import zipfile
import os
import tkinter.ttk
import requests
import json

latest_url = f'https://api.github.com/repos/newkincode/simple_farming_game/releases/latest'

latest_response = requests.get(latest_url)
latest_releases = json.loads(latest_response.text)

window = tkinter.Tk()
window.title("openinstalll")
window.geometry("600x300")

def show_progress(block_num, block_size, total_size):
    percent = int(block_num * block_size * 100 / total_size)
    progressbar["value"] = percent
    window.update_idletasks()

def download():
    url = f"https://github.com/newkincode/simple_farming_game/releases/download/{latest_releases['tag_name']}/dist.zip"
    urllib.request.urlretrieve(url, "sfg.zip", show_progress)

def extract():
    with zipfile.ZipFile("sfg.zip", "r") as zip_ref:
        zip_ref.extractall("")
    os.remove("sfg.zip")
    progressbar["value"] = 100
    window.update_idletasks()
    move()

def install():
    frame2.pack()
    frame1.pack_forget()
    frame2.tkraise()
    download()
    extract()

def move():
    
    # 새 폴더 생성
    os.makedirs("C:/Program Files/simple_farming_game", exist_ok=True)
    
    # 파일 이동
    for file_name in os.listdir("main"):
        source_path = os.path.join("main", file_name)
        dest_path = os.path.join("C:/Program Files/simple_farming_game", file_name)
        os.replace(source_path, dest_path)

frame1 = tkinter.Frame(window)
frame2 = tkinter.Frame(window)

install_btn = tkinter.Button(frame1, text='설치를 진행합니다.', command=install)
install_btn.pack()

progressbar = tkinter.ttk.Progressbar(frame2, orient="horizontal", length=300, mode="determinate")
progressbar.pack(pady=10)

frame1.pack()
frame1.tkraise()

window.mainloop()