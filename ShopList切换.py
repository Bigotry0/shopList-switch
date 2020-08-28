import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
import configparser
import os
from shutil import copyfile

path_current=os.getcwd()+'\\Config.ini'
shoplist_path=os.getcwd()+'\\shoplist'

Config=configparser.ConfigParser()#读取Config.ini文件内容，读取path内容，读取当前shoplist
Config.read(path_current)
path=Config.get('path','current')
shoplist=Config.get('path','shoplist')

window=tk.Tk()#创建window窗体
window.title('ShopList select')
window.geometry('720x600')

prompt=tk.Label(window,text='当前选择的ShopList为:'+shoplist,font=('Arial',16),width=30,height=1)#Label提升框
prompt.pack(side='top')

frame_select_path=tk.Frame()#facility目录设置器frame
frame_select_path.pack(side='bottom')

def button_path():      #打开目录选择器，更新目录，写入ini文件
    global path
    tmp=path
    print(tmp)
    path=filedialog.askdirectory()
    print(path)
    if path=='':     #知识点：当文件选择器未选时，返回值为‘’
        return 0
    text_path.delete(0.0,'end')
    text_path.insert('end',path)
    Config.set('path','current',path)
    Config.write(open(path_current,'w+'))

text_path=tk.Text(frame_select_path,font=('Arial,12'),height=1)#路径文本显示
text_path.pack(side='left')
text_path.insert('end',path)

button_path=tk.Button(frame_select_path,text='选择目录',font=('Arial',12),width=14,height=1,command=button_path)#路径选择按钮
button_path.pack(side='right')

frame_radiobutton=tk.Frame(window)#radiobutton组frame
frame_radiobutton.pack()

var_filename=tk.StringVar()#radiobutton关联变量
var_filename.set(shoplist)#初始选项

def select_shoplist():       #radiobutton选择函数
    prompt.config(text='当前选择的ShopList为:'+var_filename.get())

#radiobutton数据
MODES=[('00: Potion - Aqua Sac (1 - 255)','shopList_00.slt'),
       ('01: Torrent Sac - Vaal Hazak Talon (256 - 510)','shopList_01.slt'),
       ('02: Vaal Hazak Wing - Critical Jewel 2 (511 - 765)','shopList_02.slt'),
       ('03: Tenderized Jewel 2 - Unavailable (766 - 1020)','shopList_03.slt'),
       ('04: Unavailable - Acidic Glavenus Spineshell (1021 - 1275)','shopList_04.slt'),
       ('05: Acidic Glavenus Tailedge - Simple Urn (1276 - 1530)','shopList_05.slt'),
       ('06: Grimalkyne Doll - Protectors: Dried Goldenfish (1531 - 1785)','shopList_06.slt'),
       ('07: Troupers: Horned Urchin - Friendship/Physique Jewel 4 (1786 - 2040)','shopList_07.slt'),
       ('08: Satiated/Physique Jewel 4 - Unavailable (2041 - 2295)','shopList_08.slt'),
       ('09: Unavailable - Unavailable (2296 - 2550)','shopList_09.slt'),
       ('10: Unavailable - Unavailable (2251 - 2774)','shopList_10.slt')]

for test,value in MODES:#批量创建radiobutton
    r=tk.Radiobutton(frame_radiobutton,text=test,font=('Arial',14),variable=var_filename,value=value,command=select_shoplist)
    r.pack()

def button_yes():         #确定按钮点击函数
    #文件复制
    shoplist_path_now=shoplist_path+'\\'+var_filename.get()
    copyfile(shoplist_path_now,path+'\\shopList.slt')
    Config.set('path','shoplist',var_filename.get())
    Config.write(open(path_current,'w+'))
    tk.messagebox.showinfo(title='切换成功!',message='按确定返回')

button_yes=tk.Button(window,text='确定',font=('Arial',15),width=6,height=1,command=button_yes)#确定按钮
button_yes.pack()

window.mainloop()
